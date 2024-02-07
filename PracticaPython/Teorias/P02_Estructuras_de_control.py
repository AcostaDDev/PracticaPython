"""
=========================================================================================================================
 Estructuras condicionales, flujos while y for
==========================================================================================================================
"""

#--------------------------------------------------------------------------------------------------------------------------
# 1 - Estructura IF
#--------------------------------------------------------------------------------------------------------------------------

Edad = 52

if Edad > 50:
    Caracteristica1 = "Mayor de 50"
    Caracteristica2 = "Joven"
else:
	Caracteristica1 = "Menor de 50"
	Caracteristica2 = "Muy Joven"
print("¿Como es una persona e 52 años? {} y {}".format(Caracteristica1, Caracteristica2))  # {} son sustituidos por las variables

#--------------------------------------------------------------------------------------------------------------------------
# 2 - Estructura ELIF
#--------------------------------------------------------------------------------------------------------------------------

Var1 = 120

if Var1 > 100:
	print("El número {} es mayor que 100".format(Var1))
elif Var1 < 50:
	print("El número {} es menor que 50".format(Var1))
else:
	print("El número {} está entre 50 y 100".format(Var1))

#--------------------------------------------------------------------------------------------------------------------------
# 3 - Estructura FOR
#--------------------------------------------------------------------------------------------------------------------------

# Elementos de una lista

Lista1 = [2, 4, 5, "dato1"]

for Dato in Lista1:	
	print(Dato,end= " ")  # El end hace que no saltemos de linea después del print
else:
	print("Son los datos de la lista")
print("He terminado de imprimir")     # el else es opcional, se ejecuta al acabar el bucle

# Elementos de un rango

# range(d, h, s): desde hasta y step, Si no pongo step, por omisión lo trataría como step 1, los 3 valores pueden ser negativos. El Hasta no se incluye en el resultado, el desde si
# range(n): Iria de 0 a n-1

for i in range(4,16,2):
    print(i)

#--------------------------------------------------------------------------------------------------------------------------
# 4 - Estructura While.    Solicitamos un número por pantalla hasta que incorpore un número par
#--------------------------------------------------------------------------------------------------------------------------

var2 = int(input("introduce número par: "))
while var2%2 != 0:   # % es el módulo, es decir el resto de una división, si se incorpora un dato no numérico se produce un error no conbtrolado
	var2 = int(input("El número introducido no es par, introduce otro: "))
print("Fin de programa, el número " + str(var2) + " es un número par")

#--------------------------------------------------------------------------------------------------------------------------
# 5 - Instrucciones de ruptura y salto de bucle
#--------------------------------------------------------------------------------------------------------------------------

# Continue

Lista2 = [1, 2, 3, 4, 5, 6]
for wDato in Lista2:
	if wDato == 3: continue   # salta hasta el final del bucle y sigue iterando
	print(wDato,end= " ")  # El end hace que no saltemos de linea después del print
else:   # el else es opcional, se ejecuta al acabar el bucle
	print("Son los datos de la lista y nos hemos saltado el 3")
print("He terminado de imprimir")

# Break

Lista3 = [1, 2, 3, 4, 5, 6]
for wDato in Lista3:
	if wDato == 3: break   # Finaliza el bucle
	print(wDato,end= " ")  # El end hace que no saltemos de linea después del print
else:   # el else es opcional, se ejecuta al acabar el bucle
	print("Son los datos de la lista y no imprimimos del 3 en adelante, incluido el 3")
print("He terminado de imprimir")