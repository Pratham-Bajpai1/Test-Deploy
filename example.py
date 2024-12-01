import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_token = os.getenv('HF_HOME_TOKEN')

# Hugging Face Inference API URL
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
headers = {"Authorization": f"Bearer {api_token}"}

st.title("AI Text Generation with Hugging Face")

# Input from user
prompt = st.text_input("Enter your prompt:", "")

if st.button("Generate Text"):
    if prompt:
        with st.spinner("Generating..."):
            data = {"inputs": prompt,
                    "parameters": {
                        "max_length": 100,
                        "temperature": 0.7,
                        "do_sample": True,
                        "stop": ["\n\n", "Human:"]
                    }}

            response = requests.post(API_URL, headers=headers, json=data)

            if response.status_code == 200:
                st.success("Generated Text:")
                st.write(response.json()[0]["generated_text"])
            else:
                st.error(f"Error: {response.status_code}, {response.text}")
    else:
        st.warning("Please enter a prompt!")



