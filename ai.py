import requests
# OllamaでAI応答を生成
#
# NOTE: This function communicates with the Ollama API endpoint at http://localhost:11434 via HTTP.
# While this communication is typically for localhost (loopback) traffic, the data transmitted is unencrypted.
# For environments requiring higher security for this local traffic, consider setting up a
# reverse proxy (e.g., Nginx, Caddy) in front of the Ollama API to enable HTTPS.
def ask_ollama(prompt: str, model: str = "qwen:8b") -> str:
    try:
        # For production robustness, consider adding a timeout to the request,
        # e.g., requests.post(..., timeout=10)
        # While RequestException will catch timeouts, explicit timeout ensures the call doesn't hang indefinitely.
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()  # Raises HTTPError for bad responses (4XX or 5XX)
        data = response.json()
        return data["response"].strip()
    except requests.exceptions.RequestException as e:
        print(f"Ollama API request error (Network/HTTP): {type(e).__name__} - {e}")
        return "すみません、ちょっと今うまく応答できませんでした。"
    except (KeyError, ValueError) as e: # Catches issues with JSON parsing or missing keys
        print(f"Ollama API response processing error (JSON/Key): {type(e).__name__} - {e}")
        return "すみません、ちょっと今うまく応答できませんでした。"
    except Exception as e:
        print(f"Ollama unexpected error: {type(e).__name__} - {e}")
        return "すみません、ちょっと今うまく応答できませんでした。"