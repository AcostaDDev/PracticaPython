"""
=========================================================================================================================
 Tener en cuenta que python diferencia entre mayusculas y minusculas
 Este módulo nos muestra como trabajar con estructuras de agrupación de elementos Arrays, tuplas y diccionarios
==========================================================================================================================
"""

#------------------------------------------------------------------------------------------------------------------------------
# 1 - Arrays o listas comienzan desde 0, una vez creados se pueden modificar sus elementos que no tienen por que ser homogeneos
#------------------------------------------------------------------------------------------------------------------------------


print("Trabajando con Arrays")
Array1 = ["Texto1", "Texto2",5,6]

#---------------------------------------------------------------------------------------------------------------------------------
# 2 - Tuplas comienzan desde 0, una vez creadas no se pueden modificar, son mas rápidas de acceso y recorrido que un array o lista
#---------------------------------------------------------------------------------------------------------------------------------

print("\nTRabajando con Tuplas")      # \n salto de linea
Tupla1 = ("Texto1", "Texto2", True)   #con parentesis o sin parentesis asume que es tupla
Tupla2 = "Texto1", "Texto2", "Texto3"
print("Imprimo toda la tupla1:", Tupla1)
print("Imprimo toda la tupla2:", Tupla2)
print("Imprimo segundo elemento de la tupla1 ", Tupla1[1])
print("Imprimo ultimo elemento de la tupla1 ", Tupla1[-1])     # con negativos, empiezo por el final

#-----------------------------------------------------------------------------------------------------------------------------
# 3 - Añado un elemento a un array
#-----------------------------------------------------------------------------------------------------------------------------

Array2 = [25, "Texto1", False, 12.5]
Array2.append("Texto2")
print("Hemos añadido un elemento al final: ", Array2)

#-----------------------------------------------------------------------------------------------------------------------------
# 4 - Añado un elemento en una posición determinada de un array
#-----------------------------------------------------------------------------------------------------------------------------

Array3 = ["Texto1", "Texto2", "Texto3"]
Array3.insert(1, "Texto1.1")                               # (1, es la posicion, recordemos que empiezan por 0 luego es la segunda)
print("Hemos añadido Texto1.1 en la posicon 2", Array3)

#-----------------------------------------------------------------------------------------------------------------------------
# 5 - Añado varios elemento al final del array
#-----------------------------------------------------------------------------------------------------------------------------

Array4 = ["Texto1", "Texto2", "Texto3"]
Array4.extend(["Texto4", "Texto5"])
print("Hemos añadido 2 elementos al final", Array4)

#-----------------------------------------------------------------------------------------------------------------------------
# 6 - Obtenemos la posicion de un elemento en un array, si no lo encuentra devuelve error a tratar con una excepción
#-----------------------------------------------------------------------------------------------------------------------------

Array5 = ["Texto1", "Texto2", "Texto3"]
print("Esta es la posicion de Texto2 dentro del Array -> ", Array5.index("Texto2"))

#-----------------------------------------------------------------------------------------------------------------------------
# 7 - Vemos si un elemento está en un array
#-----------------------------------------------------------------------------------------------------------------------------

Array6 = ["Texto1", "Texto2", "Texto3"]
print("Vemos si Texto1 está en el array:", "Texto1" in Array6)   # el elemento debe ser exactamente igual a lo que buscamos

#-----------------------------------------------------------------------------------------------------------------------------
# 8 - Eliminamos un elemento de un array
#-----------------------------------------------------------------------------------------------------------------------------

Array7 = ["Texto1", "Texto2", "Texto3"]
Array7.remove("Texto1")
print("Hemos eliminado Texto1 del array", Array7)    # si no lo encuentra no lo elimina pero no da error

#-----------------------------------------------------------------------------------------------------------------------------
# 9 - Eliminamos el último elemento del array
#-----------------------------------------------------------------------------------------------------------------------------

Array8 = [5, "Texto1", 1765]
Array8.pop()
print("Hemos eliminado el último elemento del array", Array8) 

#-----------------------------------------------------------------------------------------------------------------------------
# 10 - Concatenamos 2 arrays
#-----------------------------------------------------------------------------------------------------------------------------

Array9 = ["Madrid", 8]
Array10 = ["Barcelona", True]
Array11 = Array9 + Array10
print("Hemos concatenado 2 arrays: ", Array11)

#-----------------------------------------------------------------------------------------------------------------------------
# 11 - Repetimos un array n veces y se lo asignamos a otro
#-----------------------------------------------------------------------------------------------------------------------------

Array12 = ["Uno", "Dos"]
Array13 = Array12*3
print("Hemos creado un array repitiendo 3 veces otro: ", Array13)

#-----------------------------------------------------------------------------------------------------------------------------
# 12 - Vemos cuantas veces aparece un dato en un array, el dato debe coincidir entero para darlo por encontrado
#-----------------------------------------------------------------------------------------------------------------------------

Array14 = ["Texto1", "Texto2", "Texto3", "Texto1"]
print("Este es el número de veces que aparece un dato en un array -> ", Array14.count("Texto1"))

#-----------------------------------------------------------------------------------------------------------------------------
# 13 - Generamos una tupla desde un array
#-----------------------------------------------------------------------------------------------------------------------------

Array15 = ["Dato1", "Dato2", "Dato3", "Dato4"]
print("Array -> ", Array15)
TuplaDesdeArray = tuple(Array15)
print("Hemos generado una tupla desde un array -> ", TuplaDesdeArray)

#-----------------------------------------------------------------------------------------------------------------------------
# 14 - Generamos un array desde una tupla
#-----------------------------------------------------------------------------------------------------------------------------

Tupla3 = ("Dato1",)     # Forzamos con la , al final a que la tupla tenga un solo valor, sino la ponemos la crearía como variable
print("Tupla -> ", Tupla3)
ArrayDesdeTupla = list(Tupla3)
print("Hemos generado un array desde una tupla -> ", ArrayDesdeTupla)

#-----------------------------------------------------------------------------------------------------------------------------
# 15 - Generamos un array desde un string, donde cada elemento es un caracter del string
#-----------------------------------------------------------------------------------------------------------------------------

Variable1 = "Esto es un texto a convertir a array"
ArrayDesdeCadena = list(Variable1)
print("Hemos creado un array desde una cadena de caracteres -> ", ArrayDesdeCadena)

#-----------------------------------------------------------------------------------------------------------------------------
# 16 - Obtenemos el número de elementos de un array
#-----------------------------------------------------------------------------------------------------------------------------

Array16 = ["Dato1", "Dato2", True, False, 56]
print("El número de elementos del Array es -> ", len(Array16))

#-----------------------------------------------------------------------------------------------------------------------------
# 17 - Inicializamos varias variables desde un array
#-----------------------------------------------------------------------------------------------------------------------------

Array17 = ["Dato1", 2, "Dato3"]
Var1, Var2, Var3 = Array17       # debe coincidir el número de variables con los elementos del array, sino error no controlado
print("Hemos cargados 3 variables desde un array de 3 elementos", "Var1:", Var1, "Var2:", Var2, "Var3:", Var3)

#-----------------------------------------------------------------------------------------------------------------------------
#DICCIONARIOS - Los diccionarios son estructuras de datos que no están ordenadas y se almacenan en forma clave : valor; 
#pueden almacenar tuplas, arrays e incluso otros diccionarios, ¿a que suena a Json?
#-----------------------------------------------------------------------------------------------------------------------------

Diccionario1 = {"01":"Alava", "02":"Albacete","03":"Alicante"}
print("Esto es un diccionario clave-Datos -> ", Diccionario1) 

Diccionario2 = {"Aragón": ("Huesca", "Zaragoza", "Teruel"), "Galicia":("La Coruña", "Lugo", "Orense", "Pontevedra")}
print("Esto es un diccionario clave-tupla -> ", Diccionario2) 

Diccionario3 = {"Aragón": ["Huesca", "Zaragoza", "Teruel"], "Galicia":["La Coruña", "Lugo", "Orense", "Pontevedra"]}
print("Esto es un diccionario clave-array -> ", Diccionario3)

#-----------------------------------------------------------------------------------------------------------------------------
# 18 - Accedemos a datos concretos de diccionarios
#-----------------------------------------------------------------------------------------------------------------------------

Diccionario4 = {"01":"Alava", "02":"Albacete","03":"Alicante"}
print("Accedemos a un elemento concreto de un diccionario clave-datos -> ", Diccionario4["01"]) 
Diccionario5 = {"Aragón": ("Huesca", "Zaragoza", "Teruel"), "Galicia":("La Coruña", "Lugo", "Orense", "Pontevedra")}
print("Accedemos a un elemento concreto de un diccionario clave-tupla -> ", Diccionario5["Aragón"]) 

#-----------------------------------------------------------------------------------------------------------------------------------
# 19 - Borramos los datos de un dicionario que tengan una clave determinada
#      Importante: Aunque se pueden indicar claves duplicadas en un diccionario no se aconseja, de hecho internamente
#      se elimnan todas las claves duplicadas, quedando operativo sólo la últiuma aparición de la clave con su valor correspondiente
#-----------------------------------------------------------------------------------------------------------------------------------

Diccionario6 = {"01":True, 2:"Albacete","01":"Alicante"}
print(Diccionario6)      # sólo imprimirá {'01': 'Alicante', 2: 'Albacete'}
del Diccionario6["01"]
print("Hemos borrado un dato de un diccionario -> ", Diccionario6)  # imprimirá {2: 'Albacete'}

#-----------------------------------------------------------------------------------------------------------------------------
# 20 - Borramos el diccionario completo, no solo el contenido sino que la variable que lo contiene deja de estar definida
#    - Comentar que el del aplicado a una variable también elimina la variable
#-----------------------------------------------------------------------------------------------------------------------------

Diccionario6 = {"01":True, 2:"Albacete","01":"Alicante"}
print(Diccionario6)      # sólo imprimirá {'01': 'Alicante', 2: 'Albacete'}
del Diccionario6
print("Hemos borrado un dato de un diccionario -> ", Diccionario6)  # Da error, por variable Diccionario no definida

#-----------------------------------------------------------------------------------------------------------------------------
# 21 - Controlar si una variable existe o no (porque no la hemos definido todavía o la hemos borrado). 
#    - Es aplicable a variables, diccionarios, tuplas, arrays
#-----------------------------------------------------------------------------------------------------------------------------

var1 = 'dato 1'
if 'var1' in locals():
    print("la variable: var 1 existe y su valor es: ", var1)
else:
    print('la variable: var1 no existe')

#-----------------------------------------------------------------------------------------------------------------------------
# 22 - Obtenemos las claves de un diccionario
#-----------------------------------------------------------------------------------------------------------------------------

Diccionario7 = {"01":"Primer valor", "02":"Segundo valor",3:"Tercer valor"}
print("Obtenemos sólo las claves de un diccionario -> ", Diccionario7.keys())

#-----------------------------------------------------------------------------------------------------------------------------
# 23 - Obtenemos los valores de un diccionario
#-----------------------------------------------------------------------------------------------------------------------------

Diccionario8 = {"A1":True, 2:"Segundo valor"}
print("Obtenemos sólo las claves de un diccionario -> ", Diccionario8.values())

#-----------------------------------------------------------------------------------------------------------------------------
# 24 - Convertimos diccionario para trabajar con el como un array, obttenemos cada para, solo claves o sólo valores
#-----------------------------------------------------------------------------------------------------------------------------

Diccionario9 = {"01":"Primer valor", "02":"Segundo valor",3:"Tercer valor"}
Array9 = list(Diccionario9)           # Array9 contiene las keys del diccionario9, es lo mismo que Array9 = list(Diccionario9.keys())
Array91 = list(Diccionario9.items())  # Array 91 contiene un array de tuplas, donde cada tupla contiene una pareja clave valor del diccionario9
Array92 = list(Diccionario9.values()) # Array 92 contiene los valores del diccionario9

# Como son Arrays ahora puedo acceder por índice

print(Array9[0])  # 01
print(Array91[0]) # ('01', 'primer valor')
print(Array92[0]) # primer valor

#-----------------------------------------------------------------------------------------------------------------------------
# 25 - Obtenemos la posición de una cadena dentro de otra
#-----------------------------------------------------------------------------------------------------------------------------

Cadena1 = "Esta es la cadena principal donde buscamos caracteres"
Indice = Cadena1.find("prin")     # obtenemos en Indice la posición donde comienza prin
print("Esta es la posición donde comienza la cadena: ", Indice)
