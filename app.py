from PIL import Image
import PIL.Image

from pytesseract import image_to_string
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'
output = pytesseract.image_to_string(PIL.Image.open('image_hand.jpeg').convert("RGB"), lang='eng')
output = np.array(output)

var = PIL.
