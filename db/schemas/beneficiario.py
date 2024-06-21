def beneficiario_schema(beneficiario) -> dict:
    return {"id": str(beneficiario["_id"]),
            "usuario_id": str(beneficiario["usuario_id"]),
            "edad":str(beneficiario["edad"]),
            "comuna":str(beneficiario["comuna"]),
            "monto_subsidio":str(beneficiario["monto_subsidio"]),
    }



def beneficiarios_schema(beneficiarios) -> list:
    return [beneficiario_schema(beneficiario) for beneficiario in beneficiarios]

