import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('models/mpg_predictor.joblib')

st.title('Car Fuel Efficiency Predictor')

st.write('Enter car specifications to predict MPG:')

# Inputs
cylinders = st.slider('Cylinders', 3, 8, 4)
displacement = st.slider('Displacement', 68.0, 455.0, 200.0)
horsepower = st.slider('Horsepower', 46.0, 230.0, 100.0)
weight = st.slider('Weight', 1613.0, 5140.0, 3000.0)
acceleration = st.slider('Acceleration', 8.0, 24.8, 15.0)
model_year = st.slider('Model Year', 70, 82, 76)
origin = st.selectbox('Origin', ['USA', 'Europe', 'Japan'])
power_to_weight = horsepower / weight

# Predict
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

if st.button('Predict MPG'):
    prediction = model.predict(input_data)[0]
    st.write(f'Predicted MPG: {prediction:.2f}')
