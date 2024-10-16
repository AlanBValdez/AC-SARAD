import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    UPLOAD_FOLDER = 'static/uploads'
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'tu_clave_openai')
    DATABASE_URI = 'Driver={SQL Server};Server=tu_servidor;Database=tu_base_de_datos;UID=usuario;PWD=contraseña;'
