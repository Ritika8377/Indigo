# mock_data.py
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.flight_status
flights_collection = db.flights

mock_flights = [
    {'id': 1, 'flightNumber': 'AA123', 'status': 'On Time', 'gate': 'A1'},
    {'id': 2, 'flightNumber': 'BA456', 'status': 'Delayed', 'gate': 'B2'},
    {'id': 3, 'flightNumber': 'CA789', 'status': 'Cancelled', 'gate': 'C3'}
]

flights_collection.insert_many(mock_flights)
