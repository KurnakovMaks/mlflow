import pandas as pd
from pydantic import BaseModel

import mlflow
from fastapi import FastAPI

app = FastAPI()


# Define the input data model using Pydantic
class InputData(BaseModel):
    p_length: float
    p_width: float
    s_length: float
    s_width: float


def get_model(model_id):
    model = mlflow.sklearn.load_model(f"{model_id}/artifacts/model/")
    return model


# create a route
@app.get("/")
def index():
    return {"text": "FastAPI with model"}


# Define a route to accept input data and return predictions
@app.post("/predict")
async def predict(input_data: InputData):
    try:
        # Convert input data to a DataFrame
        input_df = pd.DataFrame([input_data.model_dump()])
        model = get_model()
        # Make predictions using the loaded model
        prediction = model.predict(input_df)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        return {"prediction": str(e)}
