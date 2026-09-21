import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

try:
    conexion = pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", ""),
        port=int(os.getenv("DB_PORT", 3307))
    )
    print("¡Conexión exitosa a MariaDB, la jugada entró directo al área!")
    conexion.close()
except Exception as e:
    print(f"Error al conectar con MariaDB: {e}")