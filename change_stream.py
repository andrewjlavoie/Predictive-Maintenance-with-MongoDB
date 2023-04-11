import requests
from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB connection
client = MongoClient("uri")
db = client.predictive_maintenance
collection = db.data_records_ts

# Flask API URL
api_url = "http://localhost:5000/predict"

# Watch the MongoDB collection for new documents
with collection.watch([{'$match': {'operationType': 'insert'}}]) as stream:
    for change in stream:
        new_doc = change['fullDocument']

        # Get the temperature value of the new document
        temperature = new_doc['temperature']

        # Call the Flask API with the temperature value
        response = requests.post(api_url, json={"temperature": temperature})
        prediction = response.json()["prediction"]

        # Update the document with the 'probability' field
        collection.update_one({"_id": ObjectId(new_doc["_id"])}, {"$set": {"probability": prediction}})
