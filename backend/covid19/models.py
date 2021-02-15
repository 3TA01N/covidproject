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

class StockData(models.Model):
    symbol = models.CharField(max_length=10)
    date = models.DateField(max_length=20)
    open = models.DecimalField(max_digits=15, decimal_places=7)
    high = models.DecimalField(max_digits=15, decimal_places=7)
    low = models.DecimalField(max_digits=15, decimal_places=7)
    close = models.DecimalField(max_digits=15, decimal_places=7)
    adj_close = models.DecimalField(max_digits=15, decimal_places=7, null=True, blank=True)
    volume = models.PositiveIntegerField()
    objects = CopyManager()

    class Meta:
        managed = False
        db_table = 'covid19_stockdata'
        unique_together = (('symbol', 'date'),)

    def __repr__(self):
        return f'<StockData: covid10_stockdata object ({self.symbol}, {self.date}, {self.open}, {self.high}, {self.low}, {self.close}>'

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
