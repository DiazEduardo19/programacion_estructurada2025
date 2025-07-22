from conexionBD import *
import datetime

def regsitrar(nombre,apellidos,email,contrasena):
    try:
        nom=nombre
        fecha=datetime.datetime.now()
        sql="insert into usuarios(nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s,)"
        val=(nombre,apellidos,email,contrasena,fecha)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return 
    

def inicio_sesion(email,contrasena):
    try:
        sql="select * from ususarios where email=%s and password=%s"
        val=(email,contrasena)
        cursor.exceute(sql,val)
        registro=cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return None