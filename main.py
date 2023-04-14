import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.uic import loadUi
from conexion_sqlite import Comunicacion

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('C:\Escritorio\DAVID\VS_Code\Proyecto\Proyecto\mante.ui',self)

        self.bt_menu.clicked.connect(self.mover_menu)

        self.base_datos = Comunicacion()

        self.bt_minimizar.clicked.connect(self.control_bt_normal)
        self.bt_colapsar.clicked.connect(self.control_bt_normal)
        self.bt_cerrar.clicked.connect(lambda: self.close())
    
        self.bt_database.clicked.connect(self.page_base_datos)
        self.bt_registrar.clicked.connect(self.registrar_mantenimiento)
        self.bt_actualizar.clicked.connect(self.modificar_mantenimiento)
        self.bt_eliminar.clicked.connect(self.eliminar_mantenimiento)
        self.bt_program.clicked.connect(self.programacion_mantenimiento)
        self.bt_pgElim_consul.clicked.connect(self.buscar_OT_eliminar)
        self.bt_pgElim_save.clicked.connect(self.actualiza_OT_eliminar)
        self.bt_pgAct_consul.clicked.connect(self.buscar_OT_modificar)
        self.bt_pgAct_save.clicked.connect(self.actualizar_OT_modificar)
        self.bt_pgReg_save.clicked.connect(self.guardar_OT)
        self.bt_pgBD_refrescar.clicked.connect(self.actualizar_OT)
        #Eliminar barra de titulo y opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        #SizeGrip
        self.gripSize=10
        self.grip=QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize,self.gripSize)

        #Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        #Conección de botones
        self.bt_database.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_base_datos))
        self.bt_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
        self.bt_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        self.bt_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        self.bt_program.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_program))

        # Ancho de columna adaptable
        self.tabla_OT_pgElim.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_OT_pgBD.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def control_bt_minimizar(self):
        self.showMinimized()
    def control_bt_normal(self):
        self.showNormal()
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
        if event.globalPOs().y()<=10:
            self.showMaximized()
        else:
            self.showNormal()
    def mover_menu(self):
        if True:
            width=self.frame_control.width()
            normal=0
            if width==0:
                extender=200
            else:
                etender=normal
            self.animacion=QPropertyAnimation(self.frame_control,b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
    def registrar_mantenimiento(self):
        codigo =self.reg_codigo.text().upper()
        nombre =self.reg_nombre.text().upper()
        modelo =self.reg_modelo.text().upper()
        precio =self.reg_precio.text().upper()
        cantidad =self.reg_cantidad.text().upper()
        if codigo!='' and nombre!='' and modelo!='' and cantidad!='' and precio!='':
            self.base_datos.registrar_mantenimiento(codigo,nombre,modelo,precio,cantidad)
            self.signal_registrar.setText('Productos Registrados')
            codigo =self.reg_codigo.clear()
            nombre =self.reg_nombre.clear()
            modelo =self.reg_modelo.clear()
            precio =self.reg_precio.clear()
            cantidad =self.reg_cantidad.clear()
        else:
            self.signal_registrar.setText('Hay Espacios Vacios')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = VentanaPrincipal()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())