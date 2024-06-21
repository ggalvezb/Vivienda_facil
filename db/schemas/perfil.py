def perfil_schema(perfil) -> dict:
    return {"id": str(perfil["_id"]),
            "nombre_perfil": str(perfil["nombre_perfil"]),
            "descripcion_perfil":str(perfil["descripcion_perfil"]),
    }

def perfiles_schema(perfiles) -> list:
    return [perfil_schema(perfil) for perfil in perfiles]

