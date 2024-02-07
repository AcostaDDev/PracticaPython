"""
=========================================================================================================================
 Ejemplos de uso de except, tratamiento general, tratamiento específico
==========================================================================================================================
"""

import sys 

#--------------------------------------------------------------------------------------------------------------------------
# 1 - Control general de excepción, no preguntamos por un tipo de excepción concreto
#--------------------------------------------------------------------------------------------------------------------------

wContinuar = "S"
while wContinuar == "S":
	wNumero = input("Introduce un número: ")
	if wNumero == "0":
		wContinuar = "N"
		continue
	try:
		wNumero = int(wNumero) * 2
	except:
		print("El número introducido no es válido")
		continue
	print("El doble del valor introducido es: ", wNumero)
print("Ha finalizado el cálculo del doble")	

#--------------------------------------------------------------------------------------------------------------------------
# 2 - Analizamos el error que se produce en base a sys.exc_info(), debemos importar la libreria sys
#--------------------------------------------------------------------------------------------------------------------------

# Forzamos un error tipo ValueError:

try:
	Dato = int("aa")
except:                                   
	print("Este es el error completo que se ha producido: ",sys.exc_info(), "\n") # Devuelve una tupla, con varios valores, podemos obtener el primero que es el que más nos interesa
	print("Elemento 0 del array que es por el que preguntaremos en except: ", sys.exc_info()[0])

	print("\nRecorriendo el array de errores\n")
	for dato in sys.exc_info():
		print(dato)
else:
	print(Dato)

#----------------------------------------------------------------------------------------------------------------------------------
# 3 - En el ejercicio anterior vemos que el elemento 0 del array es "ValueError", es este dato el que debemos indicar en el except 
#	  si queremos gestionar cada error posible y realizar una accion determinada dependiendo del tipo de error
#     vemos un ejemplo completo con varios except, else y finally
#----------------------------------------------------------------------------------------------------------------------------------

try:
	int("aaa")								#Dato no numérico
	#Dato = 4/0								#Division por 0
	#open('ficheronoexistente.txt','r')		#Fichero no existente
	#Dato = 1								#Operación correcta
except ValueError:               
	print("Dato no numérico")
except ZeroDivisionError:
	print("División por cero")
except FileNotFoundError:	
	print("Fichero no encontrado")
except:										# Un except genérico debe ir al final
	print("No sabemos que pasó")
else:										# Cuando no se produce ninguna excepción
	print("Todo ha ido bien")
finally:									# Se ejecuta siempre al final del bloque, haya error o no
	print("Finalizó la ejecución")