from rest_framework import serializers
from .models import CGraph
from .models import CovidCases

class CGraphSerializer(serializers.ModelSerializer):
  class Meta:
    model = CGraph
    fields = ('id', 'title', 'description')

class CovidCasesSerializer(serializers.ModelSerializer):
  class Meta:
    model = CovidCases
    fields = ('state', 'country', 'date', 'cases', 'deaths')