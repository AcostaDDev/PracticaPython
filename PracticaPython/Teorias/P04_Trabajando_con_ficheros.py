"""
=========================================================================================================================
 Operaciones realizadas con ficheros
==========================================================================================================================
"""

from io import *				#para trabajar con ficheros debemos importar el modulo IO

#--------------------------------------------------------------------------------------------------------------------------
# 1 - Creamos fichero y añadimos filas
#--------------------------------------------------------------------------------------------------------------------------
# Conviene para solventar problemas de carácteres inválidos, añadir la codificación utf8 rn la apertura del fichero de salida
# param = encoding="utf8", pero sobre todo si el fichero es de entrada (lectura)

fichnombres = open("clientes.txt","w", encoding="utf8") 	# w-- Solo escritura
fichnombres.write("primera línea del fichero\n")			# /n para saltar linea e incorporar siguiente registro   
fichnombres.write("segunda línea del fichero")
fichnombres.close
del(fichnombres)    										# No lo borramos, liberamos memoria

#--------------------------------------------------------------------------------------------------------------------------
# 2 - Leemos fichero, hay varias formas de realizar dicha lectura
#--------------------------------------------------------------------------------------------------------------------------

# 2.1 - Con read - Devuelve los n primeros caracteres del fichero

print("1 - Leemos con read")
fichnombres = open("clientes.txt","r", encoding="utf8")
Var1 = fichnombres.read(1000)     # el 1000 es el número de caracteres que quiero obtener desde el puntero, que al abrir el fichero está al comienzo
print(Var1)
fichnombres.close
del(fichnombres)    

# 2.2 - Con readlines - Devuelve los caracteres del fichero a partir de donde se situa el puntero que al abrir está al principio 
# 		La devolución la realiza como array donde cada línea es un elemento y el retorno de carro se guarda como tal

print("\n2 - Leemos con readlines")
fichnombres = open("clientes.txt","r", encoding="utf8")
Var1 = fichnombres.readlines()     
print(Var1)
fichnombres.close
del(fichnombres)    

# 2.3 - for - lee todos los registros del fichero liena a linea

print("\n3 - Leemos con for")
fichnombres = open("clientes.txt", 'r', encoding="utf8")
for linea in fichnombres:
	print(linea)
fichnombres.close()
del(fichnombres)   

# 2.4 - Con Readline y while - Devuelve la linea del fichero donde esta el puntero, readline llega al final cuando devuelve ""

print("\n4 - Leemos con readline y while")
fichnombres = open("clientes.txt", 'r', encoding="utf8")
Var1 = "Datos"
while Var1 != "":
	Var1 = fichnombres.readline()
	print(Var1)
fichnombres.close()
del(fichnombres)   

#--------------------------------------------------------------------------------------------------------------------------
# 3 - Incorporamos lineas al fichero (al ejecutar todo el codigo siempre lo creamos con 2 y añadimos esta, ver por fuera)
#--------------------------------------------------------------------------------------------------------------------------

fichnombres = open("clientes.txt","a", encoding="utf8")
var1 = fichnombres.write("\ntercera línea del fichero") 
fichnombres.close()
del(fichnombres) 

#--------------------------------------------------------------------------------------------------------------------------
# 4 - Obtener el contenido de un directorio
#--------------------------------------------------------------------------------------------------------------------------

print("\nMostramos el contenido de un directorio")
from os import *
print(listdir())   # directorio actual
#print(listdir("C:\\Desarrollo\\python\\Practicas\\")) # un directorio en concreto