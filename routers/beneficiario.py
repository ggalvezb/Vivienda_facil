from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.client import db_client
from db.models.beneficiario import Beneficiario
from db.schemas.beneficiario import beneficiario_schema, beneficiarios_schema
from bson import ObjectId
import routers.funciones as fun
#from routers.auth_user import oauth2

router=APIRouter(prefix="/beneficiario",tags=["beneficiario"])
registro_bd=db_client.beneficiario

#Retorno todos los beneficiario
@router.get("/", response_model=list[Beneficiario])
async def beneficiario():
    return fun.retorno_todos_perfiles(beneficiarios_schema,registro_bd)

#Agrego un beneficiario a la BD
@router.post("/")
async def perfil(beneficiario:Beneficiario):
    return fun.agrego_registro(Beneficiario,beneficiario_schema,beneficiario,"usuario_id",beneficiario.usuario_id,registro_bd)

#Elimino un beneficiario de la BD
@router.delete("/{id}")
async def perfil(id: str):
    return fun.elimino_registro(registro_bd,ObjectId(id))

#Edito un campo de una beneficiario en la BD
@router.put("/", response_model=Beneficiario,description="Esta funcion busca por usuario_id")
async def perfil(beneficiario:Beneficiario):
    return fun.edito_registro(Beneficiario,beneficiario_schema,beneficiario,"usuario_id",beneficiario.usuario_id,registro_bd)
