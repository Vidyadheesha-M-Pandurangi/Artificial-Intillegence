
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("best_model.pkl")

st.title("💼PayPredictor")
st.write("Enter the following details to predict whether the income is >50K or <=50K")

# Form input

age = st.slider("Age", 18, 90, 30)
workclass = st.selectbox("Workclass", ['Private', 'Self-emp-not-inc', 'Local-gov', 'State-gov', 'Federal-gov', '?'])
education = st.selectbox("Education", ['Bachelors', 'HS-grad', '11th', 'Masters', '9th', 'Some-college', 'Assoc-acdm', 'Assoc-voc', 'Doctorate', '?'])
marital_status = st.selectbox("Marital Status", ['Never-married', 'Married-civ-spouse', 'Divorced', 'Separated', 'Widowed', 'Married-spouse-absent'])
occupation = st.selectbox("Occupation", ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', '?'])
relationship = st.selectbox("Relationship", ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'])
gender = st.radio("Gender", ['Male', 'Female'])
hours_per_week = st.slider("Hours per Week", 1, 100, 40)
native_country = st.selectbox("Native Country", ['United-States', 'India', 'Mexico', 'Philippines', '?'])

# Predict
if st.button("Predict Income Category"):
    input_df = pd.DataFrame([{
        'age': age,
        'workclass': workclass,
        'education': education,
        'marital-status': marital_status,
        'occupation': occupation,
        'relationship': relationship,
        'gender': gender,
        'hours-per-week': hours_per_week,
        'native-country': native_country,

        #Default values
        
        'capital-gain': 0,
        'capital-loss': 0,
        'fnlwgt': 1,
        'educational-num': 10
    }])
    
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Income Category: **{prediction}**")
