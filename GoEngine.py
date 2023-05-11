import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from PyQt5 import uic
from GoEngine_conexion_mysql import Comunicacion


class VentanadeInicio(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\QtWindows&Icons\d_ingreso.ui",self)

        #Base de datos
        self.base_datos = Comunicacion()

        #Botones Superiores
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_colapsar.clicked.connect(self.control_bt_normal)
        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.piv_col=0 
        self.piv_nav=0 

        #Eliminar barra de titulo y opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        #SizeGrip
        self.gripSize=10
        self.grip=QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize,self.gripSize)

        #crear funcion que abra la ventanaprincipal cuando se de clic en ingreso
        self.bt_ingresar.clicked.connect(self.acceso)

    #Funcionnes de movimiento y botones
    def control_bt_minimizar(self):
        print("hola")
        self.showMinimized()
    def control_bt_normal(self):
        if self.piv_col ==0:
            self.showNormal()
            self.piv_col=1
        else:
            self.showMaximized()
            self.piv_col=0
    def control_bt_maximizar(self):
        self.showMaximized()
    # SizeGrip
    def resizeEvent(self,event):
        rect=self.rect()
        self.grip.move(rect.right()-self.gripSize,rect.bottom()-self.gripSize)
    #Mover ventana
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

    def acceso(self):
        self.close()
        user =self.txb_usuario.text()
        contra =self.txb_contra.text()
        self.comp=self.base_datos.verif_user(user)
        print(contra,"=",self.comp)
        if(self.comp==contra):
            self.VentanaOrden=VentanaOrden()
            self.VentanaOrden.show()


    
        

    
        

class VentanadePrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\QtWindows&Icons\d_principal.ui",self)

        #Base de datos
        self.base_datos = Comunicacion()

        #Botones Superiores
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_colapsar.clicked.connect(self.control_bt_normal)
        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.piv_col=0 
        self.piv_nav=0 

        #Eliminar barra de titulo y opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #SizeGrip
        self.gripSize=10
        self.grip=QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize,self.gripSize)

        # Ancho de columna adaptable
        self.tabla_pgAkm_Km.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_pgAkm_Km.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        #Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
                
        #Botones Navegar
        self.bt_nav_tra.clicked.connect(self.navego_tra)
        self.bt_nav_veh.clicked.connect(self.navego_veh)
        self.bt_nav_rep.clicked.connect(self.navego_rep)
        self.bt_nav_prin.clicked.connect(self.navego_prin)
        self.bt_nav_man.clicked.connect(self.navego_man)
        self.bt_ingreso.clicked.connect(self.navego_ing)
        

    def control_bt_minimizar(self):
        self.showMinimized()
    def control_bt_normal(self):
        if self.piv_col ==0:
            self.showNormal()
            self.piv_col=1
        else:
            self.showMaximized()
            self.piv_col=0
    def control_bt_maximizar(self):
        self.showMaximized()
    # SizeGrip

    def resizeEvent(self,event):
        rect=self.rect()
        self.grip.move(rect.right()-self.gripSize,rect.bottom()-self.gripSize)
    # Mover ventana
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
    
    def mover_navegar(self):
        if True:
            rect = self.frame_navegar.geometry()
            normal = QtCore.QRect(1, 108, rect.width(), 0)
            extender = QtCore.QRect(1, 108, rect.width(), 64)
            print(rect,",",normal,",",extender)
            if rect == normal:
                endRect = extender
            else:
                endRect = normal
            #print(rect,",",endRect)
            self.animacion = QPropertyAnimation(self.frame_navegar, b"geometry")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(rect)
            self.animacion.setEndValue(endRect)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
    #Botones de Navegar
    def navego_tra(self):
        self.close()
        self.VentanadeTrabajos=VentanadeTrabajos()
        self.VentanadeTrabajos.show()
    def navego_veh(self):
        self.close()
        self.Ventanadevehiculo=Ventanadevehiculo()
        self.Ventanadevehiculo.show()          
    def navego_rep(self):
        self.close()
        self.VentanadeRepuestos=VentanadeRepuestos()
        self.VentanadeRepuestos.show()
    def navego_prin(self):
        self.close()
        self.VentanadePrincipal=VentanadePrincipal()
        self.VentanadePrincipal.show() 
    def navego_man(self):
        self.close()
        self.VentanaOrden=VentanaOrden()
        self.VentanaOrden.show()
    def navego_ing(self):
        self.close()
        self.VentanadeInicio=VentanadeInicio()
        self.VentanadeInicio.show()

class VentanaOrden(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\QtWindows&Icons\d_ot.ui",self)

        #Base de datos
        self.base_datos = Comunicacion()

        #Botones Superiores
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_colapsar.clicked.connect(self.control_bt_normal)
        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.piv_col=0 
        self.piv_nav=0 

        #Eliminar barra de titulo y opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #SizeGrip
        self.gripSize=10
        self.grip=QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize,self.gripSize)

        # Ancho de columna adaptable
        self.tabla_pgElim_OT.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_pgBD_OT.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        #Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
                
        #Botones Navegar
        self.bt_nav_tra.clicked.connect(self.navego_tra)
        self.bt_nav_veh.clicked.connect(self.navego_veh)
        self.bt_nav_rep.clicked.connect(self.navego_rep)
        self.bt_nav_prin.clicked.connect(self.navego_prin)
        self.bt_nav_man.clicked.connect(self.navego_man)
        self.bt_ingreso.clicked.connect(self.navego_ing)
    ####################    FUNCIONES DE PAGINA ####################
        #Botones Laterales
        self.bt_menu.clicked.connect(self.mover_menu)
        self.bt_naveg.clicked.connect(self.mover_navegar)
        self.bt_pgBD_refrescar.clicked.connect(self.mostrar_base)
        self.bt_pgReg_save.clicked.connect(self.registrar_mantenimiento)
        self.bt_pgMod_Act.clicked.connect(self.modificar_mante)
        self.bt_pgMod_Con.clicked.connect(self.actualizar_mante)
        self.bt_database.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_base_datos))
        self.bt_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
        self.bt_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_modificar))
        self.bt_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        #self.bt_program.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_program))
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
        

    def control_bt_minimizar(self):
        self.showMinimized()
    def control_bt_normal(self):
        if self.piv_col ==0:
            self.showNormal()
            self.piv_col=1
        else:
            self.showMaximized()
            self.piv_col=0
    def control_bt_maximizar(self):
        self.showMaximized()
    # SizeGrip

    def resizeEvent(self,event):
        rect=self.rect()
        self.grip.move(rect.right()-self.gripSize,rect.bottom()-self.gripSize)
    # Mover ventana
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
    
    def mover_navegar(self):
        if True:
            rect = self.frame_navegar.geometry()
            normal = QtCore.QRect(1, 108, rect.width(), 0)
            extender = QtCore.QRect(1, 108, rect.width(), 64)
            print(rect,",",normal,",",extender)
            if rect == normal:
                endRect = extender
            else:
                endRect = normal
            #print(rect,",",endRect)
            self.animacion = QPropertyAnimation(self.frame_navegar, b"geometry")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(rect)
            self.animacion.setEndValue(endRect)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
    #Botones de Navegar
    def navego_tra(self):
        self.close()
        self.VentanadeTrabajos=VentanadeTrabajos()
        self.VentanadeTrabajos.show()
    def navego_veh(self):
        self.close()
        self.Ventanadevehiculo=Ventanadevehiculo()
        self.Ventanadevehiculo.show()          
    def navego_rep(self):
        self.close()
        self.VentanadeRepuestos=VentanadeRepuestos()
        self.VentanadeRepuestos.show()
    def navego_prin(self):
        self.close()
        self.VentanadePrincipal=VentanadePrincipal()
        self.VentanadePrincipal.show() 
    def navego_man(self):
        self.close()
        self.VentanaOrden=VentanaOrden()
        self.VentanaOrden.show()
    def navego_ing(self):
        self.close()
        self.VentanadeInicio=VentanadeInicio()
        self.VentanadeInicio.show()
    ####################    FUNCIONES DE ACCION DE PAGINA ####################
    ######    PAGINA RESUMEN    ######
    def mostrar_base(self):
        datos=self.base_datos.mostrar_base()
        i=len(datos)
        print(datos)
        self.tabla_pgBD_OT.setRowCount(i)
        tablerow=0
        for row in datos:
            self.tabla_pgBD_OT.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_pgBD_OT.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_pgBD_OT.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[1].strftime("%d-%m-%Y")))
            self.tabla_pgBD_OT.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_pgBD_OT.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[4]))
            self.tabla_pgBD_OT.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[5]))
            tablerow+=1
    ######    PAGINA REGISTRO   ######
    def registrar_mantenimiento(self):
        Placa =self.tBox_pgReg_Con.text().upper()
        Fecha = self.tBox_pgReg_Fec.text()
        Kilometraje = int(self.tBox_pgReg_Km.text().upper())
        Repuesto =self.cBox_pgReg_Rep.text()
        Trabajo =self.cBox_pgReg_Tra.text()
        if Placa!='' and Fecha!='' and Kilometraje!='' and Repuesto!='' and Trabajo!='':
            self.base_datos.registrar_mantenimiento( Fecha, Kilometraje, Trabajo, Repuesto,Placa)
            self.lb_pgReg_Nord.setText('Mantenimiento Registrado')
            Placa =self.tBox_pgReg_Con.clear()
            Fecha =self.tBox_pgReg_Fec.clear()
            Kilometraje =self.tBox_pgReg_Km.clear()
            Repuesto =self.cBox_pgReg_Rep.clear()
            Trabajo =self.cBox_pgReg_Tra.clear()
        else:
            self.lb_pgReg_Nord.setText('Hay Espacios Vacios')

    ######    PAGINA MODIFICAR ######
    def actualizar_mante(self):
        consulta=self.tBox_pgMod_Nord.text().upper()
        consulta=str(consulta)
        self.orden=self.base_datos.buscar_orden(consulta)
        if (len(self.orden)!=0):
            print(self.orden[0][1])
            self.tBox_pgMod_Pla.setText(str(self.orden[0][5]))
            self.tBox_pgMod_Fec.setText(self.orden[0][1].strftime("%Y-%m-%d"))
            self.txb_pgMod_Km.setText(str(self.orden[0][2]))
            self.cBox_pgMod_Tra.setText(self.orden[0][3])
            self.cBox_pgMod_Rep.setText(self.orden[0][4])
        else:
            self.lb_pgMod_Act.setText('Dato no encontrado')
        
    def modificar_mante(self):
        consulta=self.tBox_pgMod_Nord.text()
        consulta=str(consulta)
        Placa =self.tBox_pgMod_Pla.text().upper()
        Fecha = self.tBox_pgMod_Fec.text()
        Kilometraje = int(self.txb_pgMod_Km.text().upper())
        Repuesto =self.cBox_pgMod_Rep.text()
        Trabajo =self.cBox_pgMod_Tra.text()
        if Placa!='' and Fecha!='' and Kilometraje!='' and Repuesto!='' and Trabajo!='':
            self.base_datos.modificar_mante(Fecha, Kilometraje, Trabajo, Repuesto, Placa,consulta)
            self.lb_pgMod_Act.setText('Mantenimiento Registrado')
            Placa =self.tBox_pgMod_Pla.clear()
            Fecha =self.tBox_pgMod_Fec.clear()
            Kilometraje =self.txb_pgMod_Km.clear()
            Repuesto =self.cBox_pgMod_Rep.clear()
            Trabajo =self.cBox_pgMod_Tra.clear()
        else:
            self.lb_pgMod_Act.setText('Hay Espacios Vacios')
    
    ######    PAGINA ELIMINAR   ######

    ######    PAGINA PROGRAMA   ######
    
        
class VentanadeTrabajos(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\QtWindows&Icons\d_trabajos.ui",self)

        #Base de datos
        self.base_datos = Comunicacion()

        #Botones Superiores
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_colapsar.clicked.connect(self.control_bt_normal)
        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.piv_col=0 
        self.piv_nav=0 

        #Eliminar barra de titulo y opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #SizeGrip
        self.gripSize=10
        self.grip=QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize,self.gripSize)

        # Ancho de columna adaptable
        self.tabla_pgElim_OT.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_pgBD_OT.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        #Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
                
        #Botones Navegar
        self.bt_nav_tra.clicked.connect(self.navego_tra)
        self.bt_nav_veh.clicked.connect(self.navego_veh)
        self.bt_nav_rep.clicked.connect(self.navego_rep)
        self.bt_nav_prin.clicked.connect(self.navego_prin)
        self.bt_nav_man.clicked.connect(self.navego_man)
        self.bt_ingreso.clicked.connect(self.navego_ing)
        

    def control_bt_minimizar(self):
        self.showMinimized()
    def control_bt_normal(self):
        if self.piv_col ==0:
            self.showNormal()
            self.piv_col=1
        else:
            self.showMaximized()
            self.piv_col=0
    def control_bt_maximizar(self):
        self.showMaximized()
    # SizeGrip

    def resizeEvent(self,event):
        rect=self.rect()
        self.grip.move(rect.right()-self.gripSize,rect.bottom()-self.gripSize)
    # Mover ventana
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
    
    def mover_navegar(self):
        if True:
            rect = self.frame_navegar.geometry()
            normal = QtCore.QRect(1, 108, rect.width(), 0)
            extender = QtCore.QRect(1, 108, rect.width(), 64)
            print(rect,",",normal,",",extender)
            if rect == normal:
                endRect = extender
            else:
                endRect = normal
            #print(rect,",",endRect)
            self.animacion = QPropertyAnimation(self.frame_navegar, b"geometry")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(rect)
            self.animacion.setEndValue(endRect)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
    #Botones de Navegar
    def navego_tra(self):
        self.close()
        self.VentanadeTrabajos=VentanadeTrabajos()
        self.VentanadeTrabajos.show()
    def navego_veh(self):
        self.close()
        self.Ventanadevehiculo=Ventanadevehiculo()
        self.Ventanadevehiculo.show()          
    def navego_rep(self):
        self.close()
        self.VentanadeRepuestos=VentanadeRepuestos()
        self.VentanadeRepuestos.show()
    def navego_prin(self):
        self.close()
        self.VentanadePrincipal=VentanadePrincipal()
        self.VentanadePrincipal.show() 
    def navego_man(self):
        self.close()
        self.VentanaOrden=VentanaOrden()
        self.VentanaOrden.show()
    def navego_ing(self):
        self.close()
        self.VentanadeInicio=VentanadeInicio()
        self.VentanadeInicio.show()


class Ventanadevehiculo(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\QtWindows&Icons\d_vh.ui",self)
        
        #Base de datos
        self.base_datos = Comunicacion()

        #Botones Superiores
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_colapsar.clicked.connect(self.control_bt_normal)
        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.piv_col=0 
        self.piv_nav=0 

        #Eliminar barra de titulo y opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #SizeGrip
        self.gripSize=10
        self.grip=QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize,self.gripSize)

        # Ancho de columna adaptable
        self.tabla_pgElim_OT.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_pgBD_OT.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        #Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
                
        #Botones Navegar
        self.bt_nav_tra.clicked.connect(self.navego_tra)
        self.bt_nav_veh.clicked.connect(self.navego_veh)
        self.bt_nav_rep.clicked.connect(self.navego_rep)
        self.bt_nav_prin.clicked.connect(self.navego_prin)
        self.bt_nav_man.clicked.connect(self.navego_man)
        self.bt_ingreso.clicked.connect(self.navego_ing)
        

    def control_bt_minimizar(self):
        self.showMinimized()
    def control_bt_normal(self):
        if self.piv_col ==0:
            self.showNormal()
            self.piv_col=1
        else:
            self.showMaximized()
            self.piv_col=0
    def control_bt_maximizar(self):
        self.showMaximized()
    # SizeGrip

    def resizeEvent(self,event):
        rect=self.rect()
        self.grip.move(rect.right()-self.gripSize,rect.bottom()-self.gripSize)
    # Mover ventana
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
    
    def mover_navegar(self):
        if True:
            rect = self.frame_navegar.geometry()
            normal = QtCore.QRect(1, 108, rect.width(), 0)
            extender = QtCore.QRect(1, 108, rect.width(), 64)
            print(rect,",",normal,",",extender)
            if rect == normal:
                endRect = extender
            else:
                endRect = normal
            #print(rect,",",endRect)
            self.animacion = QPropertyAnimation(self.frame_navegar, b"geometry")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(rect)
            self.animacion.setEndValue(endRect)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
    #Botones de Navegar
    def navego_tra(self):
        self.close()
        self.VentanadeTrabajos=VentanadeTrabajos()
        self.VentanadeTrabajos.show()
    def navego_veh(self):
        self.close()
        self.Ventanadevehiculo=Ventanadevehiculo()
        self.Ventanadevehiculo.show()          
    def navego_rep(self):
        self.close()
        self.VentanadeRepuestos=VentanadeRepuestos()
        self.VentanadeRepuestos.show()
    def navego_prin(self):
        self.close()
        self.VentanadePrincipal=VentanadePrincipal()
        self.VentanadePrincipal.show() 
    def navego_man(self):
        self.close()
        self.VentanaOrden=VentanaOrden()
        self.VentanaOrden.show()
    def navego_ing(self):
        self.close()
        self.VentanadeInicio=VentanadeInicio()
        self.VentanadeInicio.show()

class VentanadeRepuestos(QMainWindow):
    def __init__(self):
        super(VentanadeRepuestos, self).__init__()
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\QtWindows&Icons\d_repuestos.ui",self)
        #Base de datos
        self.base_datos = Comunicacion()

        #Botones Superiores
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_colapsar.clicked.connect(self.control_bt_normal)
        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.piv_col=0 
        self.piv_nav=0 

        #Eliminar barra de titulo y opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #SizeGrip
        self.gripSize=10
        self.grip=QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize,self.gripSize)

        # Ancho de columna adaptable
        self.tabla_pgElim_OT.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_pgBD_OT.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        #Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
                
        #Botones Navegar
        self.bt_nav_tra.clicked.connect(self.navego_tra)
        self.bt_nav_veh.clicked.connect(self.navego_veh)
        self.bt_nav_rep.clicked.connect(self.navego_rep)
        self.bt_nav_prin.clicked.connect(self.navego_prin)
        self.bt_nav_man.clicked.connect(self.navego_man)
        self.bt_ingreso.clicked.connect(self.navego_ing)
        

    def control_bt_minimizar(self):
        self.showMinimized()
    def control_bt_normal(self):
        if self.piv_col ==0:
            self.showNormal()
            self.piv_col=1
        else:
            self.showMaximized()
            self.piv_col=0
    def control_bt_maximizar(self):
        self.showMaximized()
    # SizeGrip

    def resizeEvent(self,event):
        rect=self.rect()
        self.grip.move(rect.right()-self.gripSize,rect.bottom()-self.gripSize)
    # Mover ventana
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
    
    def mover_navegar(self):
        if True:
            rect = self.frame_navegar.geometry()
            normal = QtCore.QRect(1, 108, rect.width(), 0)
            extender = QtCore.QRect(1, 108, rect.width(), 64)
            print(rect,",",normal,",",extender)
            if rect == normal:
                endRect = extender
            else:
                endRect = normal
            #print(rect,",",endRect)
            self.animacion = QPropertyAnimation(self.frame_navegar, b"geometry")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(rect)
            self.animacion.setEndValue(endRect)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
    #Botones de Navegar
    def navego_tra(self):
        self.close()
        self.VentanadeTrabajos=VentanadeTrabajos()
        self.VentanadeTrabajos.show()
    def navego_veh(self):
        self.close()
        self.Ventanadevehiculo=Ventanadevehiculo()
        self.Ventanadevehiculo.show()          
    def navego_rep(self):
        self.close()
        self.VentanadeRepuestos=VentanadeRepuestos()
        self.VentanadeRepuestos.show()
    def navego_prin(self):
        self.close()
        self.VentanadePrincipal=VentanadePrincipal()
        self.VentanadePrincipal.show() 
    def navego_man(self):
        self.close()
        self.VentanaOrden=VentanaOrden()
        self.VentanaOrden.show()
    def navego_ing(self):
        self.close()
        self.VentanadeInicio=VentanadeInicio()
        self.VentanadeInicio.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanadeInicio()
    mi_app.show()
    app.exec_()