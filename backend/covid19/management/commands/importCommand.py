from covid19.models import CovidCases
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        insert_count = CovidCases.objects.from_csv('/mnt/c/Users/Kevin/covidprojectfolder/backend/jhuData.csv',ignore_conflicts=True)
        #print "{} records inserted".format(insert_count)