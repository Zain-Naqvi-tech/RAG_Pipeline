import requests  # Import the requests library to handle HTTP requests
import json      # Import the json library to parse JSON data


def generate_response(prompt):
    # This function sends a prompt to a local Ollama LLM server and streams back the generated response.

    url = "http://localhost:11434/api/generate"  # The API endpoint for the Ollama LLM server
    payload = {
        "model": "llama2",      # The name of the model to use 
        "prompt": prompt         # The prompt to send to the model
    }

    final_text = ""  # Initialize an empty string to accumulate the streamed response

    # Send a POST request to the Ollama server with the payload, enabling streaming of the response
    with requests.post(url, json=payload, stream=True) as r:
        for line in r.iter_lines():
            if line:  # Only non-empty lines
                data = json.loads(line.decode('utf-8'))  #Parse the JSON data from the line
                if "response" in data:  #check if the 'response' key exists in the data
                    final_text += data["response"]  # Append the response chunk to the final output

    print("Final Output:")
    return final_text  
