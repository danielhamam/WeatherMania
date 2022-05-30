from dotenv import load_dotenv
from os import getenv

# Load environment variables
load_dotenv()

# App Environment Variables
WEATHER_API_KEY = getenv('WEATHER_API_KEY')
DATA_FOLDER = getenv('DATA_FOLDER', '/database')