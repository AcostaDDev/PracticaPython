"""
=========================================================================================================================
 Trabajando con MySQL
 ir desasterisqueando cada uno de los módulos y comentando lo anteriores para ir creando la tabla de proveedores, 
 dando de alta registros, borrándolos, actualizándolos, consultándolos
==========================================================================================================================
"""
# La siguiente linea es operativa a pesar de estar comentada y definie el encoding utf-8 en la operativa con bases de datos
# Es conveniente añadirla para evitar transformaciones indeseadas de acentos, ñ, etc

# -*- coding: utf-8 -*-

# no es obligatorio indicar -*- en la línea anterior, se puede omitir
import pymysql

#--------------------------------------------------------------------------------------------------------------------------
# 1 - Conexión a base de datos
#--------------------------------------------------------------------------------------------------------------------------

# Creamos una clase Conexión, para trabajar con ella
# Parámetros, IP, puerto, usuario, password, nombre de la base de datos

class Conexion:
	def __init__(self, host, puerto, usuario, password, basededatos):
		self.connection = pymysql.connect(
		host=host,
		port=puerto,   
		user=usuario,
		password=password,
		db = basededatos)

		self.cursor = self.connection.cursor()

#podemos eliminar de la clase y la llamada el atributo -port, y la conexión se haría por omisión contra el puerto 3306

Conexion1 = Conexion("localhost", 3306, "root", "", "base01")		# Contra MySQL

#--------------------------------------------------------------------------------------------------------------------------
# Módulo 1 - Creamos tabla maestra de proveedores
#--------------------------------------------------------------------------------------------------------------------------

"""sql = "CREATE TABLE MAE_PROVEEDORES(COD_PROVEEDOR VARCHAR(3), NOM_PROVEEDOR VARCHAR(40), COD_PROVINCIA_PROVEEDOR VARCHAR(2), DIRECCION_PROVEEDOR VARCHAR(80), NUM_EMPLEADOS_PROVEEDOR INTEGER)" 
Conexion1.cursor.execute(sql)
Conexion1.connection.close()"""


#--------------------------------------------------------------------------------------------------------------------------
# Módulo 2 - Modificamos tabla MAE_Proveedores, añadimos clave primaria COD_Proveedor
#--------------------------------------------------------------------------------------------------------------------------

"""sql = "ALTER TABLE MAE_PROVEEDORES ADD PRIMARY KEY (COD_PROVEEDOR)" 
Conexion1.cursor.execute(sql)
Conexion1.connection.close()"""


#--------------------------------------------------------------------------------------------------------------------------
# Módulo 3 - Insertar Varios Registros
#--------------------------------------------------------------------------------------------------------------------------

# Forma 1


"""sql = "INSERT INTO MAE_PROVEEDORES (COD_PROVEEDOR, NOM_PROVEEDOR, COD_PROVINCIA_PROVEEDOR, DIRECCION_PROVEEDOR, NUM_EMPLEADOS_PROVEEDOR) \
VALUES ('001', 'CEMÉNÑOS CYY', '28', 'AVENIDA DE AMÉRICA 40', 100), \
('002', 'CARA COMO EL CEMENTO', '26', 'C/ MONFORTE 40', 50)"  
Conexion1.cursor.execute(sql)
Conexion1.connection.commit()
Conexion1.connection.close()"""


# Forma 2


"""vRegistrosNuevos = [
('003', 'ALUMINIOS MARTIN', '08', 'AVENIDA DIAGONAL 12', 30),
('004', 'MARMOL S.A.', '03', 'CALLE LANTANA 2', 18)
]

sql = "INSERT INTO MAE_PROVEEDORES (COD_PROVEEDOR, NOM_PROVEEDOR, COD_PROVINCIA_PROVEEDOR, DIRECCION_PROVEEDOR, NUM_EMPLEADOS_PROVEEDOR) VALUES (%s, %s, %s, %s, %s)"
Conexion1.cursor.executemany(sql, vRegistrosNuevos)
Conexion1.connection.commit()
Conexion1.connection.close()"""


#--------------------------------------------------------------------------------------------------------------------------
# Módulo 4 - Borra Registro
#--------------------------------------------------------------------------------------------------------------------------


"""sql = "DELETE FROM MAE_PROVEEDORES WHERE COD_PROVEEDOR = '004'"
Conexion1.cursor.execute(sql)
Conexion1.connection.commit()
Conexion1.connection.close()"""


#--------------------------------------------------------------------------------------------------------------------------
# Módulo 5 - Actualiza Registro
#--------------------------------------------------------------------------------------------------------------------------


"""sql = "UPDATE MAE_PROVEEDORES SET DIRECCION_PROVEEDOR = 'Otra direccion' WHERE COD_PROVEEDOR = '001'"
Conexion1.cursor.execute(sql)
Conexion1.connection.commit()
Conexion1.connection.close()"""


#--------------------------------------------------------------------------------------------------------------------------
# Módulo 6 - Obtenemos un registro
#--------------------------------------------------------------------------------------------------------------------------


"""sql = "SELECT * FROM MAE_PROVEEDORES WHERE COD_PROVEEDOR = '001'"
Conexion1.cursor.execute(sql)
rProveedor = Conexion1.cursor.fetchone()
print("Código proveedor -> ", rProveedor[0], "Nombre proveedor -> ", rProveedor[1])
Conexion1.cursor.close()
Conexion1.connection.close()"""


#--------------------------------------------------------------------------------------------------------------------------
# Módulo 7 - Obtenemos varios registros
#--------------------------------------------------------------------------------------------------------------------------


"""sql = "SELECT * FROM MAE_PROVEEDORES ORDER BY COD_PROVEEDOR"
Conexion1.cursor.execute(sql)
rProveedor = Conexion1.cursor.fetchall()

for rProveedor in rProveedor:
	print("Código proveedor -> ", rProveedor[0], "Nombre proveedor -> ", rProveedor[1], "Código provincia -> ", rProveedor[2])
Conexion1.cursor.close()
Conexion1.connection.close()"""