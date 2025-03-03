import pandas as pd
import joblib

# Load the trained model
model = joblib.load(r'ML Models\landslide_model.pkl')

# Define new input data (example data)
new_data = {
    'rain_intensity': [100],  # Replace with actual data
    'humidity': [80],          # Replace with actual data
    'wind_speed': [20],        # Replace with actual data
    'avgtemp_c': [25]          # Replace with actual data
}

def get_probability(datas):
    df = pd.DataFrame(datas)
    
    return model.predict(df)
