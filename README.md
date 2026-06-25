# Machine Learning Enabled Battery Digital Twin for Real-Time Monitoring and Anomaly Detection

## Overview

This project presents a Machine Learning Enabled Battery Digital Twin for real-time monitoring and anomaly detection of a lithium-ion battery. The system combines embedded hardware, sensor data acquisition, machine learning, and a web-based dashboard to create a virtual representation of a physical battery.

An ESP32 microcontroller continuously collects battery voltage, current, and temperature data from connected sensors. The acquired data is transmitted to a Python-based backend through serial communication, where a trained machine learning model analyzes the battery's operating conditions and identifies abnormal behavior.

The processed information is displayed on a real-time Digital Twin dashboard that mirrors the state of the physical battery. The dashboard provides live monitoring, graphical visualization, and anomaly status updates, enabling users to observe battery performance in real time.

---

## Features

* Real-time voltage monitoring
* Real-time current monitoring
* Real-time temperature monitoring
* Machine learning-based anomaly detection
* Digital Twin dashboard
* Live data visualization
* Real-time battery status monitoring
* Serial communication between ESP32 and Python backend

---

## System Architecture

```text
Lithium-Ion Battery
         │
         ▼
Voltage / Current / Temperature Sensors
         │
         ▼
ESP32 Microcontroller
         │
         ▼
Serial Communication
         │
         ▼
Python Backend
         │
         ▼
Machine Learning Model
         │
         ▼
Digital Twin Dashboard
```

---

## Hardware Components

| Component               | Purpose                            |
| ----------------------- | ---------------------------------- |
| ESP32 Development Board | Data acquisition and communication |
| Lithium-Ion Battery     | Battery under monitoring           |
| Voltage Sensor          | Voltage measurement                |
| Current Sensor          | Current measurement                |
| Temperature Sensor      | Temperature measurement            |

---

## Software Stack

### Embedded System

* ESP32
* Arduino IDE

### Backend

* Python
* Flask
* Flask-SocketIO

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

---

## Machine Learning Workflow

1. Collect battery sensor data.
2. Create a battery dataset.
3. Train a machine learning anomaly detection model.
4. Save the trained model.
5. Load the model in the backend.
6. Analyze incoming sensor data.
7. Classify battery behavior as Normal or Anomalous.

---

## Digital Twin Workflow

The Digital Twin continuously mirrors the real-time condition of the physical battery using live sensor measurements. The dashboard provides:

* Live voltage display
* Live current display
* Live temperature display
* Real-time graphs
* Battery status monitoring
* Anomaly detection results

---

## Project Structure

```text
Battery_Digital_Twin/
│
├── app.py
├── battery_anomaly_model.pkl
├── train_model.py
├── test_model.py
├── batterydataset.csv
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│
└── images/
    ├── dashboard.png
    ├── hardware_setup.jpg
    └── architecture.png
```

---

## Results

The developed system successfully:

* Acquires real-time battery voltage, current, and temperature data
* Creates a synchronized Digital Twin representation
* Detects anomalous operating conditions using machine learning
* Displays live battery information through a web dashboard
* Integrates embedded systems, machine learning, and digital twin technologies into a single platform

---

## Screenshots

### Hardware Setup
<img width="1316" height="1029" alt="WhatsApp Image 2026-06-25 at 9 29 28 PM" src="https://github.com/user-attachments/assets/dac999f1-f2e1-47eb-a24a-59218546db14" />

### Digital Twin Dashboard
<img width="1600" height="794" alt="WhatsApp Image 2026-06-25 at 10 32 22 PM" src="https://github.com/user-attachments/assets/d58effa3-172a-418b-bbcc-ce6038e71359" />

<img width="1600" height="768" alt="WhatsApp Image 2026-06-25 at 10 33 15 PM" src="https://github.com/user-attachments/assets/2f3b0598-7c99-4936-bd6f-d54cb2439318" />


### System Architecture
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/db197d92-859d-48d4-a35e-77043fc9a506" />

---

## Future Enhancements

* Improved anomaly detection using larger datasets
* Enhanced battery behavior modeling
* Historical data logging and analytics
* Additional battery diagnostic capabilities

---

## Conclusion

This project demonstrates the implementation of a Machine Learning Enabled Battery Digital Twin capable of real-time monitoring and anomaly detection. By integrating ESP32-based sensing, machine learning analysis, and a live web dashboard, the system provides an effective platform for intelligent battery monitoring and visualization.
