import os
import requests
import json
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

def get_letter_for_units(units):
    """Returns a shorthand letter for the given units."""
    return 'F' if units == 'imperial' else 'C' if units == 'metric' else 'K'


@app.route('/comaprecities')
def compare_cities():
    """
    Displays form for comparing weather data for two cities.
    """
    context = {
        'min_date': (datetime.now() - timedelta(days=5)),
        'max_date': datetime.now()
    }
    return render_template('comparecities.html', **context)

def get_letter_for_units(units):
    """Returns a shorthand letter for the given units."""
    return 'F' if units == 'imperial' else 'C' if units == 'metric' else 'K'


@app.route('/results')
def weather_results():
    """Displays results for current weather conditions."""
    city = request.args.get('city')
    unit = request.args.get('units')
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={api_key}")
    data = response.json()
    date_obj = datetime.now()
    todays_date = date_obj.strftime('%m / %d / %Y')

    context = {
    'date': todays_date,
    'city': data,
    'description': data,
    'temp': data,
    'humidity': data,
    'wind_speed': data,
    "feels_like": data,
    'sunrise': data,
    'sunset': data,
    'units_letter': get_letter_for_units(unit),
    'icon': data
    }

    return render_template('weatherresults.html', **context)

@app.route('/comparison_results')
def comparison_results():
    """Displays the relative weather for 2 different cities."""
    city_1 = request.args.get('city1')
    city_2 = request.args.get('city2')
    units = request.args.get('units')
    city_1_Data = getCityInformation(city_1, units)
    city_2_Data = getCityInformation(city_2, units)
    date_obj = datetime.now()
    todays_date = date_obj.strftime('%m / %d / %Y')

    context = {
    'date': todays_date,
    'city1': city_1_Data,
    'description_city1': city_1_Data,
    'temp_city1': city_1_Data,
    'humidity_city1': city_1_Data,
    'wind_speed_city1': city_1_Data,
    'sunrise_city1': city_1_Data,
    'sunset_city1': city_1_Data,
    'city2': city_2_Data,
    'description_city2': city_2_Data,
    'temp_city2': city_2_Data,
    'humidity_city2': city_2_Data,
    'wind_speed_city2': city_2_Data,
    'sunrise_city2': city_2_Data,
    'sunset_city2': city_2_Data,
    'units_letter': get_letter_for_units(units)
    }
    return render_template('citiesresults.html', **context)

def getCityInformation(city, unit):
    """
    Helper function that makes an API call for each city passed in as a parameter
    """
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={api_key}")
    data = response.json()
    return data

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True, port=3000)