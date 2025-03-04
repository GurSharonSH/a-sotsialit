#!/bin/python3
# ollama_client.py

import requests

class OllamaClient:
    def __init__(self):
        self.url = 'http://localhost:11434/'

    def send_prompt(self, prompt, parameters):
        payload = {
            'prompt': prompt,
            'parameters': parameters
        }
        response = requests.post(self.url, json=payload)
        return response.json()
