from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.client import db_client
from db.models.usuario_serviu import Usuario_serviu
from db.schemas.usuario_serviu import usuario_serviu_schema, usuarios_serviu_schema
from bson import ObjectId
import routers.funciones as fun
#from routers.auth_user import oauth2

router=APIRouter(prefix="/usuario_serviu",tags=["usuario_serviu"])
registro_bd=db_client.usuario_serviu

#Retorno todos los usuario_serviu
@router.get("/", response_model=list[Usuario_serviu])
async def usuario_serviu():
    return fun.retorno_todos_perfiles(usuarios_serviu_schema,registro_bd)

#Agrego un usuario_serviu a la BD
@router.post("/")
async def perfil(usuario_serviu:Usuario_serviu):
    return fun.agrego_registro(Usuario_serviu,usuario_serviu_schema,usuario_serviu,"usuario_id",usuario_serviu.usuario_id,registro_bd)

#Elimino un usuario_serviu de la BD
@router.delete("/{id}")
async def perfil(id: str):
    return fun.elimino_registro(registro_bd,ObjectId(id))

#Edito un campo de una usuario_serviu en la BD
@router.put("/", response_model=Usuario_serviu,description="Esta funcion busca por el correo")
async def perfil(usuario_serviu:Usuario_serviu):
    return fun.edito_registro(Usuario_serviu,usuario_serviu_schema,usuario_serviu,"email",usuario_serviu.usuario_id,registro_bd)