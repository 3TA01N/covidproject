import os
from datetime import datetime, timedelta
import urllib.request
import pandas as pd
filename = "jhuData.csv"
# opening the file with w+ mode truncates the file
f = open(filename, "w+")
f.close()


# currentDir = os.path.dirname(os.path.abspath(__file__))
#
# def gitPull(date1, date2):
#     delta = timedelta(days=1)
#     while date1 <= date2:
#         try:
#             strDate = date1.strftime("%m-%d-%Y")
#             url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/%s.csv' % strDate
#             urllib.request.urlretrieve(url, '%s/dailyreports/%s.csv' %(currentDir, strDate))
#             print(date1)
#             date1 += delta
#         except urllib.error.HTTPError as e:
#             print("file does not exist yet")
#             break
#
#
# if __name__ == '__main__':
#     jhudataPD = (pd.read_csv("jhuData.csv", usecols=['state','country','date','cases','deaths']))
#     dateo = jhudataPD['date'].iloc[0]
#     dateo = datetime.strptime(dateo, '%Y-%m-%d')
#     datet = datetime.now()
#
#     gitPull(datetime(2020,1,22), datet)