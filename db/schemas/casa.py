def casa_schema(casa) -> dict:
    return {"id": str(casa["_id"]),
            "direccion": str(casa["direccion"]),
            "propietario_id":str(casa["propietario_id"]),
            "estado":str(casa["estado"]),
            "rol_sii":str(casa["rol_sii"]),
            "imagenes":str(casa["imagenes"]),
            "precio_oferta":str(casa["precio_oferta"]),
            "metros_cuadrados":str(casa["metros_cuadrados"]),
            "ampliacion":str(casa["ampliacion"]),
            "ampliacion_regularizada":str(casa["ampliacion_regularizada"]),

    }

def casas_schema(casas) -> list:
    return [casa_schema(casa) for casa in casas]
