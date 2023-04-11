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
