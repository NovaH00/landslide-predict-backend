import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the synthetic sensor data
df = pd.read_csv('Datas\sensorDatas.csv')

# Define features and target
X = df[['piezometer', 'extensometer', 'inclinometer', 'accelerometer', 'rain_gauge']]
y = df['landslide_probability']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Save the model
joblib.dump(model, 'ML Models/sensor_model.pkl')
print("Model saved as 'sensor_model.pkl'")