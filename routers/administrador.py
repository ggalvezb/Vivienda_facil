from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.client import db_client
from db.models.administrador import Administrador
from db.schemas.administrador import administrador_schema, administradores_schema
from bson import ObjectId
import routers.funciones as fun
#from routers.auth_user import oauth2

router=APIRouter(prefix="/administrador",tags=["administrador"])
registro_bd=db_client.administrador

#Retorno todos los administrador
@router.get("/", response_model=list[Administrador])
async def administrador():
    return fun.retorno_todos_perfiles(administradores_schema,registro_bd)

#Agrego un administrador a la BD
@router.post("/")
async def perfil(administrador:Administrador):
    return fun.agrego_registro(Administrador,administrador_schema,administrador,"id",administrador.id,registro_bd)

#Elimino un administrador de la BD
@router.delete("/{id}")
async def perfil(id: str):
    return fun.elimino_registro(registro_bd,ObjectId(id))

#Edito un campo de una administrador en la BD
@router.put("/", response_model=Administrador,description="Esta funcion busca por el correo")
async def perfil(administrador:Administrador):
    return fun.edito_registro(Administrador,administrador_schema,administrador,"id",administrador.id,registro_bd)