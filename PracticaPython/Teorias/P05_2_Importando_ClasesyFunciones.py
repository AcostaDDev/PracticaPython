"""
=========================================================================================================================
 Importando y utilizando clases y funciones de otro fichero
==========================================================================================================================

Podemos importar la clase coche y calcular resto desde el fichero "P05_1_Importando_ClasesyFunciones" 
e varias formas:
"""

# 1 - Importamos todos los elementos existentes en P05_1_Importando_ClasesyFunciones
from P05_1_Importando_ClasesyFunciones import *

# 2 - Importamos elementos determinados de P05_1_Importando_ClasesyFunciones
#from P05_1_Importando_ClasesyFunciones import coche
#from P05_1_Importando_ClasesyFunciones import CalcularResto

# 3 - Importamos P05_1_Importando_ClasesyFunciones asignándole un alias
# import P05_1_Importando_ClasesyFunciones as P05
# En este caso podríamos referenciar a un elemento de dicho fichero a través de su alias
# Para ejecutar la función CalcularResto(n, n) existente en P05_1_Importando_ClasesyFunciones
# escribiríamos ->    P05.CalcularResto(n, n)

# Si importamos 2 ficheros distintos, dentro de los cuales tenemos una función o clase con el mismo
# nombre, se utilzará la función o clase del fichero importado en último lugar. De la misma forma, si defino 
# 2 funciones o clases con el mismo nombre dentro del mismo fichero, prevalece la definida en último lugar 

# Si queremos importar archivos que se encuentran en otros directorios, podemos asignar temporalmente la variable 
# de entorno path, indicando el directorio donde esta el archivo antes de importarlo, así tendríamos las siguientes 3 líneas:
# import sys
# sys.path.append("C:\desarrollo\libreria")
# from P05_1_Importando_ClasesyFunciones import *

Coche1 = coche("Ferrari", 4, "Diesel", False)
print(Coche1.marca)             # atributo clase externa coche
print(CalcularResto(10,3))		# llamada a función externa CalcularResto
print(Coche1.vendido)
Coche1.estavendido()			# llamada a método de clase externa
print(Coche1.vendido)
