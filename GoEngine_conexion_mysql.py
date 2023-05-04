# Conexión con la base de datos
import sys
import mysql
import mysql.connector as db


class Comunicacion():
    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost',
                                                database='educationservices1',
                                                user='root',
                                                password='WestWind1003')
    
    def registrar_mantenimiento(self,Consecutivo_orden, Fecha, Kilometraje, Trabajo, Repuesto):
        cursor = self.conexion.cursor()
        bd='''INSERT INTO ot (Consecutivo_orden, Fecha, Kilometraje, Trabajo, Repuesto)
        VALUES('{}', '{}','{}', '{}','{}')'''.format(Consecutivo_orden, Fecha, Kilometraje, Trabajo, Repuesto)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()

    def mostrar_base(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM ot " 
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro

    def programacion_mantenimiento(self, repuesto):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM tabla_datos WHERE NOMRE = {}'''.format(repuesto)
        cursor.execute(bd)
        nombrex = cursor.fetchall()
        cursor.close()     
        return nombrex

    def eliminar_mantenimiento(self,trabajo):
        cursor = self.conexion.cursor()
        bd='''DELETE FROM tabla_datos WHERE NOMBRE = {}'''.format(trabajo)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()


    def modificar_mantenimiento(self, Consecutivo_orden, Fecha, Kilometraje, Trabajo, Repuesto):
        cursor = self.conexion.cursor()
        bd ='''UPDATE tabla_datos SET  Consecutivo_orden =' {}' , Fecha = '{}', Kilometraje = '{}', Trabajo = '{}', Repuesto = '{}'
        WHERE NOMBRE = '{}' '''.format(Consecutivo_orden, Fecha, Kilometraje, Trabajo, Repuesto)
        cursor.execute(bd)
        a = cursor.rowcount
        self.conexion.commit()    
        cursor.close()
        return a
    
    def registrar_vehiculo(self, Placa, Conductor, Marca, Kilometraje):
        cursor = self.conexion.cursor()
        bd='''INSERT INTO vehiculo (Placa, Conductor, Marca, Kilometraje)
        VALUES('{}', '{}','{}', '{}','{}')'''.format(Placa, Conductor, Marca, Kilometraje)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()

    def registrar_usuario(self, user_name, password):
        cursor = self.conexion.cursor()
        bd='''INSERT INTO usuarios (user_name, password)
        VALUES('{}', '{}','{}', '{}','{}')'''.format(user_name, password)
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
    def buscar_ot(self):
        print("crear buscador")

