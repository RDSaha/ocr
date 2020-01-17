
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from datetime import datetime as dt
import numpy as np
import uuid
import os
import PIL
from PIL import Image
from pytesseract import image_to_string
import pytesseract
import tempfile
import imageio

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'





def  ocr(image):
	output = pytesseract.image_to_string(PIL.Image.open(image).convert("RGB"), lang='eng')
	return output


#Download VGG16 Weights.
#wget https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg16_weights_tf_dim_ordering_tf_kernels.h5


"""Instantiating the flask object"""
app = Flask(__name__)
CORS(app)

@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/index.html')
def index_from_checkup():
    return render_template('index.html')


@app.route("/", methods = ["POST", "GET"])
def index():
  if request.method == "POST":
    type_ = request.form.get("type", None)
    data = None
    final_json = []
    if 'img' in request.files:
      file_ = request.files['img']
      name = os.path.join(tempfile.gettempdir(), str(uuid.uuid4().hex[:10]))
      file_.save(name)
      print("[DEBUG: %s]"%dt.now(),name)

      data = ocr(file_)
      final_json.append({"opt": data}) 

    
    return jsonify(final_json)
  return jsonify({"empty":True})


if __name__=="__main__":
  app.run("0.0.0.0",80, debug = False)