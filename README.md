# Predictive Maintenance with MongoDB

This project demonstrates the use of MongoDB as a backend for storing and managing time series data in a predictive maintenance application. The application predicts equipment failure based on sensor data, such as temperature, pressure, and vibration, and uses machine learning techniques for analysis and prediction. MongoDB provides a scalable and flexible solution for handling time series data and storing trained machine learning models.

## Key Features

- **Data storage**: MongoDB is a highly scalable, high-performance NoSQL database that supports flexible data storage in JSON-like documents. This flexibility allows for easy storage and retrieval of time series data, such as sensor readings, without the need for complex schema changes.
- **Time series collections**: MongoDB provides dedicated support for time series data through time series collections. These collections are optimized for insert-heavy workloads and enable efficient storage, querying, and analysis of time series data.
- **PyMongoArrow**: Pymongoarrow offers several advantages over using $project with the aggregate() function in pymongo when building a DataFrame:

    Performance: pymongoarrow can significantly improve the performance of transferring data from MongoDB to pandas by using the Apache Arrow format. Apache Arrow is a high-performance in-memory data format optimized for analytical processing. It minimizes the need for data serialization and deserialization, allowing for much faster data transfer between MongoDB and pandas.

    Memory efficiency: By using Apache Arrow, pymongoarrow can reduce the memory overhead when working with large datasets. Arrow's columnar memory format enables more efficient memory usage when transferring data between MongoDB and pandas. This can be particularly beneficial when working with large datasets, as it can reduce the overall memory footprint.

    Ease of use: When using $project with the aggregate() function, you need to manually convert the result into a pandas DataFrame. With pymongoarrow, the conversion is handled automatically, which simplifies the process and reduces the likelihood of errors.

    Flexibility: Although $project can be used for simple transformations and filtering, pymongoarrow offers a more flexible and efficient way of transferring data between MongoDB and pandas, especially when working with complex data structures or large datasets.

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
`git clone https://github.com/andrewjlavoie/Predictive-Maintenance-with-MongoDB.git`

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
