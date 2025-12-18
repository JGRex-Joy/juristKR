from rag_service.rag.pipeline import RAGPipeline

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Jurist")

class AskRequest(BaseModel):
    question: str
    
rag_pipeline = RAGPipeline()

@app.post("/ask")
async def ask(request: AskRequest):
    answer = rag_pipeline.run(request.question)
    return {"answer": answer}