from pydantic import BaseModel
from typing import Optional

#Entidad psat
class Usuario_serviu(BaseModel):
    id: Optional[str]
    usuario_id:str
    casa_id:str


