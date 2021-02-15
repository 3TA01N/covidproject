from .models import CovidCases
from .models import StockData
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
    #print(countryData)
    stock_list = []
    data_list = []
    if 'symbol' in request.data.keys():
        symbolName = request.data['symbol']
        stocks = StockData.objects.filter(symbol = symbolName).order_by('date')
        for data_element in stocks:
            stock_list.append({
                'date': data_element.date,
                'open': data_element.open,
                'close': data_element.close,
                'volume': data_element.volume
                })

    for data_element in countryData:
        data_list.append({
            'date': data_element.date,
            'cases': data_element.cases,
            'deaths': data_element.deaths
        })
    print(data_list)
    return JsonResponse({'covid_data': data_list, 'stock_data': stock_list}, status=200)
