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
weather_flood_model = joblib.load(r'ML Models\weather_flood_model.pkl')
sensor_flood_model = joblib.load(r'ML Models\sensor_flood_model.pkl')

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
                landslide_prob = weather_model.predict(df)[0]
                flood_prob = weather_flood_model.predict(df)[0]
                
                # Clamp probabilities to 0 if less than 0
                landslide_prob = max(0, landslide_prob)
                flood_prob = max(0, flood_prob)
                
                probabilities.append({
                    'time': hour['time'],
                    'avgtemp_c': hour['temp_c'],
                    'condition': hour['condition']['text'],
                    'rain_intensity': hour.get('precip_mm', 0),
                    'humidity': hour['humidity'],
                    'wind_speed': hour['wind_kph'],
                    'landslide_probability': landslide_prob*100,
                    'flash_flood_probability': flood_prob*100
                })

    return jsonify(probabilities)

@app.route('/sensor', methods=['GET'])
def get_sensor_data():
    piezometer = request.args.get('piezo')
    water_level = request.args.get('water_level')
    flow_rate = request.args.get('flow_rate')
    extensometer = request.args.get('exten')
    inclinometer = request.args.get('incli')
    accelerometer = request.args.get('accel')
    rain_gauge = request.args.get('rain_gauge')
    
    # Check landslide sensor data
    landslide_sensors = [piezometer, extensometer, inclinometer, accelerometer, rain_gauge]
    if not all(landslide_sensors):
        return jsonify({'error': 'Please provide all landslide sensor data: piezometer, extensometer, inclinometer, accelerometer, rain_gauge'}), 400

    # Check flood sensor data
    flood_sensors = [water_level, flow_rate, rain_gauge]
    if not all(flood_sensors):
        return jsonify({'error': 'Please provide all flood sensor data: water_level, flow_rate, rain_gauge'}), 400

    # Prepare landslide sensor data
    landslide_data = {
        'piezometer': [float(piezometer)],
        'extensometer': [float(extensometer)],
        'inclinometer': [float(inclinometer)],
        'accelerometer': [float(accelerometer)],
        'rain_gauge': [float(rain_gauge)]
    }

    # Prepare flood sensor data with all required features
    flood_data = {
        'piezometer': [float(piezometer)],
        'water_level': [float(water_level)],
        'flow_rate': [float(flow_rate)],
        'extensometer': [float(extensometer)],
        'inclinometer': [float(inclinometer)],
        'accelerometer': [float(accelerometer)],
        'rain_gauge': [float(rain_gauge)]
    }

    # Make predictions
    landslide_df = pd.DataFrame(landslide_data)
    flood_df = pd.DataFrame(flood_data)
    
    landslide_prob = sensor_model.predict(landslide_df)[0]
    flood_prob = sensor_flood_model.predict(flood_df)[0]
    
    # Clamp probabilities to 0 if less than 0
    landslide_prob = max(0, landslide_prob)
    flood_prob = max(0, flood_prob)

    return jsonify({
        'landslide_probability': landslide_prob*100,
        'flash_flood_probability': flood_prob*100
    })

if __name__ == '__main__':
    app.run(debug=True)
    
