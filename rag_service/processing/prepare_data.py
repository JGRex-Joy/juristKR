from rag_service.storage.qdrant_store import QdrantStore
from rag_service.processing.chunker import Chunker
from rag_service.rag.embedder import Embedder
from rag_service.processing.docx_reader import read_docx

def prepare_data(file_path):
    qdrant = QdrantStore()
    chunker = Chunker()
    embedder = Embedder()
    
    print(f"[INFO] Обработка: {file_path}")
    
    full_text = read_docx(file_path)
    
    chunks = chunker.chunk(full_text)
    print(f"[INFO] Чанков: {len(chunks)}")
    
    embeddings = embedder.encode(chunks)
    
    print(f"[INFO] Добавление в Qdrant")
    qdrant.add_points(
        vectors=embeddings,
        texts=chunks,
    )
    
    print(f"[INFO] Файл {file_path} готов")
    
if __name__=="__main__":
    prepare_data("rag_service/data/uk_kr.docx")
    