
import requests

def query_ollama(prompt: str, model: str = "llama3") -> str:
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    if response.ok:
        return response.json().get("response", "").strip()
    return "[ERROR] Ollama response failed"
