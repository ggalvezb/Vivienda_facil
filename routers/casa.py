from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse,FileResponse
import gridfs
from pydantic import BaseModel
from db.client import db_client
from db.models.casa import Casa
from db.schemas.casa import casa_schema, casas_schema
from bson import ObjectId
import routers.funciones as fun
import os
#from routers.auth_user import oauth2

router=APIRouter(prefix="/casa",tags=["casa"])
registro_bd=db_client.casa

#Retorno todos los casa
@router.get("/", response_model=list[Casa])
async def casa():
    return fun.retorno_todos_perfiles(casas_schema,registro_bd)

#Agrego un casa a la BD
@router.post("/")
async def perfil(casa:Casa):
    return fun.agrego_registro(Casa,casa_schema,casa,"id",casa.id,registro_bd)

#Elimino un casa de la BD
@router.delete("/{id}")
async def perfil(id: str):
    return fun.elimino_registro(registro_bd,ObjectId(id))

#Edito un campo de una casa en la BD
@router.put("/", response_model=Casa,description="Esta funcion busca por el id")
async def perfil(casa:Casa):
    return fun.edito_registro(Casa,casa_schema,casa,"id",casa.id,registro_bd)

#Cargo una imagen (Test)
fs = gridfs.GridFS(db_client)
@router.post("/cargar_imagen/{id}")
async def upload_image(id:str,files: list[UploadFile] = File(...)):
    base_path = os.getcwd()
    nombre_carpeta = os.path.join(base_path, 'db', 'imagenes', 'casas',str(ObjectId(id)))
    #Verifico si existe carpeta para guardar la imagen
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
    else:
        print(f'La carpeta "{nombre_carpeta}" ya existe.')
    # Lista para almacenar los nombres de los archivos guardados
    nombres_archivos = []
    #Procedo a subir el archivo
    for index, file in enumerate(files,start=1):
        extension = file.filename.split('.')[-1].lower()
        if extension not in ['png', 'jpg', 'jpeg']:
            return {"error": f"El archivo {file.filename} no es un formato válido (PNG, JPG)."}
        nuevo_nombre_archivo = f"{index}.{extension}"
        # Guarda el archivo en la carpeta especificada
        path_archivo = os.path.join(nombre_carpeta, nuevo_nombre_archivo)
        with open(path_archivo, "wb") as myfile:
            content = await file.read()
            myfile.write(content)
            nombres_archivos.append(file.filename)
            myfile.close()
    return {"archivos_guardados": nombres_archivos}

#Obtengo una imagen (Test)
@router.get("/obtener_imagen/{ruta}")
def get_image(ruta:str):
    return FileResponse(os.getcwd()+"/"+ruta)

# Obtiene una lista de todas las rutas de las imágenes
@router.get("/listar_imagenes/{id}", response_model=list[str])
def list_images(id:str):
    base_path = os.path.join(os.getcwd(), 'db', 'imagenes', 'casas',str(id))
    rutas_imagenes = []

    # Recorrer el directorio y sus subdirectorios para encontrar todas las imágenes
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(('png', 'jpg', 'jpeg')):
                ruta_relativa = os.path.relpath(os.path.join(root, file), os.getcwd())
                rutas_imagenes.append(ruta_relativa)

    return rutas_imagenes

#Elimino una imagen
@router.delete("/borrar_imagen/{ruta}")
def delete_file(ruta:str):
    try:
        os.remove(os.getcwd()+"/"+ruta)
        return {"Foto Removida"}
    except:
        return {"Foto no encontrada"}