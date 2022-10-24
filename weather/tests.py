# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.test
import pytest

import weather


@pytest.mark.django_db
class WeatherAPi(django.test.TestCase):
    def get_city_weather(self):
        lat = 36.1673
        lon = -115.1485
        result = weather.views.get_city_weather(lon, lat)
        self.assertEqual("Las Vegas", result['name'])