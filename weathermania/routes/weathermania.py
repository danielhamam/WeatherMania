import ast
from flask import Blueprint, render_template, request
from weathermania.helpers import get_weather_forecast

# Set this up as a blueprint. Name of blueprint
bp = Blueprint('weathermania', __name__, template_folder="../templates", static_folder="../static", static_url_path='/weathermania/static')

# Weather forecasts "Database" Imitation
weather_forecasts = []

@bp.route("/") # tells Flask what URL should trigger the function
def run_app():
    return render_template('app.html', prev_weather_data_list=weather_forecasts)

@bp.route("/add_forecast", methods=['GET', 'POST'])
def add_forecast():
    city_name = request.args.get('city_name')
    print("***** Request received to add forecast for", city_name, " *****")
    # (1) Check if the city name already has a forecast
    already_exists = False
    for x_forecast in weather_forecasts:
        if x_forecast.get("name").lower() == city_name.lower():
            already_exists = True
    # (2) If it doesn't already exist, proceed with addition
    if not already_exists:
        response = get_weather_forecast(city_name)
        weather_forecasts.insert(0, response) # inserts forecast (as dictionary)
        print("***** Successfully added weather forecast for", city_name, "*****")
        return render_template("app.html", weather_data=response, prev_weather_data_list=weather_forecasts, city_exists_error=False)
    print("***** ERROR: Forecast for ", city_name, " already exists! *****")
    return render_template("app.html", prev_weather_data_list=weather_forecasts, city_exists_error=True)

@bp.route("/remove_forecast/<forecast>", methods=['GET', 'POST'])
def remove_forecast(forecast):
    print("***** Request received to remove forecast *****")
    forecast = ast.literal_eval(forecast) # convert str dictionary to python dictionary (interpret python syntax and raise exception if failed)
    for x_forecast in weather_forecasts:
        # print("x_forecast is ", type(x_forecast), " and forecast is ", type(forecast))
        if x_forecast.get("id") == forecast.get("id"):
            weather_forecasts.remove(x_forecast)
            print("***** Successfully removed weather forecast *****")
            break
    return render_template("app.html", prev_weather_data_list=weather_forecasts)
