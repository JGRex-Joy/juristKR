from sentence_transformers import SentenceTransformer
from typing import List, Union

class Embedder:
    def __init__(self, model_name = 'sergeyzh/LaBSE-ru-sts'):
        self.model = SentenceTransformer(model_name)
        
    def encode(self, texts: Union[str, List[str]]) -> List[float]:
        if isinstance(texts, str):
            texts = [texts]
        embeddings = self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True, show_progress_bar=True)
        return embeddings.tolist()
