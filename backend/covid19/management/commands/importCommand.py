from covid19.models import CovidCases
from covid19.models import StockData
import pandas as pd
from django.core.management.base import BaseCommand
from datetime import datetime

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        jhudataPD = (pd.read_csv("jhuData.csv", usecols=['state','country','date','cases','deaths']))
        csvDate = jhudataPD['date'].max()
        dbDate = max(CovidCases.objects.values_list('date', flat=True))
        csvDate = datetime.strptime(csvDate,'%Y-%m-%d')
        dbDate = datetime.combine(dbDate, datetime.min.time())
        importCase = True
        if csvDate==dbDate:
            print(type(dbDate))
            print(type(csvDate))
            importCase = False

        importStock = True
        stockPD = (pd.read_csv("stockDataCSV.csv"))
        dbDateS = max(StockData.objects.values_list('date', flat=True))
        if stockPD.empty:
            csvDateS = dbDateS
        else:
            csvDateS = stockPD['Date'].max()
            print(type(csvDateS))
            print(csvDateS)
       # quit()
       
            csvDateS = datetime.strptime(csvDateS,'%Y-%m-%d')
            dbDateS = datetime.combine(dbDateS, datetime.min.time())
       # importStock = True
        if csvDateS!=dbDateS:
            print(dbDateS)
            print(csvDateS)
            print("added new entries to StockData")
            StockData.objects.from_csv('./stockDataCSV.csv', dict(symbol='Symbol',date='Date',open='Open',high='High',low='Low',close='Close'))
        

        f = open('./lastDate.txt', 'r')
        run = f.readline()
        if run=="run" and importCase:
            print("added new entries to covidCases")
            insert_count = CovidCases.objects.from_csv('./insertData.csv',ignore_conflicts=True)
        f.close()
        #print "{} records inserted".format(insert_count)
