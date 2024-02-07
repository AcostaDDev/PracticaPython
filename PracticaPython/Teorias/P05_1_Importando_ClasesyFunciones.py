"""
=========================================================================================================================
 Clase y función a importar en otro fichero
==========================================================================================================================
"""

class coche():
	def __init__(self, marca, puertas, combustible, vendido):
		self.marca = marca 
		self.puertas = puertas
		self.combustible = combustible
		self.vendido = vendido
	def estavendido(self):
		self.vendido = True

def CalcularResto(dividendo, divisor):
	return(dividendo % divisor)
