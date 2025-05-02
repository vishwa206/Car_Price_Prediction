import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the trained model (ensure 'LinearRegressionModel.pkl' is available in the environment)
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

def predict_car_price(features):
    return model.predict([features])

# Streamlit UI
st.title("Car Price Prediction")
st.write("Enter the details of the car to predict its price")

# Collect user input data
age = st.number_input("Age of the Car (in years)", min_value=0)
km_driven = st.number_input("Kilometers Driven", min_value=0)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner", ["First", "Second", "Third", "Fourth"])

if st.button("Predict Price"):
    # Convert categorical inputs to numerical values
    fuel_type_value = 0 if fuel_type == "Petrol" else 1 if fuel_type == "Diesel" else 2
    transmission_value = 0 if transmission == "Manual" else 1
    owner_value = {"First": 0, "Second": 1, "Third": 2, "Fourth": 3}[owner]

    # Features to be passed to the model
    features = [age, km_driven, fuel_type_value, transmission_value, owner_value]

    # Predict and display the car price
    price = predict_car_price(features)
    st.write(f"Predicted Car Price: ₹ {price[0]:,.2f}")
