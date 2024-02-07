from json import load                                     # Método load para carga de json externos

with open("P04_2_fichero.ini") as wficonfigura:
    dicconfigura = load(wficonfigura)
    

print(dicconfigura["conexion"]["ip"])
print(dicconfigura["conexion"]["puerto"])
print(dicconfigura["conexion"]["usuario"])
print(dicconfigura["conexion"]["pwd"])
print(dicconfigura["conexion"]["base"])		