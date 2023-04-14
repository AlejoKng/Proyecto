import sqlite3

class Comunicacion():
    def __init__(self):
        self.conexion = sqlite3.connect( 'base_datos.db')
    
    def inserta_producto(self,codigo, nombre, modelo, precio, cantidad):
        cursor = self.conexion.cursor()
        bd='''INSERT INTO productos (CODIGO, NOMBRE, MODELO, PRECIO, CANTIDAD)
        VALUES('{}', '{}','{}', '{}','{}')'''.format(codigo, nombre, modelo, precio, cantidad)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM tabla_datos " 
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_producto):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM tabla_datos WHERE NOMBRE = {}'''.format(nombre_producto)
        cursor.execute(bd)
        nombrex = cursor.fetchall()
        cursor.close()     
        return nombrex

    def elimina_productos(self,nombre):
        cursor = self.conexion.cursor()
        bd='''DELETE FROM tabla_datos WHERE NOMBRE = {}'''.format(nombre)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()
        return nom   
    def actualiza_productos(self, codigo, nombre, modelo, precio, cantidad):
    cur = self.conexion.cursor()
    sql ='''UPDATE productos SET  CODIGO =' {}' , MODELO = '{}', PRECIO = '{}', CANTIDAD = '{}'
    WHERE NOMBRE = '{}' '''.format(codigo,  modelo, precio, cantidad, nombre)
    cur.execute(sql)
    act = cur.rowcount
    self.conexion.commit()    
    cur.close()
    return act