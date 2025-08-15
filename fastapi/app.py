from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow
import pandas as pd
import numpy as np

app = FastAPI()

# Define the input data model using Pydantic
class InputData(BaseModel):
    p_length: float
    p_width: float
    s_length: float
    s_width: float


def get_model():
    model = mlflow.sklearn.load_model(f"bfae199f2c514a0da7a140c938f5d59b/artifacts/model/")
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