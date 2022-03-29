from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set API Key
weather_api_key = os.getenv("WEATHER_API_KEY")