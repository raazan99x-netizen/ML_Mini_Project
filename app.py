import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="House Price Predictor", layout="wide")

# Load trained model
model = joblib.load("models/house_price_model.pkl")

# Title
st.title("🏠 House Price Prediction App")
st.markdown("Fill in the house details from the sidebar and click **Predict Price**.")

# ---------------- SIDEBAR INPUTS ---------------- #

st.sidebar.header("Enter House Details")


Basement_Size = st.sidebar.number_input(
    "Basement Size", 
    min_value=500, 
    max_value=10000, 
    step=50
)

Built_Year = st.sidebar.slider(
    "Built Year", 
    min_value=1900, 
    max_value=2020
) 

# built_year = st.sidebar.slider("Built Year", 1900, 2025, 2000)

Renovation_Year = st.sidebar.slider(
    "Renovation Year",
    Built_Year,   # minimum built year
    2025,
    Built_Year
)

Land_Size = st.sidebar.number_input("Land Size", 500, 100000, 2000)


input_data = {
    "Basement_Size": Basement_Size,
    "Built Year": Built_Year,
    "Renovation Year": Renovation_Year,
    "Land Size": Land_Size
}
input_df = pd.DataFrame([input_data])

# ---------------- PREDICTION ---------------- #

if st.sidebar.button("Predict Price"):

    input_data = {
    "Basement_Size": Basement_Size,
    "Built_Year": Built_Year,
    "Renovation_Year": Renovation_Year,
    "Land_Size": Land_Size
    }
    input_df = pd.DataFrame([input_data])

    feature_order = joblib.load("models/feature_order.pkl")
    input_df = input_df[feature_order]

    print("Input DF Columns:", input_df.columns)
    print("Feature Order:", feature_order)

    

    prediction = model.predict(input_df)

    predicted_price = prediction[0]

    st.success(f"💰 Predicted House Price: ₹ {predicted_price:,.2f}")

    # Optional: Price category
    if predicted_price < 3000000:
        st.info("🏘 Category: Affordable")
    elif predicted_price < 7000000:
        st.info("🏠 Category: Mid Range")
    else:
        st.info("🏡 Category: Luxury")