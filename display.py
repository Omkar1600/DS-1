import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('Random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define a function to make predictions
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    data = {'N': N, 'P': P, 'K': K, 'temperature': temperature,
            'humidity': humidity, 'ph': ph, 'rainfall': rainfall}
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)[0]
    return prediction

# Create a Streamlit app
st.title("Crop Prediction App")

# Get user inputs
N = st.slider("Ratio of Nitrogen content in soil", 0.0, 100.0, 50.0, 1.0)
P = st.slider("Ratio of Phosphorous content in soil", 0.0, 100.0, 50.0, 1.0)
K = st.slider("Ratio of Potassium content in soil", 0.0, 100.0, 50.0, 1.0)
temperature = st.slider("Temperature in degree Celsius", 0.0, 50.0, 25.0, 0.5)
humidity = st.slider("Relative humidity in %", 0.0, 100.0, 50.0, 1.0)
ph = st.slider("pH value of the soil", 0.0, 14.0, 7.0, 0.1)
rainfall = st.slider("Rainfall in mm", 0.0, 300.0, 150.0, 1.0)

# Make predictions and show the result
if st.button("Predict"):
    prediction = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
    def value(index):
        values=['apple', 'banana' ,'blackgram' ,'chickpea' ,'coconut', 'coffee' ,'cotton','grapes' ,'jute' ,'kidneybeans' ,'lentil', 'maize' ,'mango' ,'mothbeans','mungbean' ,'muskmelon' ,'orange' ,'papaya', 'pigeonpeas', 'pomegranate','rice' ,'watermelon']
        return values[index].upper()
        
    f="The predicted crop is: {}".format(value(prediction))
    st.subheader(f)
    