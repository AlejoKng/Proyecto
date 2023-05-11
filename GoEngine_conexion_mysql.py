# Conexión con la base de datos
import sys
import mysql
import mysql.connector as db


class Comunicacion():
    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost',
                                                database='myenginebase',
                                                user='root',
                                                password='WestWind1003')
    
    def registrar_mantenimiento(self, Fecha, Kilometraje, Trabajo, Repuesto,Placa):
        cursor = self.conexion.cursor()
        bd='''INSERT INTO registro_mantenimiento (registro_mantenimiento.Placa, Fecha, Kilometraje, Trabajo, Repuesto)
            VALUES ('{}', '{}', '{}', '{}', '{}')
            ON DUPLICATE KEY UPDATE registro_mantenimiento.Placa = '{}',Fecha='{}', Kilometraje='{}', Trabajo='{}', Repuesto='{}' '''.format(Placa, Fecha, Kilometraje, Trabajo, Repuesto, Placa,Fecha, Kilometraje, Trabajo, Repuesto)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()

    def mostrar_base(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM registro_mantenimiento " 
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro

    def buscar_orden(self, consecutivo):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM registro_mantenimiento WHERE Consecutivo_orden = {}'''.format(int(consecutivo))
        cursor.execute(bd)
        nombrex = cursor.fetchall()
        cursor.close()     
        return nombrex
    
    def modificar_mante(self, Fecha, Kilometraje, Trabajo, Repuesto,Placa,Consecutivo_orden):
        cursor = self.conexion.cursor()
        bd ='''INSERT INTO registro_mantenimiento (Consecutivo_orden, registro_mantenimiento.Placa, Fecha, Kilometraje, Trabajo, Repuesto)
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}')
            ON DUPLICATE KEY UPDATE registro_mantenimiento.Placa = '{}',Fecha='{}', Kilometraje='{}', Trabajo='{}', Repuesto='{}' '''.format(Consecutivo_orden, Placa, Fecha, Kilometraje, Trabajo, Repuesto, Placa,Fecha, Kilometraje, Trabajo, Repuesto)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()

    def verif_user(self, user):
        cursor = self.conexion.cursor()
        bd = '''SELECT password FROM usuarios WHERE user_name = '{}' '''.format(user)
        cursor.execute(bd)
        nombrex = cursor.fetchall()
        cursor.close()     
        return nombrex[0][0]





    def programacion_mantenimiento(self, repuesto):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM tabla_datos WHERE NOMRE = {}'''.format(repuesto)
        cursor.execute(bd)
        nombrex = cursor.fetchall()
        cursor.close()     
        return nombrex

    def eliminar_mantenimiento(self,trabajo):
        cursor = self.conexion.cursor()
        bd='''DELETE FROM registro_mantenimiento WHERE NOMBRE = {}'''.format(trabajo)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()


    
    
    def registrar_vehiculo(self, Placa, Conductor, Marca, Kilometraje):
        cursor = self.conexion.cursor()
        #bd='''INSERT INTO vehiculo (Placa, Conductor, Marca, Kilometraje)
        #VALUES('{}', '{}','{}', '{}','{}')'''.format(Placa, Conductor, Marca, Kilometraje)
        bd='''INSERT INTO registro_mantenimiento (registro_mantenimiento.Placa, Fecha, Kilometraje, Trabajo, Repuesto)
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}') ON DUPLICATE KEY 
            UPDATE registro_mantenimiento.Placa = '{}',Fecha='{}', Kilometraje='{}', Trabajo='{}', Repuesto='{}' '''.format(Placa, Conductor, Marca, Kilometraje)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()

    def registrar_usuario(self, user_name, password):
        cursor = self.conexion.cursor()
        bd='''INSERT INTO usuarios (user_name, password)
        VALUES('{}', '{})'''.format(user_name, password)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()

    def registrar_trabajos(self, Accion, Trabajo, Tipo_mantenimiento):
        cursor = self.conexion.cursor()
        bd='''INSERT INTO trabajos (Accion, Trabajo, Tipo_mantenimiento)
        VALUES('{}', '{}','{}', '{}','{}')'''.format(Accion, Trabajo, Tipo_mantenimiento)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()

    

