from typing import List, Optional
from langchain.embeddings.base import Embeddings
import requests

class OllamaEmbeddings(Embeddings):
    def __init__(self, model: str = "llama2", base_url: str = "http://localhost:11434"):
        self.model = model
        self.base_url = base_url

    def _embed(self, text: str) -> List[float]:
        try:
            response = requests.post(
                f"{self.base_url}/api/embeddings",
                json={
                    "model": self.model,
                    "prompt": text  # 注意：某些模型可能需要调整参数名（如"prompt"或"text"）
                }
            )
            response.raise_for_status()
            return response.json().get("embedding", [])
        except Exception as e:
            raise ValueError(f"Ollama embedding error: {str(e)}")

    def embed_query(self, text: str) -> List[float]:
        return self._embed(text)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self._embed(text) for text in texts]