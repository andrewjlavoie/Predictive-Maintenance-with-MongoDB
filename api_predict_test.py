'''from pymongo import MongoClient
import requests

# Replace the following with your MongoDB connection string
mongo_conn_str = "mongodb://username:password@localhost:27017/db_name"

client = MongoClient(mongo_conn_str)
db = client["db_name"]
collection = db["collection_name"]'''

# Fetch a single document (replace the query with your specific requirements)
#document = collection.find_one()
import requests

document = {
    'temperature': 240.00,
    'pressure': 1000.00,
    'vibration': 50,
}


# Flask API URL (Replace with your API endpoint)
api_url = "http://localhost:5000/predict"

# Send the features to the Flask API and get the prediction
response = requests.post(api_url, json=document)
prediction = response.json()

print(f"Prediction: {prediction}")
