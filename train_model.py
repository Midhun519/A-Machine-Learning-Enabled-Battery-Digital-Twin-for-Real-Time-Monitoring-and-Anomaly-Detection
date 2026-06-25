import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load dataset
df = pd.read_csv("battery_dataset_large.csv")

# Features only
X = df[["Voltage", "Temperature", "Current"]]

# Train Isolation Forest
model = IsolationForest(
    n_estimators=200,
    contamination=0.09,
    random_state=42
)

model.fit(X)

# Save model
joblib.dump(model, "battery_anomaly_model.pkl")

print("Model trained successfully")
print("Model saved as battery_anomaly_model.pkl")
