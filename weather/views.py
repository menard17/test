# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    cities = City.objects.all()

    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save()

    form = CityForm()
    weather_data = []

    for city in cities:
        result = get_lat_and_lot(city)
        city_weather = get_city_weather(result['let'], result['lot'])

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/index.html', context)


def get_city_weather(let, lon):
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=imperial&appid=38a41446166aa138e56e54109684934d'
    return requests.get(url.format(let, lon)).json()


def get_lat_and_lot(location):
    url = 'http://api.openweathermap.org/geo/1.0/direct?q={}&appid=38a41446166aa138e56e54109684934d'
    result = requests.get(url.format(location)).json()
    return {'let': result[0]["lat"], 'lon': result[0]["lon"]}
