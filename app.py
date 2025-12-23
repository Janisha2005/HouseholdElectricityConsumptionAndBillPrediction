import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import joblib

model = joblib.load("rfmodel.pkl")  

def calculate_bill(kwh):
    bill = 0
    slabs = [(100, 5), (100, 6), (300, 7)]
    remaining = kwh
    for limit, rate in slabs:
        use = min(remaining, limit)
        bill += use * rate
        remaining -= use
        if remaining <= 0:
            break
    if remaining > 0:
        bill += remaining * 8
    return bill

st.set_page_config(
    page_title="Electricity Predictor",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-image: url("https://beattiedukelowelectrical.com/wp-content/uploads/2024/02/iStock-1449204162.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

section[data-testid="stSidebar"] {
    background: transparent !important;
}

section[data-testid="stSidebar"] > div {
    background: rgba(0, 0, 0, 0.25) !important;  /* transparent layer */
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-right: 1px solid rgba(255,255,255,0.25);
}

h1, h2, h3 {
    color: #F3F4F6 !important;
}

p, span, label {
    color: #C7CBD1 !important;
}

.prediction-value {
    color: #F5C16C !important;
    font-weight: 700;
    font-size: 2.5rem;
}

button {
    color: #FFFFFF !important;
}
                     
""", unsafe_allow_html=True)

st.title("🏠 Household Electricity Consumption & Bill Predictor")

st.sidebar.header("Input Monthly Features")
global_intensity = st.sidebar.number_input("Average Global Intensity (A)", min_value=0.0, value=18.0)
voltage = st.sidebar.number_input("Average Voltage (V)", min_value=0.0, value=235.0)
reactive_power = st.sidebar.number_input("Average Global Reactive Power (kVAR)", min_value=0.0, value=0.45)
sub1 = st.sidebar.number_input("Sub Metering 1 (Wh)", min_value=0.0, value=500.0)
sub2 = st.sidebar.number_input("Sub Metering 2 (Wh)", min_value=0.0, value=1200.0)
sub3 = st.sidebar.number_input("Sub Metering 3 (Wh)", min_value=0.0, value=1500.0)
month = st.sidebar.selectbox("Month", list(range(1,13)))
year = st.sidebar.number_input("Year", min_value=2006, max_value=2050, value=2025)

input_df = pd.DataFrame([{
    "Global_intensity": global_intensity,
    "Voltage": voltage,
    "Global_reactive_power": reactive_power,
    "Sub_metering_1": sub1,
    "Sub_metering_2": sub2,
    "Sub_metering_3": sub3,
    "month": month,
    "year": year
}])

if st.button("Predict Consumption & Bill"):
    predicted_kwh = model.predict(input_df)[0]
    predicted_bill = calculate_bill(predicted_kwh)

    st.subheader("Predicted Electricity Consumption")
    st.metric("Monthly Consumption (kWh)", f"{predicted_kwh:.2f}")

    st.subheader("Predicted Electricity Bill")
    st.metric("Monthly Bill (₹)", f"{predicted_bill:.2f}")

