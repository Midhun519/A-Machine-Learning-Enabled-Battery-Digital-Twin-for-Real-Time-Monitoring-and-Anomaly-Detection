import joblib
import pandas as pd

model = joblib.load("battery_twin.pkl")

test = pd.DataFrame({
    "Temperature":[20],
    "Current":[2.43]
})

predicted_voltage = model.predict(test)

print("Predicted Voltage:", predicted_voltage[0])