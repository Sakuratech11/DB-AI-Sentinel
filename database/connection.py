import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def obtener_conexion():
    try:
        conexion = pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "test"),
            port=int(os.getenv("DB_PORT", "3307")),
            cursorclass=pymysql.cursors.DictCursor # Esto nos regresa los resultados como diccionarios limpios
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None