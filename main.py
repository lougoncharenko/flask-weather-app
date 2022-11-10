import os
import requests

from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file

app = Flask(__name__)


# Get the API key from the '.env' file
load_dotenv()
api_key = os.getenv('API_KEY')

@app.route('/')
def home_page():
    """
    Displays the homepage with forms for weather data.
    """
    context = {
        'min_date': (datetime.now() - timedelta(days=5)),
        'max_date': datetime.now()
    }
    return render_template('home.html', **context)

@app.route('/results')
def weather_results():
    """Displays results for current weather conditions."""
    city = request.args.get('city')
    unit = request.args.get('units')

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={api_key}")



if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)