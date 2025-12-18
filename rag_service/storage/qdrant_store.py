from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

from dotenv import load_dotenv
import uuid

import os
load_dotenv()

from typing import List

class QdrantStore:
    def __init__(self, collection_name="laws_kr", vector_size=768):
        self.client = QdrantClient(
            url=os.getenv("URL"), 
            api_key=os.getenv("API_KEY"),
            timeout=120,
        )
        self.collection_name = collection_name
        self.vector_size = vector_size
        
        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
            )
        
    def recreate(self):
        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(size=self.vector_size, distance=Distance.COSINE)
        )
        
    def add_points(self, vectors: List[float], texts: List[str]):
        points = []
        for (vector, text) in zip(vectors, texts):
            points.append({
                "id": str(uuid.uuid4()),
                "vector": vector,
                "payload": {"text": text}
            })
            
        self.client.upsert(collection_name=self.collection_name, points=points)
        