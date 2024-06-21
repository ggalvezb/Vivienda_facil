def carrito_schema(carrito) -> dict:
    return {"id": str(carrito["_id"]),
            "beneficiario_id": str(carrito["beneficiario_id"]),
            "casa_id":str(carrito["casa_id"]),
            "estado":str(carrito["estado"]),
    }

def carritos_schema(carritos) -> list:
    return [carrito_schema(carrito) for carrito in carritos]

