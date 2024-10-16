import pyodbc
from config import Config

def conectar_bd():
    conn = pyodbc.connect(Config.DATABASE_URI)
    return conn

def guardar_resultado(texto):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO resultados (texto) VALUES (?)", texto)
    conn.commit()
    conn.close()
