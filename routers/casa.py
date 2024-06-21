from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.client import db_client
from db.models.casa import Casa
from db.schemas.casa import casa_schema, casas_schema
from bson import ObjectId
import routers.funciones as fun
#from routers.auth_user import oauth2

router=APIRouter(prefix="/casa",tags=["casa"])
registro_bd=db_client.casa

#Retorno todos los casa
@router.get("/", response_model=list[Casa])
async def casa():
    return fun.retorno_todos_perfiles(casas_schema,registro_bd)

#Agrego un casa a la BD
@router.post("/")
async def perfil(casa:Casa):
    return fun.agrego_registro(Casa,casa_schema,casa,"id",casa.id,registro_bd)

#Elimino un casa de la BD
@router.delete("/{id}")
async def perfil(id: str):
    return fun.elimino_registro(registro_bd,ObjectId(id))

#Edito un campo de una casa en la BD
@router.put("/", response_model=Casa,description="Esta funcion busca por el id")
async def perfil(casa:Casa):
    return fun.edito_registro(Casa,casa_schema,casa,"id",casa.id,registro_bd)