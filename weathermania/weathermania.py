from flask import Blueprint, render_template

# Set this up as a blueprint. Name of blueprint
bp = Blueprint('weathermania', __name__, template_folder="templates", static_folder="static", static_url_path='/weathermania/static')

@bp.route("/") # tells Flask what URL should trigger the function
def run_app():
    return render_template('app.html') # default content type is HTML