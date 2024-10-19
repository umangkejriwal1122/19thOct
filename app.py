import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("placement_model.pkl","rb"))

st.set_page_config(page_title="Student Placement Predictor")

st.header("Student Placement Predictor")

cgpa = st.number_input("Enter CGPA",max_value=10.0,step=0.1)
iq = st.number_input("Enter IQ Score",max_value=200,step=1)
score = st.number_input("Enter Profile Score",max_value=100,step=1)

button = st.button("Predict")

if button:
    input = np.array([cgpa,iq,score]).reshape(1,3)
    result = model.predict(input)[0]
    if result != 0:
        st.success("Placed")
    else:
        st.error("Not Placed")