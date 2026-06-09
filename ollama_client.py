import requests

OLLAMA_URL = "http://YOUR_SERVER_IP:11434/api/generate"

MODEL = "mistral"

while True:

    prompt = input("\nYou: ")

    if prompt.lower() == "exit":
        break

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()

        result = response.json()

        print("\nAI:", result["response"])

    except Exception as e:
        print("\nError:", e)
