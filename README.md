

<h1 align="center" style="font-size:30px;">🚀 **NetGuard** <br></h1>
<p align="center">ML-Based Network Anomaly Detection using Wireshark Data</p>
<br><br>

📌**Overview**<br>
This project implements a Machine Learning-based system to detect anomalies in network traffic using real-world packet data captured through Wireshark. It identifies unusual patterns that may indicate potential security threats.
<br><br>

🧠 **Key Features**<br>
* 📡 Capture real network traffic using Wireshark
* 🧹 Data preprocessing & feature selection
* 🤖 Anomaly detection using Isolation Forest
* 🚨 Detect suspicious network behavior
* 📊 Basic visualization of traffic patterns
<br><br>

🏗️ **Project Structure**<br>
```
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
```
<br><br>

⚙️**Tech Stack**<br>
* Python 
* Pandas
* Scikit-learn
* Matplotlib
* Wireshark
<br><br>

▶️ **How to Run**<br>
*  Clone the repository
```
git clone https://github.com/sejal-176/PacketSense-Smart-Network-Anomaly-Detection.git
cd PacketSense-Smart-Network-Anomaly-Detection
```
* Install dependencies
```
pip install -r requirements.txt
```
*  Train the model
```
python src/train.py
```
*  Detect anomalies
```
python src/predict.py
```
<br><br>

📊 **Output** <br>
* Displays total anomalies detected
* Shows suspicious packets
* Helps analyze unusual network behavior
<br><br>

🧠 **Learning Outcomes**<br>
* Network traffic analysis
* Feature engineering for ML
* Unsupervised learning (Isolation Forest)
* Cybersecurity fundamentals
<br><br>


⚠️ **Disclaimer**<br>
This project is for educational purposes only. Detected anomalies do not always indicate malicious activity.
<br><br>


👤 **Author**<br>

Sejal
```
GitHub: https://github.com/sejal-176
```

