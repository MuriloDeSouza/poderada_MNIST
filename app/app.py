# app.py
from flask import Flask, render_template, request, redirect
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, request, render_template, jsonify
import time

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
model = load_model('modelo_top.h5')
model1 = load_model('linear_modelo_mnist.h5')

@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    file.save("file.jpg")
    if file.filename == '':
        return 'No selected file'
    if file:
        img = image.load_img("file.jpg", target_size=(28, 28), color_mode="grayscale")
        img_array = image.img_to_array(img)
        img_array = img_array / img_array.max()
        img_array = img_array.reshape(1,28,28,1)
        prediction = model.predict(img_array, verbose=0)
        digit = np.argmax(prediction)
        digit1 = np.argmax(prediction)
        return render_template('upload.html', digit=digit, digit1=digit1)

if __name__ == "__main__":
    app.run(debug=True)
