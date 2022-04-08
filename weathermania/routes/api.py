from audioop import add
from flask import Blueprint, request, render_template
from config import weather_api_key
from weathermania.helpers import get_city_info, add_forecast, weather_forecasts
import requests

# Set this up as a blueprint. Name of blueprint
bp = Blueprint('api', 'api')
weather_api_url = "http://api.openweathermap.org/data"

# --------------------------------------------------------------------------------------------
# API Name: mock_weather_forecast
# Purpose: Returns JSON representation of what to expect in Weather API
# --------------------------------------------------------------------------------------------
@bp.route("/mock_weather_forecast", methods=['GET']) # tells Flask what URL should trigger the function
def get_mock_weather_forecast():
    # Get City Info API
    payload = {'lat': '35', 'lon': '139', 'units': 'imperial', 'appid': weather_api_key}    
    response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params=payload
    )
    return response.json()

# --------------------------------------------------------------------------------------------
# API Name: get_weather_forecast
# Purpose: Returns a success message indicating the API services are working.
# --------------------------------------------------------------------------------------------
@bp.route("/get_weather_forecast", methods=['GET', 'POST']) # tells Flask what URL should trigger the function
def get_weather_forecast():
    # Get City Info API
    city_name = request.args.get('city_name')
    if city_name is None:
        raise Exception("City name argment not provided. Aborting...")
    else:
        city_info = get_city_info(request.args.get('city_name'))
        payload = {'lat': city_info.get("lat"), 'lon': city_info.get("lon"), 'units': 'imperial', 'appid': weather_api_key}    
        response = requests.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params=payload
        )
    add_forecast(response.json())
    return render_template("app.html", weather_data=response.json(), prev_weather_data_list=weather_forecasts)