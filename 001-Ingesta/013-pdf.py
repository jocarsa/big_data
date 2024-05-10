# pip install PyPDF2
import PyPDF2
file_path = "documento.pdf"
with open(file_path, "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)   
    pdf_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_text += page.extract_text()
print(pdf_text)
