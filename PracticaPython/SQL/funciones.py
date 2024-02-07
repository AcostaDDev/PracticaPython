from io import *
from conexion import Conexion
import pymysql

from json import load                                  

with open("SQL/datos.ini") as wficonfigura:
    dicconfigura = load(wficonfigura)

Conexion1 = Conexion(dicconfigura["conexion"]["ip"],dicconfigura["conexion"]["puerto"],dicconfigura["conexion"]["usuario"],dicconfigura["conexion"]["pwd"],dicconfigura["conexion"]["base"])


def crearTabla():
    query = "drop table if exists mae_empleados"
    Conexion1.cursor.execute(query)
    query = "CREATE TABLE mae_empleados (codigo VARCHAR(4) PRIMARY KEY, nombre VARCHAR(30), apellidos VARCHAR(45), nif VARCHAR(9), departamento VARCHAR(15), num_hijos INTEGER)"
    Conexion1.cursor.execute(query)

def insert():
    fich_altas = open("Ficheros/Altas.txt","r", encoding="utf8")
    fich_altas_correctas = open("SQL/Altas/Altas_Correctas.txt","w",encoding="utf8")
    fich_altas_fallidas = open("SQL/Altas/Altas_Fallidas.txt","w",encoding=("utf8"))
    fich_altas_correctas.write("Altas correctas: \n")
    fich_altas_fallidas.write("Altas fallidas: \n")
    lineas = fich_altas.readlines()
    for indice,l in enumerate(lineas):
        l = str(l).strip().split(";")
        l = str(l)[1:-1]
        try:
            query = "insert into mae_empleados values ({})".format(l)
            Conexion1.cursor.execute(query)
            Conexion1.connection.commit()
            print("Se ha insertado correctamente la sentencia numero: {}".format(indice+1))
            fich_altas_correctas.write("{}\n".format(l))
        except pymysql.Error as e:
            print("Ha ocurrido un error al insertar la sentencia numero: {}".format(indice+1))
            fich_altas_fallidas.write("{}\n".format(l))
            print(str(e))


    fich_altas_correctas.close()
    fich_altas_fallidas.close()
    fich_altas.close()

    del(fich_altas_correctas)
    del(fich_altas_fallidas)
    del(fich_altas)

def delete():
    fich_bajas = open("Ficheros/Bajas.txt","r", encoding="utf8")
    fich_bajas_correctas = open("SQL/Bajas/Bajas_Correctas.txt","w",encoding="utf8")
    fich_bajas_fallidas = open("SQL/Bajas/Bajas_Fallidas.txt","w",encoding=("utf8"))
    fich_bajas_correctas.write("Bajas correctas: \n")
    fich_bajas_fallidas.write("Bajas fallidas: \n")
    lineas = fich_bajas.readlines()
    for indice,l in enumerate(lineas):
        l = str(l).strip().split(";")
        l = str(l)[1:-1]
        try:
            query = "delete from mae_empleados where codigo = ({})".format(l)
            rows_affected = Conexion1.cursor.execute(query)
            if rows_affected == 0:
                print("No se encuentra el codigo {} en la tabla".format(l))
                fich_bajas_fallidas.write("{}\n".format(l))
            else:                
                print("Se ha ejecutado correctamente la sentencia numero: {}".format(indice+1))
                fich_bajas_correctas.write("{}\n".format(l))
            Conexion1.connection.commit()
        except pymysql.Error as e:
                print("Ha ocurrido un error al insertar la sentencia numero: {}".format(indice+1))
                fich_bajas_fallidas.write("{}\n".format(l))
                print(str(e))

    fich_bajas_correctas.close()
    fich_bajas_fallidas.close()
    fich_bajas.close()

    del(fich_bajas_correctas)
    del(fich_bajas_fallidas)
    del(fich_bajas)

def update():
    fich_modificaciones = open("Ficheros/Modificaciones.txt","r", encoding="utf8")
    fich_modificaciones_correctas = open("SQL/Modificaciones/Modificaciones_Correctas.txt","w",encoding="utf8")
    fich_modificaciones_fallidas = open("SQL/Modificaciones/Modificaciones_Fallidas.txt","w",encoding=("utf8"))
    fich_modificaciones_correctas.write("Modificaciones correctas: \n")
    fich_modificaciones_fallidas.write("Modificaciones fallidas: \n")
    lineas = fich_modificaciones.readlines()
    for indice,l in enumerate(lineas):
        l = str(l).strip().split(";")

        codigo = l[0]
        nombre = l[1]
        apellidos = l[2]
        nif = l[3]
        departamento = l[4]
        num_hijos = l[5]
        try:
            query = "update mae_empleados set codigo = '{}', nombre = '{}', apellidos = '{}', nif = '{}', departamento = '{}', num_hijos = '{}' where codigo = '{}'".format(codigo,nombre,apellidos,nif,departamento,num_hijos,codigo)
            rows_affected = Conexion1.cursor.execute(query)
            if rows_affected == 0:
                print("Ha ocurrido un error al modificar la sentencia numero: {}".format(indice+1))
                fich_modificaciones_fallidas.write("{}\n".format(str(l)[1:-1]))
            else:
                print("Se ha insertado correctamente la sentencia numero: {}".format(indice+1))
                fich_modificaciones_correctas.write("{}\n".format(str(l)[1:-1]))
            Conexion1.connection.commit()
        except pymysql.Error as e:
            print("Ha ocurrido un error al insertar la sentencia numero: {}".format(indice+1))
            print(str(e))
            fich_modificaciones_fallidas.write("{}\n".format(str(l)[1:-1]))


    fich_modificaciones_correctas.close()
    fich_modificaciones_fallidas.close()
    fich_modificaciones.close()

    del(fich_modificaciones_correctas)
    del(fich_modificaciones_fallidas)
    del(fich_modificaciones)

def select():
    fich_select = open("SQL/Lectura/Lectura.txt","w",encoding="utf8")
    fich_select.write("Consulta a la tabla mae_empleados \n")
    sql = "SELECT * FROM mae_empleados ORDER BY codigo"
    Conexion1.cursor.execute(sql)
    empleados = Conexion1.cursor.fetchall()

    try:
        for i in empleados:
            fich_select.write("Código -> {} || Nombre y Apellidos -> {} {} || NIF -> {} || Departamento -> {} || Num_Hijos -> {} \n".format(i[0],i[1],i[2],i[3],i[4],i[5]))
        print("Sentencia select completada")
    except pymysql.Error as e:
        print("Ha ocurrido un error en la select: ")
        print(str(e))
    fich_select.close()
    del(fich_select)

def closeConection():
    Conexion1.cursor.close()
    Conexion1.connection.close()