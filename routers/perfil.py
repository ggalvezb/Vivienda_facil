from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.client import db_client
from db.models.perfil import Perfil
from db.schemas.perfil import perfil_schema, perfiles_schema
from bson import ObjectId
import routers.funciones as fun
#from routers.auth_user import oauth2

router=APIRouter(prefix="/perfil",tags=["perfil"])
registro_bd=db_client.perfil

#Retorno todos los perfil
@router.get("/", response_model=list[Perfil])
async def perfil():
    return fun.retorno_todos_perfiles(perfiles_schema,registro_bd)

#Agrego un perfil a la BD
@router.post("/")
async def perfil(perfil:Perfil):
    return fun.agrego_registro(Perfil,perfil_schema,perfil,"nombre_perfil",perfil.nombre_perfil,registro_bd)

#Elimino un perfil de la BD
@router.delete("/{id}")
async def perfil(id: str):
    return fun.elimino_registro(registro_bd,ObjectId(id))

#Edito un campo de una perfil en la BD
@router.put("/", response_model=Perfil,description="Esta funcion busca por el Nombre del Perfil")
async def perfil(perfil:Perfil):
    return fun.edito_registro(Perfil,perfil_schema,perfil,"nombre_perfil",perfil.nombre_perfil,registro_bd)