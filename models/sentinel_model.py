from pydantic import BaseModel
from typing import Optional, Dict, Any

class ConsultaRequest(BaseModel):
    query: str
    descripcion: Optional[str] = None

class RespuestaSentinel(BaseModel):
    estado: str
    mensaje: str
    datos: Optional[Dict[str, Any]] = None