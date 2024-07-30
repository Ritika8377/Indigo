# app.py
from flask import Flask, jsonify
from pymongo import MongoClient
from kafka import KafkaProducer
import json

app = Flask(__name__)

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client.flight_status
flights_collection = db.flights

# Kafka setup
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/api/flights', methods=['GET'])
def get_flights():
    flights = list(flights_collection.find({}, {'_id': 0}))
    return jsonify(flights)

@app.route('/api/notify', methods=['POST'])
def send_notification():
    data = request.get_json()
    producer.send('flight_notifications', data)
    return jsonify({'status': 'Notification sent'})

if __name__ == '__main__':
    app.run(debug=True)
