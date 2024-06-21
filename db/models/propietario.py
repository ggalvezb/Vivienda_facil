from pydantic import BaseModel
from typing import Optional

#Entidad psat
class Perfil(BaseModel):
    id: Optional[str]
    usuario_id:str
    casa_id:Optional[list]


