from django.shortcuts import render
from django.conf import settings
import requests

def home(request):
    is_cached = ('geodata' in request.session)

    if not is_cached:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
        response = requests.get('http://freegeoip.net/json/%s' % ip_address)
        request.session['geodata'] = response.json()

    geodata = request.session['geodata']

    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': settings.GOOGLE_MAPS_API_KEY,
        'is_cached': is_cached
    })

def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
    return render(request, 'core/github.html', {'user': user})
