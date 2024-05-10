#pip install python-docx
from docx import Document
file_path = "documento.docx"
doc = Document(file_path)
doc_text = ""
for paragraph in doc.paragraphs:
    doc_text += paragraph.text + "\n"
print(doc_text)
