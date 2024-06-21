def propietario_schema(propietario) -> dict:
    return {"id": str(propietario["_id"]),
            "nombre_propietario": str(propietario["nombre_propietario"]),
            "descripcion_propietario":str(propietario["descripcion_propietario"]),
    }

def propietarios_schema(propietarios) -> list:
    return [propietario_schema(propietario) for propietario in propietarios]

