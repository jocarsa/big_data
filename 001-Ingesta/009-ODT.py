from odf import text, teletype
from odf.opendocument import load
file_path = "documento.odt"
doc = load(file_path)
doc_text = ""
for text_node in doc.getElementsByType(text.P):
    doc_text += teletype.extractText(text_node) + "\n"
print(doc_text)
