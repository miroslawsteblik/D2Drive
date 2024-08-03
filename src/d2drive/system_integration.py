import paho.mqtt.client as mqtt
import pandas as pd

class CarSystemIntegration:
    def __init__(self, broker_address, topic):
        self.broker_address = broker_address
        self.topic = topic
        self.client = mqtt.Client()

    def connect(self):
        self.client.connect(self.broker_address)

    def publish_data(self, data):
        self.client.publish(self.topic, data.to_json())

    def disconnect(self):
        self.client.disconnect()

# Example usage:
# csi = CarSystemIntegration(broker_address="localhost", topic="car/data")
# csi.connect()
# data = pd.read_csv('processed_sensor_data.csv')
# csi.publish_data(data)
# csi.disconnect()