import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="DB-AI-Sentinel",
    version="1.0.0",
    description="Secure AI Database Assistant with Guardrails"
)

class QueryRequest(BaseModel):
    user_query: str

# Lista básica de comandos SQL bloqueados por seguridad
FORBIDDEN_COMMANDS = ["DROP", "DELETE", "ALTER", "TRUNCATE"]

@app.get("/")
async def root():
    return {"message": "DB-AI-Sentinel API running smoothly."}

@app.post("/query")
async def process_query(request: QueryRequest):
    query = request.user_query.upper()
    
    # Validación simple de guardrails
    if any(cmd in query for cmd in FORBIDDEN_COMMANDS):
        raise HTTPException(
            status_code=400, 
            detail="Operación no permitida por políticas de seguridad."
        )
    
    return {
        "status": "success",
        "message": "Consulta validada correctamente.",
        "input": request.user_query
    }
