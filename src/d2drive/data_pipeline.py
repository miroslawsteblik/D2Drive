import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class DataPipeline:
    def __init__(self):
        self.scaler = StandardScaler()

    def load_data(self, file_path):
        # Load sensor data from a CSV file
        data = pd.read_csv(file_path)
        return data

    def preprocess_data(self, data):
        # Handle missing values
        data = data.fillna(method='ffill')

        # Normalize the data
        data_scaled = self.scaler.fit_transform(data)
        return data_scaled

    def save_processed_data(self, data, output_path):
        # Save the processed data to a new CSV file
        pd.DataFrame(data).to_csv(output_path, index=False)