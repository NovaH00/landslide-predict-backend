from flask import Flask, request, jsonify
import requests
import pandas as pd
import joblib
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

API_KEY = os.getenv('WEATHER_API_KEY')  # Get the API key from environment variable
BASE_URL = 'http://api.weatherapi.com/v1/forecast.json'

# Load the trained models
weather_model = joblib.load(r'ML Models\weather_model.pkl')
sensor_model = joblib.load(r'ML Models\sensor_model.pkl')

@app.route('/weather', methods=['GET'])
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if not lat or not lon:
        return jsonify({'error': 'Please provide both latitude and longitude'}), 400

    params = {
        'key': API_KEY,
        'q': f'{lat},{lon}',
        'days': 7
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), response.status_code

    data = response.json()
    forecast_days = data['forecast']['forecastday']
    
    probabilities = []
    for day in forecast_days:
        for hour in day['hour']:
            if int(hour['time'].split(' ')[1].split(':')[0]) % 3 == 0:
                weather_data = {
                    'rain_intensity': hour.get('precip_mm', 0),
                    'humidity': hour['humidity'],
                    'wind_speed': hour['wind_kph'],
                    'avgtemp_c': hour['temp_c']
                }
                df = pd.DataFrame([weather_data])
                probability = weather_model.predict(df)[0]
                probability = max(0, probability)  # Clamp probability to 0 if less than 0
                probabilities.append({
                    'time': hour['time'],
                    'avgtemp_c': hour['temp_c'],
                    'condition': hour['condition']['text'],
                    'rain_intensity': hour.get('precip_mm', 0),
                    'humidity': hour['humidity'],
                    'wind_speed': hour['wind_kph'],
                    'landslide_probability': probability*100
                })

    return jsonify(probabilities)

@app.route('/sensor', methods=['GET'])
def get_sensor_data():
    piezometer = request.args.get('piezo')
    extensometer = request.args.get('exten')
    inclinometer = request.args.get('incli')
    accelerometer = request.args.get('accel')
    rain_gauge = request.args.get('rain_gauge')
    
    if not all([piezometer, extensometer, inclinometer, accelerometer, rain_gauge]):
        return jsonify({'error': 'Please provide all sensor data: piezometer, extensometer, inclinometer, accelerometer, rain_gauge'}), 400

    sensor_data = {
        'piezometer': [float(piezometer)],
        'extensometer': [float(extensometer)],
        'inclinometer': [float(inclinometer)],
        'accelerometer': [float(accelerometer)],
        'rain_gauge': [float(rain_gauge)]
    }

    df = pd.DataFrame(sensor_data)
    probability = sensor_model.predict(df)[0]
    probability = max(0, probability)  # Clamp probability to 0 if less than 0

    return jsonify({'landslide_probability': probability*100})

if __name__ == '__main__':
    app.run(debug=True)