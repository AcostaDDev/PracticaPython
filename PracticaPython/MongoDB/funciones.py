from io import *
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://AcostaDav:Ghost1513715@practicapython.ub86zcm.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
Database = client["PracticaPython"]

def createCollection():
    Todaslascolecciones = Database.list_collection_names()
    if "mae_empleados" not in Todaslascolecciones:
        collection = Database.create_collection["mae_empleados"]
        fich_altas = open("Ficheros/Altas.txt","r", encoding="utf8")
        lineas = fich_altas.readlines()
    for indice,l in enumerate(lineas):
        l = str(l).strip().split(";")
        codigo = l[0]
        nombre = l[1]
        apellidos = l[2]
        nif = l[3]
        departamento = l[4]
        num_hijos = l[5]
        try:
            documentos = [{"codigo : '{}' , nombre : '{}' , apellidos : '{}' , nif : '{}' , departamento : '{}' , num_hijos : {}".format(codigo,nombre,apellidos,nif,departamento,num_hijos)}]
            collection._insert_one(documentos)
            print("La sentencia numero {} ha sido insertada correctamente".format(indice))
        except:
            print("Ha ocurrido un error al insertar la sentencia numero {}".format(indice))