def consultar_sentinel(prompt_usuario: str):
    """Consulta general al modelo sin base de datos"""
    try:
        response = client.models.generate_content(
            model="gemini-3.6",
            contents=prompt_usuario,
        )
        return response.text
    except Exception as e:
        return f"Error al consultar la IA: {e}"

def consultar_sentinel_con_db(prompt_usuario: str):
    """Jugada maestra: Une el esquema real de MariaDB con la IA"""
    try:
        esquema_actual = obtener_esquema_db()
        
        prompt_completo = (
            f"Actúa como un DBA experto. Aquí está la estructura actual de la base de datos del usuario:\n"
            f"{esquema_actual}\n\n"
            f"Responde a la siguiente solicitud del usuario basándote estrictamente en este esquema:\n"
            f"{prompt_usuario}"
        )
        
        response = client.models.generate_content(
            model="gemini-3.6",
            contents=prompt_completo,
        )
        return response.text
    except Exception as e:
        return f"Error al consultar la IA con contexto de BD: {e}"