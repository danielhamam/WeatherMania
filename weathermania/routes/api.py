from flask import Blueprint, request
from config import weather_api_key
from weathermania.helpers import get_city_info
import requests

# Set this up as a blueprint. Name of blueprint
bp = Blueprint('api', 'api')
weather_api_url = "http://api.openweathermap.org/data"

# --------------------------------------------------------------------------------------------
# API Name: test
# Purpose: Returns a success message indicating the API services are working.
# --------------------------------------------------------------------------------------------
@bp.route("/get_weather_forecast", methods=['GET']) # tells Flask what URL should trigger the function
def get_weather_forecast():
    # Get City Info API
    city_info = get_city_info(request.args.get('city_name'))
    payload = {'lat': city_info.get("lat"), 'lon': city_info.get("lon"), 'appid': weather_api_key}    
    response = requests.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params=payload
    )
    return response.json()
