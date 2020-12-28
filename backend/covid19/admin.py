from django.contrib import admin

# Register your models here.
from .models import CGraph
from .models import CovidCases


class CGraphAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'description')  # add this


class CovidCasesAdmin(admin.ModelAdmin):
    list_display = ('state', 'country', 'date', 'cases', 'deaths')


# Register your models here.
admin.site.register(CGraph, CGraphAdmin)  # add this
admin.site.register(CovidCases, CovidCasesAdmin)
