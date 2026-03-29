import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_clean_data(path):
    data = pd.read_csv(path)

    # Keep only useful columns
    data = data[['Time', 'Source', 'Destination', 'Protocol', 'Length']]

    # Remove missing values
    data = data.dropna()

    return data


def encode_data(data):
    le = LabelEncoder()

    data['Source'] = le.fit_transform(data['Source'])
    data['Destination'] = le.fit_transform(data['Destination'])
    data['Protocol'] = le.fit_transform(data['Protocol'])

    return data