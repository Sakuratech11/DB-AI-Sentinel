from fastapi import FastAPI
from database.connection import obtener_conexion
from routers.ai_router import router as ai_router  # <--- Importamos el router de IA

app = FastAPI(
    title="DB-AI-Sentinel",
    description="Sentinel de bases de datos con Inteligencia Artificial",
    version="1.0.0"
)

# Registramos el router en la aplicación principal
app.include_router(ai_router)

@app.get("/")
def ruta_raiz():
    return {"mensaje": "¡Bienvenido a DB-AI-Sentinel! El servidor está en la cancha y listo."}

@app.get("/probar-db")
def probar_db():
    conexion = obtener_conexion()
    if conexion:
        conexion.close()
        return {"estado": "éxito", "detalle": "Conexión a MySQL/MariaDB establecida correctamente desde la estructura limpia."}
    else:
        return {"estado": "error", "detalle": "No se pudo establecer la conexión con la base de datos."}