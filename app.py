import streamlit as st
import numpy as np
import pickle

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="Wine Quality Predictor",
    page_icon="🍷",
    layout="centered"
)

# -----------------------
# LOAD MODEL
# -----------------------
try:
    with open("wine_quality_model.pkl", "rb") as file:
        model = pickle.load(file)
except:
    st.error("❌ wine_quality_model.pkl file not found in folder!")
    st.stop()

# -----------------------
# CUSTOM CSS
# -----------------------
st.markdown("""
<style>
.stApp {
    background-color: #b0b528;
}

.main {
    background-color: white;
    padding: 30px;
    border-radius: 15px;
}

h1 {
    color: darkred;
    text-align: center;
}

label {
    font-weight: bold;
}

.stButton>button {
    background-color: red;
    color: white;
    height: 50px;
    width: 100%;
    font-size: 18px;
    border-radius: 10px;
}

.stButton>button:hover {
    background-color: darkred;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# TITLE
# -----------------------
st.markdown("<h1>🍷 Wine Quality Prediction App</h1>", unsafe_allow_html=True)
st.write("Enter chemical properties of wine:")

# -----------------------
# INPUTS
# -----------------------
col1, col2 = st.columns(2)

with col1:
    fixed_acidity = st.number_input("Fixed Acidity", 0.0, 20.0)
    citric_acid = st.number_input("Citric Acid", 0.0, 2.0)
    chlorides = st.number_input("Chlorides", 0.0, 1.0)
    total_sulfur = st.number_input("Total Sulfur Dioxide", 0.0, 300.0)
    sulphates = st.number_input("Sulphates", 0.0, 2.0)
    alcohol = st.number_input("Alcohol", 0.0, 20.0)

with col2:
    volatile_acidity = st.number_input("Volatile Acidity", 0.0, 2.0)
    residual_sugar = st.number_input("Residual Sugar", 0.0, 20.0)
    free_sulfur = st.number_input("Free Sulfur Dioxide", 0.0, 100.0)
    density = st.number_input("Density", 0.9, 1.1)
    ph = st.number_input("pH", 0.0, 5.0)

# -----------------------
# PREDICT BUTTON
# -----------------------
if st.button("Predict Wine Quality 🍾"):
    input_data = np.array([[fixed_acidity, volatile_acidity, citric_acid,
                             residual_sugar, chlorides, free_sulfur,
                             total_sulfur, density, ph, sulphates, alcohol]])

    prediction = model.predict(input_data)

    st.success(f"🎉 Predicted Wine Quality: {round(prediction[0],2)} / 10")

# -----------------------
# FOOTER
# -----------------------
st.markdown("<hr>")
st.markdown("<center>Developed by Govarthanan</center>", unsafe_allow_html=True)
