# Live-Event-Streaming-Using-Apache-Kafka

🚀 DDoS Detection System using Apache Kafka
📌 Project Overview

This project implements a real-time DDoS attack detection system using Apache Kafka and Python.
It simulates network traffic, detects abnormal high traffic, and generates alerts with a live dashboard.

⚙️ Requirements
Python 3.x
Apache Kafka (running)
Python libraries:
pip install kafka-python pandas matplotlib streamlit
▶️ How to Run (Step-by-Step)
✅ 1. Start Kafka Server

Open CMD:

cd C:\kafka\kafka_2.13-4.2.0
bin\windows\kafka-server-start.bat config\server.properties

👉 Keep this terminal OPEN

✅ 2. Create Kafka Topic

Open new CMD:

cd C:\kafka\kafka_2.13-4.2.0
bin\windows\kafka-topics.bat --create --topic traffic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
✅ 3. Run Producer (Traffic Generator)
python traffic_generator.py

👉 This simulates network traffic

✅ 4. Run Consumer (DDoS Detector)
python ddos_detector.py

👉 Detects DDoS attacks and prints alerts

✅ 5. Run Dashboard
streamlit run dashboard_live.py

👉 Opens browser with live dashboard

📊 Output
Alerts stored in:
alerts.json
Example alert:
{"ip": "192.168.1.5", "attack": "DDoS", "severity": "HIGH"}
⚡ Features
Real-time traffic simulation
DDoS attack detection
Kafka-based streaming pipeline
