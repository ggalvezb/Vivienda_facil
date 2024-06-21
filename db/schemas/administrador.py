def administrador_schema(administrador) -> dict:
    return {"id": str(administrador["_id"]),
            "usuario_id": str(administrador["usuario_id"]),
    }



def administradores_schema(administradores) -> list:
    return [administrador_schema(administrador) for administrador in administradores]

