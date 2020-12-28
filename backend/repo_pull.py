import os
from git import Repo
import psycopg2
from config import config
from datetime import datetime
from pathlib import Path
import csv 
import pandas as pd
import io
import numpy as np
from contextlib import closing

insertDF = pd.DataFrame()
date = datetime(2020, 11, 4)



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


            
def gitPull():
    repo_path = os.getenv('/mnt/c/Users/Kevin/covidprojectfolder/backend')
    repo = Repo(repo_path, search_parent_directories=True)
    o = repo.remotes.origin
    if not repo.bare:
        current = repo.head.commit
        o.pull()
        if current == repo.head.commit:
            print("no change")
        # conn = connect(config())
        # insertQuery = """INSERT INTO head_id (head_id)
        # VALUES(%s)""" 7
        # cur = conn.cursor()
        # cur.execute(insertQuery, (repo.head.object.hexsha,))
        # print ("hi")
        # conn.commit()
        # cur.close()
    else:
        print('Could not load repository at {} :('.format(repo_path))

def copyfrom(conn, df, table):
    s_buf = io.StringIO()

    #print(df);
    df.to_csv(s_buf, index=None, header=None)
    #print(s_buf.getvalue()[0:1000])
    cur = conn.cursor()
    #print(df.columns.values)
    
    
    print(df[640:650])
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
    #gitPull()    
    
    for entry in os.scandir('/mnt/c/Users/Kevin/covidprojectfolder/backend/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports'):
        if entry.path.endswith(".csv") and datetime.strptime(Path(entry).stem, '%m-%d-%Y')>date:
            df = pd.read_csv(entry,index_col=0)
            sumUsDF = pd.DataFrame()
            stateList = pd.DataFrame()
            temp = pd.DataFrame()
            tempLong = 0;
            tempLat = 0;
            df = df.filter(['Province_State','Country_Region','Lat','Long','Long_','Confirmed','Deaths','Recovered'])
            usDF = (df.groupby(df.Country_Region)).get_group("US")
            #print(usDF)
            usDF.fillna(0, inplace=True)
            stateList = usDF['Province_State'].unique()
            columnList = ['Confirmed','Deaths','Recovered','Active']

            #print(df)
            for i in stateList:
                #print(i)
                temp = (usDF.groupby(usDF.Province_State)).get_group(i)
                tempLat = temp['Lat'].iloc[0]
                if 'Long' in temp.columns:
                    tempLong = temp[((temp.filter(like='Long_',axis=1).columns).values.tolist())[0]].iloc[0]
                else:
                    tempLong = temp[((temp.filter(like='Long_', axis=1).columns).values.tolist())[0]].iloc[0]
                tempState = temp['Province_State'].iloc[0]
                temp = temp.filter(columnList)
                temp = temp.sum(axis=0)

                temp = temp.to_frame().T
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
    #print(insertDF)
    insertDF = insertDF.astype({"Confirmed":'int', "Deaths":'int'})
    insertDF['Province_State'] = insertDF['Province_State'].replace(np.nan, "not provided")
    insertDF['Province_State'] = insertDF['Province_State'].replace(np.nan, "not provided")
    insertDF['Country_Region'] = insertDF['Country_Region'].str.replace(',', ".")
    insertDF['Province_State'] = insertDF['Province_State'].str.replace(',', ".")
    jhuData = insertDF.iloc[:,[0,1,2,5,6]]
    print(jhuData)
    jhuData.columns = ['state','country','date','cases','deaths']
    jhuData.to_csv(r'/mnt/c/Users/Kevin/covidprojectfolder/backend/jhuData.csv', index = False)

    #groupData = jhuData.groupby('Country_Region').get_group('Afghanistan')
    #print(groupData.sort_values('date'))
    #print(jhuData)
    
    #location = insertDF.iloc[:,[2,3,5,6]]
    #print(jhuData.columns)
    conn = connect(config())
    #gitPull()
    #copyfrom(conn, jhuData, 'covid_cases')
    conn.commit()
    conn.close()
    
    