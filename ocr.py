import pytesseract
import cv2

def extraer_texto_de_imagen(ruta_imagen):
    img = cv2.imread(ruta_imagen)
    texto = pytesseract.image_to_string(img)
    return texto
