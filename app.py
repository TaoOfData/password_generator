import streamlit as st
import password_generator as pw

st.title('Random Password Generator')
st.text('This app generates random password for users')
passLen = st.slider('Select length of Password',6,65)
if st.button('Generate'):
    st.write(f'Here is Password generated for you: {pw.generatePassword(passLen)}')
