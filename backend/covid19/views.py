from .models import CovidCases
from rest_framework.decorators import api_view
import csv
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import CGraphSerializer
from .serializers import CovidCasesSerializer
from .models import CGraph


class CGraphView(viewsets.ModelViewSet):
    serializer_class = CGraphSerializer
    queryset = CGraph.objects.all()


class CovidCasesView(viewsets.ModelViewSet):
    serializer_class = CovidCasesSerializer
    queryset = CovidCases.objects.all()
# Create your views here.

@api_view(['GET','POST'])
def getCountryData(request):
    if 'country' not in request.data.keys():
        print(request)
        return JsonResponse({"error" : "country does not exist"}, status = 400)
    countryName = request.data['country']
    countryData = CovidCases.objects.filter(country = countryName).order_by('date')
    print(countryData)
    data_list = []
    for data_element in countryData:
        data_list.append({
            'date': data_element.date,
            'cases': data_element.cases,
            'deaths': data_element.deaths
        })
    return JsonResponse({'data': data_list}, status=200)