from langchain_text_splitters import RecursiveCharacterTextSplitter

class Chunker:
    def __init__(self, chunk_size=600, chunk_overlap=100):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,  
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=[
                "\n### ", 
                "\n## ", 
                "\n# ", 
                "\nСтатья ", 
                "\nГлава ", 
                "\n", 
                " ", 
                ""
            ]
        )
        
    def chunk(self, text: str) -> list[str]:
        return self.splitter.split_text(text)
