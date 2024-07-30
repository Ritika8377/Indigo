# consumer.py
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('flight_notifications',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    notification = message.value
    print(f"Notification: {notification}")
