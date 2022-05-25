from flask import request
from config import weather_api_key
import requests

# --------------------------------------------------------------------------------------------
# Method Name: get_city_info
# Purpose: Returns latitude, longitude, country, and state of specified city name. 
# --------------------------------------------------------------------------------------------

def get_city_info(city_name):
    print("***** Retrieving city info for", city_name, "*****")
    payload = {'q': city_name, 'appid': weather_api_key}
    response = requests.get(
                "http://api.openweathermap.org/geo/1.0/direct",
                params=payload
    )
    data = response.json() # deserializes
    # print("DATA FROM CITY INFO: ", data)
    return data[0] # dictionary within a list

# --------------------------------------------------------------------------------------------
# Method Name: get_weather_forecast
# Purpose: Returns JSON representation of requested city's weather forecast.
# --------------------------------------------------------------------------------------------

def get_weather_forecast(city_name):
    # Get City Info API
    if city_name is None:
        raise Exception("City name argment not provided. Aborting...")
    else:
        city_info = get_city_info(request.args.get('city_name'))
        print("***** Fetching weather forecast for", city_name, "*****")
        payload = {'lat': city_info.get("lat"), 'lon': city_info.get("lon"), 'units': 'imperial', 'appid': weather_api_key}    
        response = requests.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params=payload
        )
    # print("RESPONSE: ", response.json())
    return response.json()