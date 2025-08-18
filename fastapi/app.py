import pandas as pd
from pydantic import BaseModel

import mlflow
from fastapi import FastAPI

app = FastAPI()


class InputData(BaseModel):
    p_length: float
    p_width: float
    s_length: float
    s_width: float


# After finding best_run_id
from mlflow.tracking import MlflowClient


def get_model(model_id):  # FIXED FUNCTION
    model_uri = f"runs:/{model_id}/model"
    return mlflow.sklearn.load_model(model_uri)


def get_best_model(experiment_id, metric_name="accuracy"):
    runs = mlflow.search_runs(experiment_ids=experiment_id)
    best_accuracy = 0
    best_run_id = None
    for index, run in runs.iterrows():
        run_id = run["run_id"]
        run_data = mlflow.get_run(run_id).data
        run_metrics = run_data.metrics
        if metric_name in run_metrics:
            accuracy = run_metrics[metric_name]
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_run_id = run_id
    return best_run_id, best_accuracy


best_run_id, best_accuracy = get_best_model("0")

client = MlflowClient()
if not client.list_artifacts(best_run_id, "model"):
    raise ValueError("Model artifact missing in best run")

model = mlflow.pyfunc.load_model(f"runs:/{best_run_id}/model")

if best_run_id:
    print("Best model found in experiment '0'")
    print(f"Best Run ID: {best_run_id}")
    print(f"Accuracy: {best_accuracy}")
else:
    print("No model with specified metric found")


@app.get("/")
def index():
    return {"text": "FastAPI with model"}


@app.post("/predict")
async def predict(input_data: InputData):
    try:
        input_df = pd.DataFrame([input_data.model_dump()])
        model = get_model(best_run_id)  # Now uses dynamic best_run_id
        prediction = model.predict(input_df)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        return {"error": str(e)}
