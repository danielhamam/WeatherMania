from flask import Blueprint, render_template
from weathermania.helpers import weather_forecasts

# Set this up as a blueprint. Name of blueprint
bp = Blueprint('weathermania', __name__, template_folder="../templates", static_folder="../static", static_url_path='/weathermania/static')

@bp.route("/") # tells Flask what URL should trigger the function
def run_app():
    return render_template('app.html', prev_weather_data_list=weather_forecasts)