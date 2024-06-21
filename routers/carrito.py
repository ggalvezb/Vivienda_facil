from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.client import db_client
from db.models.carrito import Carrito
from db.schemas.carrito import carrito_schema, carritos_schema
from bson import ObjectId
import routers.funciones as fun
#from routers.auth_user import oauth2

router=APIRouter(prefix="/carrito",tags=["carrito"])
registro_bd=db_client.carrito

#Retorno todos los carrito
@router.get("/", response_model=list[Carrito])
async def carrito():
    return fun.retorno_todos_perfiles(carritos_schema,registro_bd)

#Agrego un carrito a la BD
@router.post("/")
async def perfil(carrito:Carrito):
    return fun.agrego_registro(Carrito,carrito_schema,carrito,"id",carrito.id,registro_bd)

#Elimino un carrito de la BD
@router.delete("/{id}")
async def perfil(id: str):
    return fun.elimino_registro(registro_bd,ObjectId(id))

#Edito un campo de una carrito en la BD
@router.put("/", response_model=Carrito,description="Esta funcion busca por el correo")
async def perfil(carrito:Carrito):
    return fun.edito_registro(Carrito,carrito_schema,carrito,"id",carrito.id,registro_bd)