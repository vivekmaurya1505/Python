from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image = Image.open(r'C:\Users\ankitaPC\Desktop\2.png', mode='r')
text = tess.image_to_string(image)
print(text)

import pyttsx3
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
