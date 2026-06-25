import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("battery_dataset_large.csv")

# Input Features
X = df[["Temperature", "Current"]]

# Target
y = df["Voltage"]

model = LinearRegression()

model.fit(X, y)

joblib.dump(model, "battery_twin.pkl")

print("Digital Twin Model Created")