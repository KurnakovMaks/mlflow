import streamlit as st
import requests
import json

# Define the Streamlit app title and description
st.title("Machine Learning Model Deployment")
st.write("Use this app to make predictions with the deployed model.")

# Create input fields for user to enter data
st.header("Input Data")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")
sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")

# Create a button to trigger predictions
if st.button("Predict"):
    # Define the input data as a dictionary
    input_data = {
        "p_length": petal_length,
        "p_width": petal_width,
        "s_length": sepal_length,
        "s_width": sepal_width,
    }

    # Make a POST request to the FastAPI model
    # model_url = "http://0.0.0.0:8000/predict/"
    model_url = "http://fastapi:8000/predict"
    response = requests.post(model_url, json=input_data)

    if response.status_code == 200:
        prediction = json.loads(response.text)["prediction"]
        st.success(f"Model Prediction: {prediction}")
    else:
        st.error("Failed to get a prediction. Please check your input data and try again.")