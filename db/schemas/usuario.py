def usuario_schema(usuario) -> dict:
    return {"id": str(usuario["_id"]),
            "email": str(usuario["email"]),
            "username":str(usuario["username"]),
            "clave":str(usuario["clave"]),
            "nombre":str(usuario["nombre"]),
            "rut":str(usuario["rut"]),
            "perfil_id":str(usuario["perfil_id"]),
    }

def usuarios_schema(usuarios) -> list:
    return [usuario_schema(usuario) for usuario in usuarios]

