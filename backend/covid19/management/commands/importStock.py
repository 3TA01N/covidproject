
from covid19.models import StockData
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        insert_count = StockData.objects.from_csv('./StockDataCSV.csv',ignore_conflicts=True)
#print "{} records inserted".format(insert_count)
