import serial
import joblib
import pandas as pd
from flask import Flask, render_template
from flask_socketio import SocketIO
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

model = joblib.load("battery_anomaly_model.pkl")

ser = serial.Serial("COM5", 115200, timeout=1)

def battery_health(v, t):
    health = 100

    if v < 3.5:
        health -= (3.5 - v) * 50

    if t > 40:
        health -= (t - 40) * 2

    return max(0, round(health, 2))

@app.route("/")
def home():
    return render_template("index.html")

def stream():
    while True:
        try:
            line = ser.readline().decode(errors="ignore").strip()
            if not line:
                continue

            parts = line.split(",")

            if len(parts) != 4:
                continue

            if not parts[0].strip().isdigit():
                continue

            idx = int(parts[0])
            v = float(parts[1])
            t = float(parts[2])
            c = float(parts[3])

            if t <= 0 or t > 80:
                continue

            pred = model.predict([[v, t, c]])[0]
            status = "NORMAL" if pred == 1 else "ANOMALY"

            socketio.emit("update", {
                "i": idx,
                "v": v,
                "t": t,
                "c": c,
                "s": status,
                "h": battery_health(v, t)
            })

            time.sleep(0.1)

        except Exception as e:
            print(e)

if __name__ == "__main__":
    socketio.start_background_task(stream)
    socketio.run(app, host="0.0.0.0", port=5000, debug=False)
