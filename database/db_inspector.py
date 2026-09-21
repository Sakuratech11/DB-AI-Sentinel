import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def obtener_esquema_db():
    try:
        conexion = pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", ""),
            port=int(os.getenv("DB_PORT", 3307))
        )
        
        with conexion.cursor() as cursor:
            # Consultamos las tablas de la base de datos actual
            cursor.execute("SHOW TABLES;")
            tablas = cursor.fetchall()
            
            esquema = "Tablas encontradas en la base de datos:\n"
            for tabla in tablas:
                nombre_tabla = tabla[0]
                esquema += f"- {nombre_tabla}\n"
                
                # Opcional: podemos extraer las columnas de cada tabla
                cursor.execute(f"DESCRIBE `{nombre_tabla}`;")
                columnas = cursor.fetchall()
                for col in columnas:
                    esquema += f"    * Columna: {col[0]} ({col[1])}\n"
                    
        conexion.close()
        return esquema
    except Exception as e:
        return f"Error al inspeccionar la base de datos: {e}"