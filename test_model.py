import joblib
import pandas as pd

model = joblib.load("battery_anomaly_model.pkl")

# Test samples
test_data = pd.DataFrame({
    "Voltage":[3.95, 3.00, 4.20],
    "Temperature":[20, 65, 70],
    "Current":[2.43, 3.10, 2.00]
})

predictions = model.predict(test_data)

for i in range(len(test_data)):
    print("\nSample", i+1)
    print(test_data.iloc[i])

    if predictions[i] == 1:
        print("Status: NORMAL")
    else:
        print("Status: ANOMALY")