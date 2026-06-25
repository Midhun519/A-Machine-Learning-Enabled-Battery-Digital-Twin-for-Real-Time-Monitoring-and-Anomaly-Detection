import serial
import pandas as pd
import joblib

model = joblib.load("battery_anomaly_model.pkl")

ser = serial.Serial("COM5", 115200)

print("Live Battery Monitoring Started...\n")

def clean_temp(temp):
    # filter unrealistic values
    if temp <= 5 or temp > 80:
        return None
    return temp

while True:
    try:
        line = ser.readline().decode(errors='ignore').strip()
        if not line:
            continue

        parts = line.split(',')
        if len(parts) != 4:
            continue

        idx = int(parts[0])
        voltage = float(parts[1])
        temp = float(parts[2])
        current = float(parts[3])

        temp = clean_temp(temp)
        if temp is None:
            # skip bad sensor reading
            continue

        X = pd.DataFrame([[voltage, temp, current]],
                         columns=["Voltage", "Temperature", "Current"])

        pred = model.predict(X)[0]

        status = "NORMAL" if pred == 1 else "ANOMALY"

        print(f"{idx} | V={voltage:.3f} | T={temp:.2f} | I={current:.3f} → {status}")

    except Exception as e:
        print("Error:", e)