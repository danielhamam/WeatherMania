from flask import Flask
from weathermania import weathermania

# Run instance of the Flask class (serves as WSGI application)
app = Flask(__name__) 

# Register blueprints
app.register_blueprint(weathermania.bp) 

if __name__ == '__main__':
    app.run(debug=True)