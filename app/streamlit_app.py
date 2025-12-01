import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------
# Load Model
# ---------------------------------------
model = joblib.load('models/mpg_predictor.joblib')

# ---------------------------------------
# UI Styling
# ---------------------------------------
st.set_page_config(page_title="Car Fuel Efficiency Predictor", layout="centered")

# Custom CSS for clean premium look
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        .stSlider > div > div > div > div {
            background: #ff4b4b !important;
        }
        .block-container {
            padding-top: 3rem;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: 700;
            color: #ffffff;
        }
        .subtitle {
            text-align: center;
            color: #bbbbbb;
            font-size: 18px;
            margin-bottom: 30px;
        }
        .predict-box {
            background-color: #1c1f26;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 22px;
            font-weight: 700;
            color: #00e676;
            border: 1px solid #2c313a;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🚗 Car Fuel Efficiency Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Enter car specifications to estimate fuel efficiency (MPG)</div>", unsafe_allow_html=True)

# ---------------------------------------
# Input UI
# ---------------------------------------

col1, col2 = st.columns(2)

with col1:
    cylinders = st.slider('Cylinders', 3, 8, 4)
    horsepower = st.slider('Horsepower', 46.0, 230.0, 100.0)
    acceleration = st.slider('Acceleration', 8.0, 24.8, 15.0)

with col2:
    displacement = st.slider('Displacement', 68.0, 455.0, 200.0)
    weight = st.slider('Weight', 1613.0, 5140.0, 3000.0)
    model_year = st.slider('Model Year', 70, 82, 76)

origin = st.selectbox('Origin', ['USA', 'Europe', 'Japan'])

# New feature
power_to_weight = horsepower / weight

# ---------------------------------------
# Prediction
# ---------------------------------------
input_data = pd.DataFrame({
    'cylinders': [cylinders],
    'displacement': [displacement],
    'horsepower': [horsepower],
    'weight': [weight],
    'acceleration': [acceleration],
    'model_year': [model_year],
    'origin': [origin],
    'power_to_weight': [power_to_weight]
})

if st.button('🔍 Predict MPG', use_container_width=True):
    prediction = model.predict(input_data)[0]

    st.markdown(
        f"<div class='predict-box'>Predicted MPG: {prediction:.2f}</div>",
        unsafe_allow_html=True
    )
