import streamlit as st

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")
file = st.file_uploader("Pick a file")
date = st.date_input("Pick Calendar")
st.write(date)

genders = ['Male', 'Female', 'Others']
radio = st.radio("Select your gender", genders)

if name:
  st.write(f" Hello {name} ")
  st.write(f" You uploaded ' ' {file} ")