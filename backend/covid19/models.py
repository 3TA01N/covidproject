from django.db import models
from postgres_copy import CopyManager


# Create your models here.

class CGraph(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def _str_(self):
        return self.title


class Location(models.Model):
    state = models.CharField(max_length=20, primary_key=True)
    country = models.CharField(max_length=20)
    latitude = models.DecimalField(decimal_places=10, max_digits=15)
    longitude = models.DecimalField(decimal_places=10, max_digits=15)

    class Meta:
        managed = False
        db_table = 'location'

    def __repr__(self):
        return f'<Location: location object ({self.state}, {self.country}, {self.latitude}, {self.longitude}>'


class CovidCases(models.Model):
    state = models.CharField(max_length=20, primary_key=True)
    country = models.CharField(max_length=20)
    date = models.DateField()
    cases = models.PositiveIntegerField()
    deaths = models.PositiveIntegerField()

    objects = CopyManager()

    class Meta:
        managed = False
        db_table = 'covid_cases'

    def __repr__(self):
        return f'<CovidCases: covid_cases object ({self.state}, {self.country}, {self.date}, {self.cases} {self.deaths}>'
