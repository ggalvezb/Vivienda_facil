from pydantic import BaseModel
from typing import Optional

#Entidad psat
class Casa(BaseModel):
    id: Optional[str]
    direccion:str
    propietario_id:str
    estado:str
    rol_sii:str
    imagenes:str
    precio_oferta:str
    metros_cuadrados:str
    ampliacion:str
    ampliacion_regularizada:str


