import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyAzGTp64xUh-dEvUpUPsdvOyrGQWtmqZX0")

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text, image_data, prompt):
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("Please upload a file")

st.set_page_config(page_title="Invoice Generator")
st.sidebar.header("RoboBill")
st.sidebar.write("Made by Rogini")
st.sidebar.write("Powered by Google Gemini")
st.header("RoboBill")
st.subheader("Made by Rogini")
st.subheader("Manage you expenses with RoboBill")
input = st.text_input("What do you want me to do?",key = "input")
uploaded_file = st.file_uploader("Choose an image from Gallery",type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

ssubmit = st.button("Let's Go!")

input_prompt = """
You are an expert in reading invoices. We are going to upload a person's bill and you will have to answer any type of questions that the user asks you to.
You need to greet the user first. Make sure to keep the fonts uniform and give the items
list in a point-wise format.
At the end, make sure to repeat the name of our app "RoboBill" and ask the user to use it again.
"""

if ssubmit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("Here's what you need to know!")
    st.write(response)
