from pydantic import BaseModel
from typing import Optional

#Entidad psat
class Usuario(BaseModel):
    id: Optional[str]
    username: Optional[str]
    email:str
    clave:str
    nombre:str
    rut:str
    perfil_id:str


