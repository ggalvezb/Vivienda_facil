from pydantic import BaseModel
from typing import Optional

#Entidad psat
class Administrador(BaseModel):
    id: Optional[str]
    usuario_id:str

