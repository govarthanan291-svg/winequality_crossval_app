import streamlit as st
import numpy as np
import pickle

# Page Config
st.set_page_config(
    page_title="🍷 Wine Quality Prediction App",
    page_icon="🍷",
    layout="centered"
)

# Load Model
with open("wine_quality_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.markdown("<h1 style='text-align:center; color:#8B0000;'>🍷 Wine Quality Prediction</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Input Fields
fixed_acidity = st.number_input("Fixed Acidity", 0.0, 20.0)
volatile_acidity = st.number_input("Volatile Acidity", 0.0, 2.0)
citric_acid = st.number_input("Citric Acid", 0.0, 2.0)
residual_sugar = st.number_input("Residual Sugar", 0.0, 20.0)
chlorides = st.number_input("Chlorides", 0.0, 1.0)
free_sulfur = st.number_input("Free Sulfur Dioxide", 0.0, 100.0)
total_sulfur = st.number_input("Total Sulfur Dioxide", 0.0, 300.0)
density = st.number_input("Density", 0.9, 1.1)
ph = st.number_input("pH", 0.0, 5.0)
sulphates = st.number_input("Sulphates", 0.0, 2.0)
alcohol = st.number_input("Alcohol", 0.0, 20.0)

# Predict Button
if st.button("Predict Wine Quality 🍾"):
    input_data = np.array([[fixed_acidity, volatile_acidity, citric_acid,
                             residual_sugar, chlorides, free_sulfur,
                             total_sulfur, density, ph, sulphates, alcohol]])

    prediction = model.predict(input_data)

    st.success(f"🍷 Predicted Wine Quality: {round(prediction[0],2)}")

