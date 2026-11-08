
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Water Potability Prediction",
    page_icon="💧",
    layout="centered"
)

# Load trained model
@st.cache_resource
def load_model():
    
    return joblib.load('water_model.pkl')

model = load_model()

# Application title
st.title("💧 Water Potability Prediction")
st.write("Enter water quality parameters to predict whether water is safe for drinking.")

st.divider()

# Input form
with st.form("water_form"):

    st.subheader("Water Quality Parameters")

    col1, col2 = st.columns(2)

    with col1:
        ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0)
        hardness = st.number_input("Hardness", min_value=0.0, value=150.0)
        solids = st.number_input("Solids", min_value=0.0, value=20000.0)
        chloramines = st.number_input("Chloramines", min_value=0.0, value=7.0)
        sulfate = st.number_input("Sulfate", min_value=0.0, value=300.0)

    with col2:
        conductivity = st.number_input("Conductivity", min_value=0.0, value=400.0)
        organic_carbon = st.number_input("Organic Carbon", min_value=0.0, value=10.0)
        trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=60.0)
        turbidity = st.number_input("Turbidity", min_value=0.0, value=4.0)

    submitted = st.form_submit_button(
        "🔍 Predict Potability",
        use_container_width=True,
       
    )

# Prediction

# Prediction
if submitted:

    if not hasattr(model, "predict"):
        st.error(f"Invalid model object: {type(model)}")
        st.write("PKL contents:", repr(model))
    else:
        new_data = np.array([[
            ph, hardness, solids, chloramines, sulfate,
            conductivity, organic_carbon, trihalomethanes, turbidity
        ]])

        predictions = model.predict(new_data)

        if predictions[0] == 1:
            st.success("Water is Potable.", icon="✅")
        else:
            st.error("Water is Not Potable.", icon="⚠️")
