

#🚀 NetGuard: ML-Based Network Anomaly Detection using Wireshark Data

##📌**Overview**
This project implements a Machine Learning-based system to detect anomalies in network traffic using real-world packet data captured through Wireshark. It identifies unusual patterns that may indicate potential security threats.

##🧠 **Key Features**
* 📡 Capture real network traffic using Wireshark
* 🧹 Data preprocessing & feature selection
* 🤖 Anomaly detection using Isolation Forest
* 🚨 Detect suspicious network behavior
* 📊 Basic visualization of traffic patterns

##🏗️ **Project Structure**
network-anomaly-ml/
│
├── data/
│   └── network_data.csv
│
├── model/
│   └── model.pkl
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│
├── app/ (optional)
│   └── app.py
│
├── requirements.txt
└── README.md

##⚙️ **Tech Stack**
* Python 🐍
* Pandas
* Scikit-learn
* Matplotlib
* Wireshark

##▶️ **How to Run**
* 1. Clone the repository
git clone https://github.com/sejal-176/PacketSense-Smart-Network-Anomaly-Detection.git
cd PacketSense-Smart-Network-Anomaly-Detection
* 2. Install dependencies
pip install -r requirements.txt
* 3. Train the model
python src/train.py
* 4. Detect anomalies
python src/predict.py

##📊 **Output**
* Displays total anomalies detected
* Shows suspicious packets
* Helps analyze unusual network behavior

##🧠 **Learning Outcomes**
* Network traffic analysis
* Feature engineering for ML
* Unsupervised learning (Isolation Forest)
* Cybersecurity fundamentals

##⚠️ **Disclaimer**
This project is for educational purposes only. Detected anomalies do not always indicate malicious activity.

##👤 **Author**
Sejal
GitHub: https://github.com/sejal-176
