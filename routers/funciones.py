from db.client import db_client

#Retorno todos los perfiles
def retorno_todos_perfiles(schemas,base_datos):
    return schemas(base_datos.find())

#Agrego un registro a la BD
def agrego_registro(Entidad,entidad_schema,dato,campo_de_busqueda,campo_a_buscar,base_datos):
    try:
        if type(search_perfil(Entidad,entidad_schema,campo_de_busqueda,campo_a_buscar,base_datos)) == Entidad:
            return {"El usuario ya existe"}
        
        perfil_dict=dict(dato)
        del perfil_dict["id"]
        id = base_datos.insert_one(perfil_dict).inserted_id
        new_user=entidad_schema(base_datos.find_one({"_id":id}))
        return Entidad(**new_user)
    except:
        return {"Error"}
    
#Elimino un registro de la BD
def elimino_registro(base_datos,id):
    found=base_datos.find_one_and_delete({"_id": id})
    if found:
        return {"Registro eliminado"}
    if not found:
        return {"Error: No se encontro registro"}   

#Edito un campo de un registro en la BD
def edito_registro(Entidad,entidad_schema,dato,campo_de_busqueda,campo_a_buscar,base_datos):
    registro_dict=dict(dato)
    del registro_dict["id"]
    try:
        base_datos.find_one_and_replace({campo_de_busqueda: campo_a_buscar}, registro_dict)
    except:
        return {"Error: No se a encontrado usuario"}
    return search_perfil(Entidad,entidad_schema,campo_de_busqueda,campo_a_buscar,base_datos)

#Funcion para buscar un registro
def search_perfil(Entidad,entidad_schema,field:str, key,base_datos):
    try:
        perfil = base_datos.find_one({field:key})
        return Entidad(**entidad_schema(perfil))
    except:
        return {"Error: No se a encontrado usuario"}


