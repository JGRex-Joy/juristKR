from docx import Document

def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for _ in doc.paragraphs:
        if _.text.strip():
            full_text.append(_.text.strip())
            
    return "\n".join(full_text)