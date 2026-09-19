import streamlit as st
import os

from apikey import google_gemini_api_key


st.set_page_config(layout="wide") #set layout to wide

st.title("blogcraft - AI powered blogging platform") #title for web app
st.subheader("Generate blog posts with AI") #subheader for web app

with st.sidebar:
  st.header("Input your blog details below:") #header for sidebar
  st.subheader("Enter your blog title and description") #subheader for sidebar
  blog_title = st.text_input("Blog Title") #text input for blog title
  keyword_ip = st.text_input("Enter your blog keywords (comma separated)") #text input for blog keywords

  number_words = st.slider("select number of words in your blog post", 250, 1000, 250) #slider for number of words in blog post
  img_consent = st.radio("Do you want to generate images for your blog post?", ("Yes", "No")) #radio button for image generation consent
  if img_consent == "Yes":
    img_count = st.slider("How many images do you want in your blog?", 1,5,1) #slider for number of images in blog post
  else:
    img_count = 0
  
  submit_btn = st.button("Generate blog") #button to generate blog post

