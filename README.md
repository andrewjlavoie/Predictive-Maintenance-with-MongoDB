# Predictive Maintenance with MongoDB

This project demonstrates the use of MongoDB as a backend for storing and managing time series data in a predictive maintenance application. The application predicts equipment failure based on sensor data, such as temperature, pressure, and vibration, and uses machine learning techniques for analysis and prediction. MongoDB provides a scalable and flexible solution for handling time series data and storing trained machine learning models.

## Key Features

- **Data storage**: MongoDB is a highly scalable, high-performance NoSQL database that supports flexible data storage in JSON-like documents. This flexibility allows for easy storage and retrieval of time series data, such as sensor readings, without the need for complex schema changes.
- **Time series collections**: MongoDB provides dedicated support for time series data through time series collections. These collections are optimized for insert-heavy workloads and enable efficient storage, querying, and analysis of time series data.
- **PyMongoArrow**: MongoDB's GridFS feature allows for storage and retrieval of large files, such as trained machine learning models, in a MongoDB database. This enables seamless integration of model storage and deployment within the same database system.

## Project Structure

predictive_maintenance_project/
│
├── api_predict_test.py # Tests sample document against model through Flask API
├── app.py # Flask API code
├── data_generation_1.ipynb # Jupyter Notebook for the data generation
├── start_here.py # Read the data with pymongoarrow, generate a graphic, build an ML model, test prediction
│
└── README.md # Project documentation


## Getting Started

1. Clone this repository:
`git clone https://github.com/yourusername/predictive_maintenance_project.git`

2. Install the required dependencies:
`pip install flask numpy pandas pymongo pymongoarrow pyarrow joblib scikit-learn`

3. Generate the dataset and store it in a MongoDB database:
Open the `data_generation_1.ipynb` and edit the MongoDB DB URI in the bottom cell. Follow the comments.

4. Train and evaluate the machine learning model:
Open the `start_here.ipynb` and follow the comments.

5. Deploy the Flask API:
`python ./app.py`

6. Test API
`python ./api_predict_test.py


## Acknowledgements

- [MongoDB](https://www.mongodb.com/)
- [scikit-learn](https://scikit-learn.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Pandas](https://pandas.pydata.org/)
- [PyMongoArrow](https://pypi.org/project/pymongoarrow/)
