import csv
import pandas as pd



jhuDataCSV = pd.read_csv('./jhuData.csv')
print(jhuDataCSV['date'])
date_specific_df = jhuDataCSV.loc[(jhuDataCSV['date']=='2021-01-09') & (jhuDataCSV['country']=='Afghanistan')]
date_spec_2 = jhuDataCSV.loc[(jhuDataCSV['date']=='2021-01-10') & (jhuDataCSV['country']=='Afghanistan')]
print(date_specific_df)
print(date_spec_2)
