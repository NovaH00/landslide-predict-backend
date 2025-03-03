import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_weather_model():
    # Load weather data
    df = pd.read_csv('Flash flood Datas/weatherDatas.csv')
    
    # Split features and target
    X = df.drop('flash_flood_probability', axis=1)
    y = df['flash_flood_probability']
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate model
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    
    print("Weather Model Scores:")
    print(f"Training R² score: {train_score:.4f}")
    print(f"Testing R² score: {test_score:.4f}")
    
    # Save model
    joblib.dump(model, 'ML Models/weather_flood_model.pkl')
    return model

def train_sensor_model():
    # Load sensor data
    df = pd.read_csv('Flash flood Datas/sensorDatas.csv')
    
    # Split features and target
    X = df.drop('flash_flood_probability', axis=1)
    y = df['flash_flood_probability']
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate model
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    
    print("\nSensor Model Scores:")
    print(f"Training R² score: {train_score:.4f}")
    print(f"Testing R² score: {test_score:.4f}")
    
    # Save model
    joblib.dump(model, 'ML Models/sensor_flood_model.pkl')
    return model

if __name__ == "__main__":
    # Create directories if they don't exist
    os.makedirs('Flash flood Model', exist_ok=True)
    os.makedirs('ML Models', exist_ok=True)
    
    # Train both models
    weather_model = train_weather_model()
    sensor_model = train_sensor_model() 