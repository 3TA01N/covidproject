
from django.core.management.base import BaseCommand, CommandError
from covid19.models import CovidCases
class Commmand(BaseCommand):
    for row in CovidCases.objects.all().reverse():
        if CovidCases.objects.filter(date=row.date).count() > 1 and CovidCases.objects.filter(state=row.date).count() > 1 and CovidCases.objects.filter(country=row.country).count()> 1:
            row.delete()
