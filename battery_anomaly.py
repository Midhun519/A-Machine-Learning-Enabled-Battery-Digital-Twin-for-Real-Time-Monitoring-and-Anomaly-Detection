import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("battery_dataset.csv")

X = data[["Voltage", "Temperature", "Current"]]

model = IsolationForest(
    contamination=0.2,
    random_state=42
)

model.fit(X)

data["Result"] = model.predict(X)

print(data)

print("\n1 = Normal")
print("-1 = Anomaly")