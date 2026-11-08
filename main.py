
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Water Quality Prediction",
    page_icon="💧",
    layout="centered"
)

st.title("💧 Water Quality Prediction")
st.write("Enter the water quality parameters below.")

with st.form("water_quality_form"):

    col1, col2 = st.columns(2)

    with col1:
        ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
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
        "Submit",
        use_container_width=True
    )

if submitted:

    input_data = {
        "ph": ph,
        "Hardness": hardness,
        "Solids": solids,
        "Chloramines": chloramines,
        "Sulfate": sulfate,
        "Conductivity": conductivity,
        "Organic_carbon": organic_carbon,
        "Trihalomethanes": trihalomethanes,
        "Turbidity": turbidity
    }

    st.success("Form submitted successfully!")

    st.subheader("Entered Water Quality Data")

    df = pd.DataFrame([input_data])
    st.dataframe(df, use_container_width=True)
