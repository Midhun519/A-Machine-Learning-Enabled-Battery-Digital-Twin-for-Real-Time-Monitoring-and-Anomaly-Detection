import pandas as pd
import joblib

# Load trained model
model = joblib.load("battery_anomaly_model.pkl")

print("=== TESTING MODEL ===")

# Normal battery condition
normal = pd.DataFrame(
    [[3.98, 25.0, 2.43]],
    columns=["Voltage", "Temperature", "Current"]
)

pred = model.predict(normal)

print("\nTest 1")
print("Voltage=3.98V Temp=25C Current=2.43")

if pred[0] == 1:
    print("NORMAL")
else:
    print("ANOMALY")

# Abnormal battery condition
anomaly = pd.DataFrame(
    [[3.00, 65.0, 3.10]],
    columns=["Voltage", "Temperature", "Current"]
)

pred = model.predict(anomaly)

print("\nTest 2")
print("Voltage=3.00V Temp=65C Current=3.10")

if pred[0] == 1:
    print("NORMAL")
else:
    print("ANOMALY")

# Another abnormal condition
anomaly2 = pd.DataFrame(
    [[4.30, 70.0, 2.00]],
    columns=["Voltage", "Temperature", "Current"]
)

pred = model.predict(anomaly2)

print("\nTest 3")
print("Voltage=4.30V Temp=70C Current=2.00")

if pred[0] == 1:
    print("NORMAL")
else:
    print("ANOMALY")