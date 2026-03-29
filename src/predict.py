import pickle
from preprocess import load_and_clean_data, encode_data

# Load model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

# Load data
data = load_and_clean_data("data/network_data.csv")
data = encode_data(data)

features = data[['Source', 'Destination', 'Protocol', 'Length']]

# Predict
data['Anomaly'] = model.predict(features)

# Show anomalies
anomalies = data[data['Anomaly'] == -1]

print("🚨 Total anomalies:", len(anomalies))
print(anomalies.head())