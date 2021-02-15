import csv
import pandas as pd


df = pd.DataFrame(columns =['state','country','date','cases','deaths']) 
df.to_csv('./jhuData.csv', index=False)
jhuDataCSV = pd.read_csv('./jhuData.csv')
jhuDataCSV['date'] = pd.to_datetime(jhuDataCSV['date'])
insertDataCSV = pd.read_csv('./insertData.csv')
print(len(jhuDataCSV.index))
print(len(insertDataCSV.index))

print(insertDataCSV[jhuDataCSV.duplicated(keep=False)])
date_specific_df = jhuDataCSV.loc[(jhuDataCSV['date']=='2021-02-01') & (jhuDataCSV['country']=='Afghanistan')]
date_spec_2 = jhuDataCSV.loc[(jhuDataCSV['date']=='2021-01-30') & (jhuDataCSV['country']=='Afghanistan')]
print(insertDataCSV['date'])
print(date_spec_2)
