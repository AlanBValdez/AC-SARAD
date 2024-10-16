from flask import Flask, render_template, request, redirect
import pytesseract
import cv2
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar_imagen', methods=['POST'])
def procesar_imagen():
    if 'imagen' not in request.files:
        return redirect(request.url)

    file = request.files['imagen']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filepath = os.path.join('static/uploads', 'captura.png')
        file.save(filepath)

        # Procesamiento de imagen con OpenCV
        img = cv2.imread(filepath)
        texto_extraido = pytesseract.image_to_string(img)

        return render_template('index.html', texto_extraido=texto_extraido)

if __name__ == "__main__":
    app.run(debug=True)
