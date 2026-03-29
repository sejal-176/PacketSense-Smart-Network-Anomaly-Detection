from sklearn.ensemble import IsolationForest
import pickle
from preprocess import load_and_clean_data, encode_data

# Load data
data = load_and_clean_data("C:\\Users\\HP\\OneDrive\\Desktop\\ml_cybersec\\data\\network_data.csv.csv")

# Encode
data = encode_data(data)

# Select features
features = data[['Source', 'Destination', 'Protocol', 'Length']]

# Train model
model = IsolationForest(contamination=0.05)
model.fit(features)

# Save model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved!")