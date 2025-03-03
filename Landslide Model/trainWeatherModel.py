import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the synthetic data
df = pd.read_csv('Datas\weatherDatas.csv')

# Define features and target
X = df[['rain_intensity', 'humidity', 'wind_speed', 'avgtemp_c']]
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
import joblib
joblib.dump(model, r'ML Models/wether_model.pkl')
print("Model saved as 'landslide_model.pkl'")