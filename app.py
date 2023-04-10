from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the logistic regression model
model = joblib.load('logistic_regression_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the request
    input_data = request.get_json()

    # Extract the temperature, pressure, and vibration values
    temperature = input_data['temperature']
    pressure = input_data['pressure']
    vibration = input_data['vibration']

    # Create an input array for the model
    input_array = np.array([[temperature, pressure, vibration]])

    # Predict the probability of equipment failure
    probability = model.predict_proba(input_array)[:, 1]

    # Return the probability as a JSON response
    response = {"probability": probability[0]}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
