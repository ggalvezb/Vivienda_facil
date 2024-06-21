from pydantic import BaseModel
from typing import Optional

#Entidad psat
class Carrito(BaseModel):
    id: Optional[str]
    beneficiario_id:str
    casa_id:int
    estado:str

