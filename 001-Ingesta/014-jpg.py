# pip install pytesseract
import pytesseract
from PIL import Image
image_path = "texto.jpg"
with Image.open(image_path) as img:
    text = pytesseract.image_to_string(img)
print(text)
