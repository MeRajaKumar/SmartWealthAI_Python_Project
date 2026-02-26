import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load dataset
data = pd.read_csv("data/financial_data.csv")

X = data[["income", "expenses", "duration", "risk_level"]]
y = data["future_value"]

model = LinearRegression()
model.fit(X, y)

# Ensure Models folder exists
os.makedirs("Models", exist_ok=True)

# Save model properly
joblib.dump(model, "Models/investment_model.pkl")

print("Model trained and saved successfully.")