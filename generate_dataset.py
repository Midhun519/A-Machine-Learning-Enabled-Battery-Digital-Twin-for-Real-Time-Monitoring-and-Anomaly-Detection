import pandas as pd
import numpy as np

np.random.seed(42)

# Normal data
normal_voltage = np.random.normal(3.95, 0.03, 5000)
normal_temp = np.random.normal(20, 2, 5000)
normal_current = np.random.normal(2.43, 0.01, 5000)

normal = pd.DataFrame({
    "Voltage": normal_voltage,
    "Temperature": normal_temp,
    "Current": normal_current,
    "Label": "Normal"
})

# Anomaly data
anomaly_voltage = np.random.uniform(2.5, 4.5, 500)
anomaly_temp = np.random.uniform(45, 80, 500)
anomaly_current = np.random.uniform(2.0, 3.5, 500)

anomaly = pd.DataFrame({
    "Voltage": anomaly_voltage,
    "Temperature": anomaly_temp,
    "Current": anomaly_current,
    "Label": "Anomaly"
})

dataset = pd.concat([normal, anomaly])

dataset.to_csv("battery_dataset_large.csv", index=False)

print("Dataset Created")
print(dataset.shape)