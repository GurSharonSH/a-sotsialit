#!/bin/python3

# main.py
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
    ollama_client = OllamaClient(api_key='YOUR_API_KEY')

    user_input = input("Enter your sentence: ")

    platforms = ['facebook', 'twitter', 'instagram']
    for platform in platforms:
        config = load_config(platform)
        adapted_text = adapt_text_for_platform(user_input, config)
        response = ollama_client.send_prompt(prompt=adapted_text, parameters=config['additional_parameters'])
        print(f"Adapted text for {platform}: {adapted_text}")
        print(f"Response from Ollama: {response}")

if __name__ == "__main__":
    main()
