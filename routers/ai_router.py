from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.ai_service import consultar_sentinel

# Creamos el router con un prefijo y una etiqueta para la documentación automática (Swagger)
router = APIRouter(
    prefix="/ai",
    tags=["Inteligencia Artificial - Sentinel"]
)

# Definimos el esquema de entrada con Pydantic (Validación de datos profesional)
class ConsultaRequest(BaseModel):
    prompt: str

@router.post("/consultar")
def hacer_consulta_ia(datos: ConsultaRequest):
    if not datos.prompt.strip():
        raise HTTPException(status_code=400, detail="El prompt no puede ir vacío, capitán.")
    
    # Invocamos el servicio que aislamos previamente
    respuesta_ia = consultar_sentinel(datos.prompt)
    
    return {
        "estado": "éxito",
        "prompt_enviado": datos.prompt,
        "respuesta_sentinel": respuesta_ia
    }