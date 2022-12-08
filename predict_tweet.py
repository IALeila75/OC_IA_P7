# Let's upload all relevant libraries
import streamlit as st
import json
import requests

# Web App Title
st.title("Predict Sentiment Tweets")
st.header('This app is created to predict if a tweet is positive or negative')

# Declare a form to receive a tweet
form = st.form(key="my_form")
tweet = form.text_input(label="Enter the tweet")
submit = form.form_submit_button(label="Make Prediction Tweet")
if submit:   
   url = 'https://p7apiflask.azurewebsites.net/predict_sentiment'
   request_data = {'text': tweet}
   r = requests.post(url, params=request_data)
   st.write(r.json())
    