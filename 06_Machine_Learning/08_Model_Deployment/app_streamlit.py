# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os # Used to check if the pipeline.pkl file exists

# Set the page title and icon
st.set_page_config(page_title="Housing Price Predictor", page_icon="🏠")

# Load the Model
model_path = 'pipeline.pkl'
if not os.path.exists(model_path):
   st.error(f"Error: Model file '{model_path}' not found. Please ensure 'pipeline.pkl' is in the same directory.")
   st.stop() # Stop the app if the model is not found

try:
   # Load the pre-trained pipeline
   with open(model_path, 'rb') as file:
      pipeline = pickle.load(file)
      st.success("Model loaded successfully!")
except Exception as e:
   st.error(f"Error loading model: {e}")
   st.stop() # Stop the app if model loading fails

# Streamlit App Layout
st.title("🏡 California Housing Price Predictor")
st.markdown("""
    Enter the details of the house below to get an estimated median house value.
    This app uses a pre-trained machine learning model.
""")

st.header("House Features")

# Create input fields for each feature
# Using st.columns for better layout
col1, col2 = st.columns(2)

with col1:
    med_inc = st.number_input("Median Income (MedInc)")
    house_age = st.number_input("House Age (HouseAge)")
    ave_rooms = st.number_input("Average Rooms (AveRooms)")
    ave_bedrms = st.number_input("Average Bedrooms (AveBedrms)")

with col2:
    population = st.number_input("Population (Population)")
    ave_occup = st.number_input("Average Occupancy (AveOccup)")
    latitude = st.number_input("Latitude (Latitude)")
    longitude = st.number_input("Longitude (Longitude)")

# Create a DataFrame from the user inputs
# The order of columns must match the training data
input_data = pd.DataFrame([[
    med_inc,
    house_age,
    ave_rooms,
    ave_bedrms,
    population,
    ave_occup,
    latitude,
    longitude
]], columns=[
    'MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
    'Population', 'AveOccup', 'Latitude', 'Longitude'
])

st.subheader("Input Data Summary:")
st.write(input_data)

# Prediction buton
if st.button("Predict House Price"):
    try:
        # Make a prediction using the loaded pipeline
        prediction = pipeline.predict(input_data.values)

        # Display the prediction
        st.success(f"Estimated Median House Value: ${prediction[0]*100000:,.2f}") # Price is in 100K USD
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.warning("Please check your input values and try again.")