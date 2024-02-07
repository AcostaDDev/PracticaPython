import pymysql

class Conexion:
	def __init__(self, host, puerto, usuario, password, basededatos):
		self.connection = pymysql.connect(
		host=host,
		port=puerto,   
		user=usuario,
		password=password,
		db = basededatos)

		self.cursor = self.connection.cursor()	