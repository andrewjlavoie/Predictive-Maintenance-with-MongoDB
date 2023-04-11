import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from scipy.signal import windows
from pymongo import MongoClient

import time
import pprint

np.random.seed(41)
random.seed(41)

# Replace 'your_connection_string' with your MongoDB connection string
client = MongoClient('uri')
db = client.predictive_maintenance
collection = db.data_records_ts
last_doc = collection.aggregate([
    { '$sort': { 'time': -1 } },
    { '$limit': 1 }
])
for doc in last_doc:
    last_time = doc['time']
print(last_time)


n_samples  = 10080 # about a week
start_time = last_time
time_delta = timedelta(minutes=1)

# Generate time data
timestamps = [start_time + i * time_delta for i in range(n_samples)]

# Generate temperature data
temp_base = np.random.uniform(180, 200, n_samples)
failure_temp_ranges = [(5, 10), (5, 10), (5, 10), (5, 10), (5, 10)]

# Generate pressure and vibration data
pressure_data = np.random.normal(1000, 10, n_samples)
vibration_data = np.random.normal(50, 5, n_samples)

# Generate failure data
failure_data = np.zeros(n_samples, dtype=int)
failure_indices = [500, 3000, 6000]

for index, (low, high) in zip(failure_indices, failure_temp_ranges):
    failure_data[index:index + 100] = 1
    
    # Apply Gaussian window for a smooth transition
    window_size = 200
    window = windows.gaussian(window_size, std=50)
    temp_increase = np.random.uniform(low, high, window_size) * window
    
    start_index = max(index - window_size // 2, 0)
    end_index = start_index + window_size
    temp_base[start_index:end_index] += temp_increase

data = pd.DataFrame({
    'sensor_id': 'sensor01',
    'time': timestamps,
    'temperature': temp_base,
    'pressure': pressure_data,
    'vibration': vibration_data,
    'failure': failure_data
})

print(data.head())
print(data.describe())
print(data.info())


# Convert the DataFrame to a list of dictionaries and insert it into the 'data_records' collection
data_dict = data.to_dict('records')

for doc in data_dict:
    collection.insert_one(doc)
    pprint.pprint(doc)
    time.sleep(2)