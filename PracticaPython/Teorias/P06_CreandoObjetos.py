"""
==========================================================================================================================
Creamos clases con y sin herencia
Tener en cuenta que:
 - En python todos los atributos son públicos, no obstante por acuerdo entre programadores si un atributo es
   precedido de "_" por ejemplo _material, este atributo debe tratarse como privado.
 - Si a un atributo lo definimos con "__" delante, por ejemplo __material, python internamente renombra
   a este atributo para evitar coincidencias con las subclases que comienzan por __.
   Por ejemplo:
    __material  -> Es renombrado automáticamente por pytnom como _<nombre de la clase>_<atributo>, en este caso
	se renombraría a      _mueble__material
==========================================================================================================================
"""

#--------------------------------------------------------------------------------------------------------------------------
# 1 - Clase padre, muebles con constructor y métodos para cambiar el estado
#--------------------------------------------------------------------------------------------------------------------------

class mueble():
	def __init__(self, patas, material, color, precio):
		self.patas = patas 
		self.material = material
		self.color = color
		self.precio = precio
		self._estado = "en stock"    # El estado indicamos que es privado y que solo lo debemos modificar a través de las funciones de la clase, pero claro, esto nos lo podemos saltar
	def almacenar(self):
		self._estado = "en stock"
	def reservar(self):
		self._estado = "reservado"
	def vender(self):
		self._estado = "vendido"
	def MostrarEstado(self):
		print(self._estado)

#--------------------------------------------------------------------------------------------------------------------------
# 2 - Clase Mesa, silla y cama que heredan de muebles y tienen algún atributo más
#--------------------------------------------------------------------------------------------------------------------------

class mesa(mueble):
	diametro = 1
class silla(mueble):
	conrespaldo = True
class cama(mueble):
	Litera = False

# Creamos una instancia de cada objeto

mueble1 = mueble(6, "Aluminio", "Azul", 500)
mesa1 = mesa(4, "madera", "marrón", 120)
silla1 = silla(3, "metacrilato", "hielo", 200)
cama1 = cama(6, "hierro", "plata", 500)

# Mostramos un atributo particular del objeto “mesa” y uno general que figura en la clase “muebles”

print("=> Mostramos diámetro y material de la mesa")
print("Diámetro: ", mesa1.diametro, "     Material: " , mesa1.material)

# Cambiamos el estado del objeto mueble1 utilizando el método denominado “reservar”.

print("=> Mostramos estado del mueble antes y después de cambiarlo")
print("Estado anterior mueble -> ", end="")
mueble1.MostrarEstado()
mueble1.reservar()
print("Nuevo estado mueble -> ", end="")
mueble1.MostrarEstado()

# Cambiamos el estado del objeto mesa1 utilizando el método heredado de la clase “muebles” denominado “reservar”.

print("=> Mostramos estado de la mesa antes y después de cambiarlo")
print("Estado anterior -> ", end="")
mesa1.MostrarEstado()
mesa1.vender()
print("Nuevo estado -> ", end="")
mesa1.MostrarEstado()