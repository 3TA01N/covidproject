import os
import psycopg2
from config import config
from datetime import datetime, timedelta
from pathlib import Path
import urllib.request
import csv
import pandas as pd
import io
import numpy as np
import sys
import yfinance as yf


import os

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
application = get_wsgi_application()
from covid19.models import StockData

date_list = list(StockData.objects.values_list('date', flat=True))
print(max(date_list))
lastDate = max(date_list)
last_date = datetime.combine(lastDate, datetime.min.time())
print(type(lastDate))


insertDF = pd.DataFrame()
stockDataCSV = (pd.read_csv("SPYHistorical.csv", usecols=['Symbol', 'Date', 'Open', 'High', 'Low', 'Close']))
stockDataCSV['Date'] = pd.to_datetime(stockDataCSV['Date'])

currentDir = os.path.dirname(os.path.abspath(__file__))
spy = yf.Ticker('SPY')
#if (stockDataCSV.empty):
 #   last_date = datetime(2020, 1, 22)
#else:
 #   last_date = stockDataCSV['Date'].max()
    #last_date = datetime(2020, 1, 22)
date_now = datetime.now() + timedelta(days=1)
    #print(last_date)
    #print(datetime.now())
#last_date = datetime(2020, 1, 22)



def pull_stock_data(date1, date2):
        str_start = date1.strftime('%Y-%m-%d')
        str_end = date2.strftime('%Y-%m-%d')
        spy_data = spy.history(start=str_start, end=str_end)
        spy_data.drop(['Volume', 'Dividends', 'Stock Splits'], axis=1, inplace=True)
        spy_data['Symbol'] = 'SPY'
        spy_data['Date'] = spy_data.index
        spy_data = spy_data.reindex(columns=['Symbol', 'Date', 'Open', 'High', 'Low', 'Close'])
        if (not spy_data['Date'].is_unique):
            spy_data = spy_data[0:0]
        print(spy_data)
        spy_data = spy_data.drop_duplicates()
        spy_data.to_csv(os.path.join(currentDir, 'SPYHistorical.csv'), index=False)
        spy_data.to_csv(os.path.join(currentDir, 'stockDataCSV.csv'), index=False)



pull_stock_data(last_date, date_now)


