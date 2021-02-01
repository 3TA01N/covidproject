import os
#from git import Repo
import psycopg2
from config import config
from datetime import datetime, timedelta
from pathlib import Path
import urllib.request
import csv 
import pandas as pd
import io
import numpy as np

from contextlib import closing

insertDF = pd.DataFrame()
currentDir = os.path.dirname(os.path.abspath(__file__))
print(currentDir)
print(os.path.join(currentDir, 'jhuData.csv'))

jhudataPD = (pd.read_csv("jhuData.csv", usecols=['state','country','date','cases','deaths']))
jhudataPD['date'] = pd.to_datetime(jhudataPD['date'])
countryNames = jhudataPD.country.unique()
options = []
ind = 0
for i in countryNames:
    options.append({
        'label': countryNames[ind],
        'value': countryNames[ind]
    })
    ind+=1
#print(jhudataPD.columns)
if (jhudataPD.empty):
    lastDate = datetime(2020, 1, 22)#'2020-01-22'
else:
    lastDate = jhudataPD['date'].max()
print(lastDate)
#print(lastDate)
#lastDate = datetime(2020,1,22)
#print(lastDate)
#lastDate = datetime.strptime(lastDate, '%Y-%m-%d')
#lastDate = datetime(2020, 1, 22)

dateNow = datetime.now()#datetime(2020,3,28)
#print(dateNow)


def connect(param):
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**param)
        print("connected")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("connected")
    return conn


            
def gitPull(date1, date2):
    delta = timedelta(days=1)
    while date1 < date2:
        try:

            #if file with that date already exists, skip
            strDate = date1.strftime("%m-%d-%Y")
            url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/%s.csv' % strDate
            urllib.request.urlretrieve(url, '%s/dailyreports/%s.csv' %(currentDir, strDate))
            print(date1)
            date1 += delta
        except urllib.error.HTTPError as e:
            print("file does not exist yet")
            break


def copyfrom(conn, df, table):
    s_buf = io.StringIO()

    #print(df);
    df.to_csv(s_buf, index=None, header=None)
    #print(s_buf.getvalue()[0:1000])
    cur = conn.cursor()
    #print(df.columns.values)
    
    
    #print(df[640:650])
    v = s_buf.getvalue()
    v = v.replace("\"", "")
    v = v.strip()
   # print(v)
    new_sio = io.StringIO()
    new_sio.seek(0)
    new_sio.write(v)
    new_sio.seek(0)
    s_buf.seek(0)
    cur.copy_from(new_sio, table, null='', sep=',', columns=('state', 'country', 'date', 'cases', 'deaths'))
    conn.commit()
    cur.close()
    
# def getFrom(table, value):
    # conn = connect(config())
    # cursor = conn.cursor()
    # select_Query = "select * 
    
if __name__ == '__main__':
    gitPull(lastDate, dateNow)
    for entry in os.scandir('%s/dailyreports' % currentDir):
        if entry.path.endswith(".csv") and datetime.strptime(Path(entry).stem, '%m-%d-%Y')>lastDate:
            #print(Path(entry).stem)
            df = pd.read_csv(entry)
            sumUsDF = pd.DataFrame()
            stateList = pd.DataFrame()
            temp = pd.DataFrame()
            tempLong = 0;
            tempLat = 0;
            hasLocation = True
            colNameFormat = []
            if 'Province_State' in df.columns:
                df = df.filter(['Province_State','Country_Region','Lat','Long','Long_','Confirmed','Deaths','Recovered'])
            else:
                df = df.filter(['Province/State', 'Country/Region', 'Confirmed','Deaths','Recovered'])
                #print(df.columns)
                df.columns = ['Province_State', 'Country_Region', 'Confirmed','Deaths','Recovered']
                hasLocation = False

            usDF = (df.groupby(df.Country_Region)).get_group("US")
            #print(usDF)
            usDF.fillna(0, inplace=True)
            stateList = usDF['Province_State'].unique()
            columnList = ['Confirmed','Deaths','Recovered','Active']

            #print(df)
            for i in stateList:
                #print(i)
                temp = (usDF.groupby(usDF.Province_State)).get_group(i)
                if hasLocation:
                    tempLat = temp['Lat'].iloc[0]
                    if 'Long' in temp.columns:
                        tempLong = temp[((temp.filter(like='Long_', axis=1).columns).values.tolist())[0]].iloc[0]
                    else:
                        tempLong = temp[((temp.filter(like='Long_', axis=1).columns).values.tolist())[0]].iloc[0]


                else:
                    tempLat = "not given"
                    tempLong = "not given"

                tempState = temp['Province_State'].iloc[0]
                temp = temp.filter(columnList)
                temp = temp.sum(axis=0)

                try:
                    temp = temp.to_frame().T
                except AttributeError:
                    pass
                temp['Lat'] = tempLat
                temp['Long'] = tempLong
                temp['Province_State'] = tempState
                temp['Country_Region'] = "US"
                sumUsDF = pd.concat([temp,sumUsDF], axis=0, ignore_index=True).drop_duplicates().reset_index(drop=True)
                #print(temp)
            #clear
            df = df[df['Country_Region'] != 'US']

            #clear
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            #print(sumUsDF)
            df = pd.concat([df, sumUsDF], axis = 0, ignore_index=True).drop_duplicates().reset_index(drop=True)
            #print(sumUsDF)
            df['date'] = datetime.strptime(Path(entry).stem, '%m-%d-%Y')

            #print(df)
            insertDF=pd.concat([df,insertDF], axis=0, ignore_index=True)
                #

    cTitles = [ 'Province_State','Country_Region','date','Lat','Long_','Confirmed','Deaths','Recovered','Long']
    insertDF = insertDF.reindex(columns=cTitles)
    insertDF[['Province_State']].fillna("not provided",inplace=True)
    insertDF['Confirmed'].fillna(0,inplace=True)
    insertDF['Recovered'].fillna(0, inplace=True)
    insertDF['Deaths'].fillna(0, inplace=True)
    bool1 = pd.isnull(insertDF['Confirmed'])
    bool2 = pd.isnull(insertDF['Deaths'])
    #print([bool1])
    #print([bool2])
    #print(insertDF)
    if insertDF.empty:
        print("no updates since last ran")
        quit()
    insertDF = insertDF.astype({"Confirmed":'int', "Deaths":'int'})
    insertDF['Province_State'] = insertDF['Province_State'].replace(np.nan, "not provided")
    insertDF['Province_State'] = insertDF['Province_State'].replace(np.nan, "not provided")
    insertDF['Country_Region'] = insertDF['Country_Region'].str.replace(',', ".")
    insertDF['Province_State'] = insertDF['Province_State'].str.replace(',', ".")
    jhuData = insertDF.iloc[:,[0,1,2,5,6]]
    print(jhuData)
    jhuData.columns = ['state','country','date','cases','deaths']
    jhuDataCSV = pd.read_csv("jhuData.csv")
    print(jhuData)
    jhuData.drop_duplicates(inplace=True)
    jhuData.to_csv(os.path.join(currentDir, 'insertData.csv'), index = False)
    newCSV = jhuData.append(jhuDataCSV)#jhuData
   # print(newCSV['date'])
    newCSV.drop_duplicates(inplace=True)
    newCSV.to_csv(os.path.join(currentDir, 'jhuData.csv'), index = False)



    conn = connect(config())
    #copyfrom(conn, jhuData, 'covid_cases')
    conn.commit()
    conn.close()
    
    