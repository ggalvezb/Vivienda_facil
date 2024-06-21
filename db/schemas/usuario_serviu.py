def usuario_serviu_schema(usuario_serviu) -> dict:
    return {"id": str(usuario_serviu["_id"]),
            "usuario_id": str(usuario_serviu["usuario_id"]),
            "casa_id":str(usuario_serviu["casa_id"]),
    }



def usuarios_serviu_schema(usuarios_serviu) -> list:
    return [usuario_serviu_schema(usuario_serviu) for usuario_serviu in usuarios_serviu]

