


"""
Get current weather in FRANKFURT
"""

import requests
import json

def get_weather():
    """
    Get current weather in FRANKFURT
    """
    url = 'http://api.openweathermap.org/data/2.5/weather?q=frankfurt&units=metric&APPID=d9d9a9a2f8d0c3d3e8b8f1b7c1b9f0d9'
    r = requests.get(url)
    data = r.json()
    return data

def display_weather(data):
    """
    Display weather
    """
    print(data)



display_weather(get_weather())
