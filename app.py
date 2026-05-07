import streamlit as st 

st.title("Streamlit Analysis Dashboard")
st.write("Enter text to analyze sentiment")

user_input = st.text_area("Enter your text")

if st.button("Analyze"):
    st.write ("Analyzing...")
