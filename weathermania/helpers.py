from flask import request
from config import weather_api_key
import requests

# --------------------------------------------------------------------------------------------
# Method Name: get_city_info
# Purpose: Returns latitude, longitude, country, and state of specified city name. 
# --------------------------------------------------------------------------------------------

def get_city_info(city_name):
    payload = {'q': city_name, 'appid': weather_api_key}
    response = requests.get(
                "http://api.openweathermap.org/geo/1.0/direct",
                params=payload
    )
    data = response.json() # deserializes
    return data[0] # dictionary within a list