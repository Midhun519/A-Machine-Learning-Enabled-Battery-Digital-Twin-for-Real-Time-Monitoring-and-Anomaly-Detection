import joblib
import pandas as pd

# Load twin
twin = joblib.load("battery_twin.pkl")

# Example real sensor reading
actual_voltage = 3.92
temperature = 20.0
current = 2.43

data = pd.DataFrame({
    "Temperature":[temperature],
    "Current":[current]
})

predicted_voltage = twin.predict(data)[0]

error = abs(actual_voltage - predicted_voltage)

print("===== DIGITAL TWIN =====")
print(f"Actual Voltage    : {actual_voltage:.3f} V")
print(f"Predicted Voltage : {predicted_voltage:.3f} V")
print(f"Error             : {error:.3f} V")

if error < 0.10:
    print("Status: NORMAL")
else:
    print("Status: WARNING")