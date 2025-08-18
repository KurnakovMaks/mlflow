from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import mlflow

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42
)

for n in [10, 40, 60, 80, 100]:
    mlflow.start_run()
    # Create and train a RandomForestClassifier
    clf = RandomForestClassifier(n_estimators=n)
    clf.fit(X_train, y_train)
    # Make predictions
    y_pred = clf.predict(X_test)
    # Log metrics
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)
    # Log parameters
    mlflow.log_params({"n_estimators": n, "random_state": 42})

    # Log the model as an artifact
    mlflow.sklearn.log_model(clf, "model")
    mlflow.end_run()
