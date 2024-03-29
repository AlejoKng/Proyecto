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
    
    def registrar_trabajo(self, trabajo, tipo, periodicidad):
        cursor = self.conexion.cursor()
        bd='''INSERT INTO trabajos (Trabajo, Tipo_mantenimiento,Periodicidad) VALUES ('{}', '{}', '{}')
            ON DUPLICATE KEY UPDATE Trabajo = '{}',Tipo_mantenimiento='{}', Periodicidad='{}' '''.format(trabajo, tipo, periodicidad,trabajo, tipo, periodicidad)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()

    def registrar_vehiculo(self, placa, marca, conductor, kilometraje):
        cursor = self.conexion.cursor()
        bd='''INSERT INTO vehiculos (Placa, Conductor, Marca, Kilometraje) VALUES ('{}', '{}', '{}', '{}')
            ON DUPLICATE KEY UPDATE Placa = '{}',Conductor='{}', Marca='{}', Kilometraje='{}' '''.format(placa, marca, conductor, kilometraje,placa, marca, conductor, kilometraje)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()

    def mostrar_base(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM registro_mantenimiento " 
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro
    
    def mostrar_base_vehiculos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM vehiculos " 
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro
    
    def mostrar_base_trabajos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM trabajos " 
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro
    
    def mostrar_base_repuestos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM repuestos " 
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro
    
    def base_un_filtro(self,consulta):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM registro_mantenimiento WHERE Consecutivo_orden='{}'".format(consulta) 
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro
    
    def base_ODO(self,consulta):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM odometro WHERE Placa='{}'".format(consulta) 
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro
    
    def todo_base_ODO(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM odometro "
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro
    
    def todo_base_PRO(self):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO programacion_mantenimiento (Consecutivo_orden, Placa, Trabajo, Proximo_mantenimiento_km)
                SELECT r.Consecutivo_orden, v.Placa, t.Trabajo, r.Kilometraje + t.Periodicidad
                FROM vehiculos v
                JOIN registro_mantenimiento r ON v.Placa = r.Placa
                JOIN trabajos t ON r.Trabajo = t.Trabajo
                LEFT JOIN programacion_mantenimiento p ON r.Consecutivo_orden = p.Consecutivo_orden
                WHERE p.Consecutivo_orden IS NULL OR r.Kilometraje + t.Periodicidad > p.Proximo_mantenimiento_km;'''
        cursor.execute(bd)
        bd = "SELECT * FROM programacion_mantenimiento ORDER BY Consecutivo_orden DESC"
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro
    
    def modificar_ODO(self, Placa,Fecha, Kilometraje):
        cursor = self.conexion.cursor()
        bd ='''INSERT INTO odometro (Placa, Fecha, Kilometraje)
            VALUES ('{}', '{}', '{}')
            ON DUPLICATE KEY UPDATE Fecha='{}', Kilometraje='{}' '''.format(Placa, Fecha, Kilometraje, Fecha, Kilometraje)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def actualizar_trab(self,trabajo,Tipo_mantenimiento,Periodicidad,consulta):
        cursor = self.conexion.cursor()
        bd ='''UPDATE trabajos SET Trabajo="{}",Tipo_mantenimiento="{}",Periodicidad="{}" WHERE Trabajo="{}"'''.format(trabajo,Tipo_mantenimiento,Periodicidad,consulta)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    
    def eliminar_mante(self,consulta):
        cursor = self.conexion.cursor()
        bd='''DELETE FROM registro_mantenimiento WHERE Consecutivo_orden = {}'''.format(consulta)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()

    def eliminar_trabajo1(self,consulta):
        cursor = self.conexion.cursor()
        bd='''DELETE FROM trabajos WHERE Trabajo = "{}"'''.format(consulta)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()

    def buscar_orden(self, consecutivo):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM registro_mantenimiento WHERE Consecutivo_orden = {}'''.format(consecutivo)
        cursor.execute(bd)
        nombrex = cursor.fetchall()
        cursor.close()     
        return nombrex
    
    def buscar_trab(self, consulta):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM trabajos WHERE Trabajo='{}'".format(consulta) 
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro
    
    def buscar_vh(self, consulta):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM vehiculos WHERE Placa='{}'".format(consulta) 
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro
    
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

    def trae_trab(self):
            cursor = self.conexion.cursor()
            bd = '''SELECT Trabajo FROM trabajos'''
            cursor.execute(bd)
            nombrex = cursor.fetchall()
            cursor.close()
            vec=[]
            for x in nombrex:
                vec.append(x[0])
            return vec
    
    def trae_repu(self):
            cursor = self.conexion.cursor()
            bd = '''SELECT Repuesto FROM repuestos'''
            cursor.execute(bd)
            nombrex = cursor.fetchall()
            cursor.close()
            vec=[]
            for x in nombrex:
                vec.append(x[0])
            return vec
    
    def trae_vehi(self):
            cursor = self.conexion.cursor()
            bd = '''SELECT Placa FROM vehiculos'''
            cursor.execute(bd)
            nombrex = cursor.fetchall()
            cursor.close()
            vec=[]
            for x in nombrex:
                vec.append(x[0])
            return vec
            



    def programacion_mantenimiento(self, repuesto):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM tabla_datos WHERE NOMRE = {}'''.format(repuesto)
        cursor.execute(bd)
        nombrex = cursor.fetchall()
        cursor.close()     
        return nombrex

    

    def registrar_usuario(self, user_name, password):
        cursor = self.conexion.cursor()
        bd='''INSERT INTO usuarios (user_name, password)
        VALUES('{}', '{})'''.format(user_name, password)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()



    

