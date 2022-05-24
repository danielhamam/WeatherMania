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
    response = get_weather_forecast(city_name)
    print("Preparing to add forecast: ", response)
    weather_forecasts.insert(0, response) # inserts forecast (as dictionary)
    print("Successfully added forecast: ", response)
    return render_template("app.html", weather_data=response, prev_weather_data_list=weather_forecasts)

@bp.route("/remove_forecast/<forecast>", methods=['GET', 'POST'])
def remove_forecast(forecast):
    print("Preparing to remove forecast: ", forecast)
    forecast = ast.literal_eval(forecast) # convert str dictionary to python dictionary (interpret python syntax and raise exception if failed)
    for x_forecast in weather_forecasts:
        print("x_forecast is ", type(x_forecast), " and forecast is ", type(forecast))
        if x_forecast.get("id") == forecast.get("id"):
            weather_forecasts.remove(x_forecast)
            print("Successfully removed forecast: ", forecast)
            break
    return render_template("app.html", prev_weather_data_list=weather_forecasts)