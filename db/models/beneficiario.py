from pydantic import BaseModel
from typing import Optional

#Entidad psat
class Beneficiario(BaseModel):
    id: Optional[str]
    usuario_id:str
    edad:int
    comuna:str
    monto_subsidio:str
    monto_subsidio:str

