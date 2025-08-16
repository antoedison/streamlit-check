import streamlit as st

# Title
st.title("🚀 My First Streamlit App")

# Input box
name = st.text_input("Enter your name:")

# Button
if st.button("Say Hello"):
    st.success(f"Hello, {name}! Welcome to my Streamlit app 🎉")
