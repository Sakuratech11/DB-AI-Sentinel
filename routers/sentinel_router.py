from fastapi import APIRouter, HTTPException
from models.sentinel_model import ConsultaRequest, RespuestaSentinel
from database.connection import obtener_conexion

router = APIRouter(
    prefix="/sentinel",
    tags=["Sentinel Operations"]
)

@router.get("/estado-db", response_model=RespuestaSentinel)
def verificar_conexion():
    conexion = obtener_conexion()
    if conexion:
        conexion.close()
        return RespuestaSentinel(
            estado="éxito",
            mensaje="Conexión a MySQL establecida correctamente desde el router modular."
        )
    else:
        raise HTTPException(status_code=500, detail="No se pudo conectar a la base de datos.")

@router.post("/ejecutar-consulta", response_model=RespuestaSentinel)
def ejecutar_consulta_segura(pet: ConsultaRequest):
    # Aquí prepararemos el terreno para cuando llegue la IA y las consultas a la BD
    return RespuestaSentinel(
        estado="recibido",
        mensaje=f"Consulta lista para análisis: {pet.query}",
        datos={"descripcion": pet.descripcion}
    )
@router.get("/consultar-version-db")
def consultar_version_db():
    conexion = obtener_conexion()
    if not conexion:
        raise HTTPException(status_code=500, detail="No se pudo conectar a la base de datos.")
    
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT VERSION();")
        version = cursor.fetchone()
        cursor.close()
        conexion.close()
        return {
            "estado": "éxito",
            "motor": "MariaDB / MySQL",
            "version_servidor": version[0] if version else "Desconocida"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al ejecutar la consulta: {str(e)}")