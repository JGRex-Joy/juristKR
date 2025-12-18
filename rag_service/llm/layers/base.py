from rag_service.llm.client import LLMClient

class BaseLLMLayer:
    def __init__(self, llm: LLMClient):
        self.llm = llm