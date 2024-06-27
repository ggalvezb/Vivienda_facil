from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.client import db_client
from db.models.usuario import Usuario
from db.schemas.usuario import usuario_schema, usuarios_schema
from bson import ObjectId
import routers.funciones as fun
#from routers.auth_user import oauth2

router=APIRouter(prefix="/usuario",tags=["usuario"])
registro_bd=db_client.usuario

#Retorno todos los usuario
@router.get("/", response_model=list[Usuario])
async def usuario():
    return fun.retorno_todos_perfiles(usuarios_schema,registro_bd)

#Agrego un usuario a la BD
@router.post("/")
async def usuario(usuario:Usuario):
    return fun.agrego_registro(Usuario,usuario_schema,usuario,"email",usuario.email,registro_bd)

#Elimino un usuario de la BD
@router.delete("/{id}")
async def perfil(id: str):
    return fun.elimino_registro(registro_bd,ObjectId(id))

#Edito un campo de una usuario en la BD
@router.put("/", response_model=Usuario,description="Esta funcion busca por el correo")
async def perfil(usuario:Usuario):
    return fun.edito_registro(Usuario,usuario_schema,usuario,"email",usuario.email,registro_bd)

#Retorno la informacion de un usuario
@router.get("/{correo}")
async def usuario(correo:str):
    return fun.search_perfil(Usuario,usuario_schema,"email",correo,registro_bd)

#Reviso si el usuario existe
@router.get("/check/{correo}")
async def perfil(correo:str):
    return fun.agrego_registro(Usuario,usuario_schema,usuario,"email",correo,registro_bd)