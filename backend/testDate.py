import os

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
application = get_wsgi_application()
from covid19.models import CovidCases

date_list = list(CovidCases.objects.values_list('date', flat=True))
print(max(date_list))
