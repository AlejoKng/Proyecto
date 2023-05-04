import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from PyQt5 import uic
from conexion_sqlite import Comunicacion

class VentanadeInicio(QMainWindow):
    def __init__(self):
        super(VentanadeInicio, self).__init__()
        uic.loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\Proyecto\d_ingreso.ui",self)
        self.VentanaOrden=VentanaOrden()
        #crear funcion que abra la ventanaprincipal cuando se de clic en ingreso
        self.bt_ingresar.clicked.connect(self.acceso)

    def acceso(self):
        self.close()
        self.VentanaOrden.show()
        
        

class VentanadePrincipal(QMainWindow):
    def __init__(self):
        super(VentanadePrincipal, self).__init__()
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\Proyecto\d_ingreso.ui",self)

class VentanaOrden(QMainWindow):
    def __init__(self):
        super(VentanaOrden, self).__init__()
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\Proyecto\d_ot.ui",self)
        self.provf=0 
        
        self.base_datos = Comunicacion()
        
        #Botones Superiores
        self.bt_menu.clicked.connect(self.mover_menu)
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_colapsar.clicked.connect(self.control_bt_normal)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        #Eliminar barra de titulo y opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        #Botones Laterales
        self.bt_database.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_base_datos))
        self.bt_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
        self.bt_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        self.bt_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        #self.bt_program.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_program))

        # Ancho de columna adaptable
        self.tabla_OT_pgElim.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_OT_pgBD.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        
        #SizeGrip
        self.gripSize=10
        self.grip=QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize,self.gripSize)

        # self.bt_registrar.clicked.connect(self.registrar_mantenimiento)
        # self.bt_pgReg_save.clicked.connect(self.registrar_mantenimiento)
        # self.bt_database.clicked.connect(self.basededatos_mantenimiento)
        # self.bt_actualizar.clicked.connect(self.modificar_mantenimiento)
        # self.bt_eliminar.clicked.connect(self.eliminar_mantenimiento)
        # self.bt_program.clicked.connect(self.programacion_mantenimiento)
        # self.bt_pgElim_consul.clicked.connect(self.buscar_OT_eliminar)
        # self.bt_pgElim_save.clicked.connect(self.actualiza_OT_eliminar)
        # self.bt_pgAct_consul.clicked.connect(self.buscar_OT_modificar)
        # self.bt_pgAct_save.clicked.connect(self.actualizar_OT_modificar)
        # self.bt_pgBD_refrescar.clicked.connect(self.actualizar_OT)

    ####################    FUNCIONES DE PAGINA ####################
    def control_bt_minimizar(self):
        print("hola")
        self.showMinimized()
    def control_bt_normal(self):
        if self.provf ==0:
            self.showNormal()
            self.provf=1
        else:
            self.showMaximized()
            self.provf=0
    def control_bt_maximizar(self):
        self.showMaximized()
    ### SizeGrip
    def resizeEvent(self,event):
        rect=self.rect()
        self.grip.move(rect.right()-self.gripSize,rect.bottom()-self.gripSize)
    ###Mover ventana
    def mousePressEvent(self,event):
        self.click_position = event.globalPos()
    def mover_ventana(self,event):
        if self.isMaximized()==False:
            if event.buttons()==QtCore.Qt.LeftButton:
                self.move(self.pos()+event.globalPos()-self.click_position)
                self.click_position=event.globalPos()
                event.accept()
        if event.globalPos().y()<=10:
            self.showMaximized()
        else:
            self.showNormal()
    def mover_menu(self):
        if True:
            width=self.frame_menu.width()
            normal=0
            if width==0:
                extender=300
            else:
                extender=normal
            self.animacion=QPropertyAnimation(self.frame_menu,b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
    ####################    FUNCIONES DE ACCION ####################
    ######    PAGINA RESUMEN    ######
    def mostrar_base(self):
        datos=self.base_datos.mostrar_base()
        i=len(datos)
        self.ot.setRowCount(i)
        tablerow=0
        for row in datos:
            self.Id=row[0]
            self.ot.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
            self.ot.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
            self.ot.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
            self.ot.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
            self.ot.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
            tablerow+=1
    ######    PAGINA REGISTRO   ######
    def registrar_mantenimiento(self):
        Consecutivo_orden =self.txb_pgReg_cod.text().upper()
        Fecha =self.txb_pgReg_fech.text().upper()
        Kilometraje =self.txb_pgReg_km.text().upper()
        Repuesto =self.txb_pgReg_rep.text().upper()
        Trabajo =self.txb_pgReg_trab.text().upper()
        if Consecutivo_orden!='' and Fecha!='' and Kilometraje!='' and Repuesto!='' and Trabajo!='':
            self.base_datos.registrar_mantenimiento(Consecutivo_orden, Fecha, Kilometraje, Trabajo, Repuesto)
            self.signal_registrar.setText('Productos Registrados')
            Consecutivo_orden =self.txb_pgReg_cod.clear()
            Fecha =self.txb_pgReg_fech.clear()
            Kilometraje =self.txb_pgReg_km.clear()
            Repuesto =self.txb_pgReg_rep.tclear()
            Trabajo =self.txb_pgReg_trab.clear()
        else:
            self.label_8.setText('Hay Espacios Vacios')
    ######    PAGINA ACTUALIZAR ######
    def actualizar_mate(self):
        consulta=self.txb_pgAct_NOrd.text().upper()
        consulta=str("'"+consulta+"'")
        self.orden=self.base_datos.buscar_ot(consulta)
        if (len(self.orden)!=0):
            self.Id=self.orden[0][0]
            self.txb_pgMod_cons.setText(self.orden[0][1])
            self.txb_pgMod_fech.setText(self.orden[0][2])
            self.txb_pgMod_km.setText(self.orden[0][3])
            self.txb_pgMod_trab.setText(self.orden[0][4])
            self.txb_pgMod_rep.setText(self.orden[0][5])
        else:
            self.lb_pgMod_actu.setText('Productos Actualizados')
            
  


        
    ######    PAGINA ELIMINAR   ######
    ######    PAGINA PROGRAMA   ######
    
        
class VentanadeTrabajos(QMainWindow):
    def __init__(self):
        super(VentanadeTrabajos, self).__init__()
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\Proyecto\d_trabajos.ui",self)

class Ventanadevehiculo(QMainWindow):
    def __init__(self):
        super(Ventanadevehiculo, self).__init__()
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\Proyecto\d_vh.ui",self)
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanadeInicio()
    mi_app.show()
    app.exec_()