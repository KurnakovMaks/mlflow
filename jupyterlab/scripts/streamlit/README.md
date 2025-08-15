# Model Creation with mlflow

FYI, I created a conda environment and ran all my codes in that environment.

The provided Python code leverages the Iris dataset to train a set of Random Forest Classifier models with varying numbers of estimators (10, 40, 60, 80, 100) using MLflow.

This Python script showcases the use of MLflow for the end-to-end deployment of machine learning models. It employs the popular Iris dataset and RandomForestClassifier to create multiple models with different numbers of estimators. The key steps include:

Data Loading and Splitting:
Loads the Iris dataset, separating features (X) and labels (y).
Splits the data into training and testing sets.
Model Training Loop:
Iterates over a predefined list of estimator values (10, 40, 60, 80, 100).
Starts an MLflow run for each iteration.
Creates and trains a RandomForestClassifier with the specified number of estimators.
Makes predictions on the test set.
Logging Metrics and Parameters:
Logs accuracy metrics for each model using MLflow.
Logs model parameters, including the number of estimators and random state.
MLflow Run Finalization:
Ends the MLflow run for each iteration.
http://127.0.0.1:5000/ Will show the mlflow dashboard.

How do we extract the best model?

The above code returns the best model by going through all the models that was run under the experiment id 0.

Now, we will build upon this foundation of best model to deploy the best-performing model using FastAPI, Docker, and Streamlit.