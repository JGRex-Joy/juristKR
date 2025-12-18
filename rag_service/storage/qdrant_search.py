from qdrant_client import QdrantClient, models
from typing import List

from rag_service.storage.qdrant_store import QdrantStore

class QdrantSearch(QdrantStore):
    def __init__(self, collection_name="laws_kr", vector_size=768):
        super().__init__(collection_name=collection_name, vector_size=vector_size)

    def search(self, query_vector: List[float], top_k: int = 5) -> List[str]:
        result = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=top_k,
            with_payload=True,
            search_params=models.SearchParams(hnsw_ef=128)
        )
        
        print(f'[INFO] Found contexts: {[p.payload.get("text", "") for p in result.points]}')
        return [p.payload.get("text", "") for p in result.points]
