"""
=========================================================================================================================
 Trabajando con MongoDB
 ir desasterisqueando cada uno de los módulos y comentando lo anteriores para ir creando la tabla de proveedores, 
 dando de alta registros, borrándolos, actualizándolos, consultándolos
==========================================================================================================================
"""
# La siguiente linea es operativa a pesar de estar comentada y define el encoding utf-8 en la operativa con bases de datos
# Es conveniente añadirla para evitar transformaciones indeseadas de acentos, ñ, etc

# -*- coding: utf-8 -*-

# no es obligatorio indicar -*- en la línea anterior, se puede omitir
import pymongo

#--------------------------------------------------------------------------------------------------------------------------
# 1 - Conexión a base de datos - ===>   PARA TRABAJAR CON LA BASE DE DATOS EN SaaS DEBE INSTALARSE DNSPYTHON   <===
#--------------------------------------------------------------------------------------------------------------------------
 
Cadenaconexion =  "mongodb://localhost:27017/"															# Conexion local
#Cadenaconexion =  "mongodb+srv://alumno01:alumno01@cluster0.jztsq.mongodb.net/BASESGE2022"				# Conexion al cluster SaaS de Mongo Atlas, requiere instalar dnspython
clienteMongo = pymongo.MongoClient(Cadenaconexion)
Database = clienteMongo["BDProveedores"]																# Base de datos Local
#Database = clienteMongo["BASESGE2024"]																	# Base de datos SaaS	

#--------------------------------------------------------------------------------------------------------------------------
# 2 - Vemos las colecciones que existen y si no existe la coleccion "ColProveedores", la creamos
#--------------------------------------------------------------------------------------------------------------------------

Todaslascolecciones = Database.list_collection_names()

if "ColProveedores" not in Todaslascolecciones:     #si no existe la coleccion, la creamos
	coleccion = Database["ColProveedores"]          #creamos coleccion
	Listadedocumentos = [
	{"COD_PROVEEDOR":"010", "NOM_PROVEEDOR":"CEMENTERA VALENCIA", "COD_PROVINCIA_PROVEEDOR":25, "DIRECCION_PROVEEDOR":"MOSTOLES", "NUM_EMPLEADOS_PROVEEDOR":5}]

	Alta = coleccion.insert_many(Listadedocumentos) #insertamos documentos en la colección


#--------------------------------------------------------------------------------------------------------------------------
# 3 - Creamos varios documentos en la coleccion ColProveedores
#--------------------------------------------------------------------------------------------------------------------------

"""
coleccion = Database["ColProveedores"]          #creamos colección
Listadedocumentos = [
{"COD_PROVEEDOR":"014","NOM_PROVEEDOR":"Cementos Portlan", "COD_PROVINCIA_PROVEEDOR":23, "DIRECCION_PROVEEDOR":"PLAZA DE CIBELES","NUM_EMPLEADOS_PROVEEDOR":4 },
{"COD_PROVEEDOR":"015","NOM_PROVEEDOR":"Asfalto S,A", "COD_PROVINCIA_PROVEEDOR":21, "DIRECCION_PROVEEDOR":"PLAZA DE NEPTUNO","NUM_EMPLEADOS_PROVEEDOR":8}
]
Alta = coleccion.insert_many(Listadedocumentos) #insertamos documentos en la colección
"""

#--------------------------------------------------------------------------------------------------------------------------
# 4 - Borramos documentos que cumplen una condicion, pej: COD_PROVEEDOR = "014"
#--------------------------------------------------------------------------------------------------------------------------

"""
coleccion = Database["ColProveedores"]
docQuery = {"COD_PROVEEDOR": "014"}				# docQuery es un documento que contiene el criterio de búsqueda
rcoleccion = coleccion.delete_many(docQuery)

print(rcoleccion.deleted_count,"Documentos borrados")
"""

#-----------------------------------------------------------------------------------------------------------------------------
# 5 - Actualizamos Documentos que cumplan una determinada condición, pej: COD_PROVEEDOR = "011" y COD_PROVINCIA_PROVEEDOR = 21
#-----------------------------------------------------------------------------------------------------------------------------

"""
coleccion = Database["ColProveedores"]
docQuery = {"COD_PROVEEDOR": "011", "COD_PROVINCIA_PROVEEDOR":21}	      # docQuery es un documento que contiene el criterio de búsqueda
docModificaciones = {"$set": {"DIRECCION_PROVEEDOR":"Nueva Direccion3"}}  # DocModificaciones contiene los cambios a realizar

rcoleccion = coleccion.update_many(docQuery,docModificaciones)
print(rcoleccion.modified_count,"Documentos actualizados")
"""

#--------------------------------------------------------------------------------------------------------------------------
# Módulo 6 - Obtenemos varios registros
#--------------------------------------------------------------------------------------------------------------------------

"""
coleccion = Database["ColProveedores"]
docQuery = {"COD_PROVEEDOR": "011"}          # Criterio de selección

 # Campos que quiero me devuelva, el parámetro 0 o 1 indica si queremos que no aparezca, aunque lo escribamos compo dato a traer
 # sólo se admite un 0, si docCapos={} se traerían todos los campos

docCampos =  {"_id" : 0, "COD_PROVEEDOR": 1, "NOM_PROVEEDOR": 1, "DIRECCION_PROVEEDOR": 1} 
for documento in coleccion.find(docQuery, docCampos):
	print(list(documento.values())[0])   # Mostramos COD_PROVEEDOR del documento
	print(list(documento.values())[1])   # Mostramos NOMBRE_PROVEEDOR del documento
	print(list(documento.values())[2])   # Mostramos DIRECCION_PROVEEDOR del documento
"""