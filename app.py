from flask import Flask
from weathermania.routes import weathermania, api

# Run instance of the Flask class (serves as WSGI application)
app = Flask(__name__) 

# Lower logging level to debug
# logging.basicConfig(level=logging.DEBUG)

# Register blueprints
app.register_blueprint(weathermania.bp) 
app.register_blueprint(api.bp, url_prefix='/api') 

if __name__ == '__main__':
    app.run(debug=True)