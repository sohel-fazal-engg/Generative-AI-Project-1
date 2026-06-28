import pandas as pd
import streamlit as st

name = st.text_input("Enter name : ")

age = st.slider("Enter age : ",18, 100, 25)

choices = ["Amul", "Kwality Walls", "Nandini", "Rollick"]
ice_cream = st.selectbox("Which brand of ice cream do you like ?", choices)

st.title(f"Your name is {name}.\nYour age is {age}.\nYour favourite ice cream brand is {ice_cream}")

uploaded_file = st.file_uploader("Upload a csv file", type = "csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file, type="csv")
    st.write(df)