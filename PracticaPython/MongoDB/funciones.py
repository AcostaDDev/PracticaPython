from io import *
import pymongo

uri = "mongodb+srv://AcostaDav:Ghost1513715@practicapython.ub86zcm.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)
Database = client["PracticaPython"]

def createCollection():
    collection = Database["mae_empleados"]
    Todaslascolecciones = Database.list_collection_names()
    if "mae_empleados" in Todaslascolecciones:
        collection.drop()
    collection = Database["mae_empleados"]
    fich_altas = open("Ficheros/Altas.txt","r", encoding="utf8")
    lineas = fich_altas.readlines()
    
 
    for indice,l in enumerate(lineas):
        l = str(l).strip().split(";")
        codigo = l[0]
        nombre = l[1]
        apellidos = l[2]
        nif = l[3]
        departamento = l[4]
        num_hijos = int(l[5])
        try:
            documentos = [{'codigo' : codigo , 'nombre' : nombre , 'apellidos' : apellidos , 'nif' : nif , 'departamento' : departamento , 'num_hijos' : num_hijos}]
            collection.insert_many(documentos)
            print("La sentencia numero {} ha sido insertada correctamente".format(indice))
        except Exception as e:
            print("Ha ocurrido un error al insertar la sentencia numero {}".format(indice))
            print(str(e))