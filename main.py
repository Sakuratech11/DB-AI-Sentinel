from fastapi import FastAPI
from routers.sentinel_router import router as sentinel_router

app = FastAPI(
    title="DB-AI-Sentinel",
    description="Sentinel de bases de datos con Inteligencia Artificial",
    version="1.0.0"
)

# Incluimos nuestro router modular
app.include_router(sentinel_router)

@app.get("/")
def ruta_raiz():
    return {"mensaje": "¡Bienvenido a DB-AI-Sentinel! El servidor modular está en la cancha."}