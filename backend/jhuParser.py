import csv
import pandas as pd

jhuDataCSV = pd.read_csv('./jhuData.csv')
date_specific_df = jhuDataCSV.loc[(jhuDataCSV['date']=='2021-01-19') & (jhuDataCSV['country']=='Afghanistan')]
date_spec_2 = jhuDataCSV.loc[(jhuDataCSV['date']=='2021-01-30') & (jhuDataCSV['country']=='Afghanistan')]
print(date_specific_df)
print(date_spec_2)


