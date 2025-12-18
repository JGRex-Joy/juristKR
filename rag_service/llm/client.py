from google import genai
from dotenv import load_dotenv
import os

class LLMClient:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("LLM_API_KEY")
        
        if not api_key:
            raise ValueError("LLM_API_KEY is not found")
        
        self.client = genai.Client(api_key=api_key)
        self.model = "gemma-3-27b-it"
        
    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )
        
        return response.text