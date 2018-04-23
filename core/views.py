from django.shortcuts import render
from django.conf import settings
import requests

def home(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://freegeoip.net/json/%s' % ip_address)
    geodata = response.json()
    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': settings.GOOGLE_MAPS_API_KEY
    })
