import streamlit as st
import joblib
import random
model = joblib.load('your_password')
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2021/03/07/20/45/hack-6077545_1280.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
st.title("Password Maker by Tanmoy Das")
if st.button('Click here to make your password'):
  pass_maker="".join(random.sample(model,8))
  st.write(pass_maker) 
  st.success('Successfully created!', icon="✅")



