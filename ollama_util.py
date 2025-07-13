import requests as http

# OllamaでAI応答を生成
def ask_ollama(prompt: str, model: str = "qwen3:8b") -> str:
    try:
        response = http.post("http://localhost:11434/api/generate", json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        return response.json()["response"].strip()
    except Exception as e:
        print("Ollamaエラー:", e)
        return "すみません、ちょっと今うまく応答できませんでした。"
