from rag_service.llm.client import LLMClient
from rag_service.llm.layers.normalizer import LLMNormalizerLayer
from rag_service.llm.layers.query import LLMQuery

from rag_service.rag.embedder import Embedder

from rag_service.storage.qdrant_search import QdrantSearch


class RAGPipeline:
    def __init__(self):
        self.llm_client = LLMClient()
        self.normalizer = LLMNormalizerLayer(self.llm_client)
        self.query = LLMQuery(self.llm_client)
        self.embedder = Embedder()
        self.searcher = QdrantSearch()
        
    def run(self, user_query: str) -> str:
        normalized_user_query = self.normalizer.normalize(user_query)
        normalized_user_query_vector = self.embedder.encode(normalized_user_query)[0]
        context = self.searcher.search(normalized_user_query_vector)
        answer = self.query.answer(user_query, context)
        
        return answer