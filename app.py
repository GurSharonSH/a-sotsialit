#!/bin/python3

# streamlit_app.py
import streamlit as st
import json
from ollama_client import OllamaClient

# Load configurations
def load_config(platform):
    with open(f'configs/config_{platform}.json', 'r') as file:
        return json.load(file)

def adapt_text_for_platform(text, config):
    # Implement your text adaptation logic here
    adapted_text = text[:config['post_length']]
    if 'hashtags' in config:
        adapted_text += ' ' + ' '.join(config['hashtags'])
    if 'mentions' in config:
        adapted_text += ' ' + ' '.join(config['mentions'])
    return adapted_text

def main():
    st.title("Social Media Adapter")
    st.header("Send and Adapt Text for Different Platforms")

    user_input = st.text_area("Enter your sentence:", height=200)
    if st.button("Send"):
        ollama_client = OllamaClient()
        
        platforms = ['facebook', 'twitter', 'instagram']
        for platform in platforms:
            config = load_config(platform)
            adapted_text = adapt_text_for_platform(user_input, config)
            response = ollama_client.send_prompt(prompt=adapted_text, parameters=config['additional_parameters'])
            
            st.subheader(f"Adapted text for {platform.capitalize()}:")
            st.write(adapted_text)
            st.subheader(f"Response from Llama:")
            st.write(response)

if __name__ == "__main__":
    main()
