import mlflow
import mlflow.sklearn

from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# from sklearn.model_selection import train_test_split

# set the MLflow tracking URI
mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("meu_experiment-1")

with mlflow.start_run():
  X,y = make_regression(n_samples=100, n_features=1, noise=0.1)
  model = LinearRegression()
  model.fit(X,y)

  mlflow.log_param("coeficiente", model.coef_[0])
  mlflow.log_metric("score", model.score(X,y))
  mlflow.sklearn.log_model(model, "model")

  print(f"Model saved in MLFlow: {mlflow.get_artifact_uri()}")
