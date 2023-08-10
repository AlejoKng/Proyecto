import sys
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve,QStringListModel,Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView,QCompleter,QListView,QProxyStyle
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
        user =self.txb_usuario.text()
        contra =self.txb_contra.text()
        self.comp=self.base_datos.verif_user(user)
        #print(contra,"=",self.comp)
        if(self.comp==contra):
            self.close()
            self.VentanaOrden=VentanadePrincipal()
            self.VentanaOrden.show()

class VentanadePrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\QtWindows&Icons\d_principal.ui",self)

        #Base de datos
        self.base_datos = Comunicacion()

        #Botones Superiores
        self.bt_menu.clicked.connect(self.mover_menu)
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
        # Configurar el completer
        self.completervehi = QCompleter()
        self.completervehi.setCaseSensitivity(False)  # No distinguir mayúsculas de minúsculas
        self.completervehi.setModelSorting(QCompleter.CaseInsensitivelySortedModel)  # Ordenar insensible a mayúsculas/minúsculas
        self.completervehi.setFilterMode(Qt.MatchContains)
        # 1. Obtener la lista de opciones para el completer
        # 2. Establecer la lista de opciones en el completer
        # 3. Asignar el completer al QLineEdit
        opciones = self.base_datos.trae_vehi()
        self.completervehi.setModel(QtCore.QStringListModel(opciones))
        self.tBox_pgAkm_Pla.setCompleter(self.completervehi)

        # Botones en la Pagina
        self.bt_pgAkm_Cons.clicked.connect(self.mostrar_odo)
        self.bt_pgElim_save.clicked.connect(self.modificar_odo)

        

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
    
    # Funciones de pagina
    def mostrar_odo(self):
        Placa=self.tBox_pgAkm_Pla.text().upper()
        Placa=str(Placa)
        self.consulta=self.base_datos.base_ODO(Placa)
        datos=self.base_datos.todo_base_ODO()
        i=len(datos)
        self.tabla_pgAkm_Km.setRowCount(i)
        tablerow=0
        for row in datos:
            self.tabla_pgAkm_Km.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_pgAkm_Km.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1].strftime("%d-%m-%Y")))
            self.tabla_pgAkm_Km.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            tablerow+=1
        if (len(self.consulta)!=0):
            self.tBox_pgAkm_Fec.setText(self.consulta[0][1].strftime("%Y-%m-%d"))
            self.tBox_pgAkm_Km.setText(str(self.consulta[0][2]))

    def modificar_odo(self):
        Placa =self.tBox_pgAkm_Pla.text().upper()
        Fecha = self.tBox_pgAkm_Fec.text()
        Kilometraje = int(self.tBox_pgAkm_Km.text().upper())
        if Placa!='' and Fecha!='' and Kilometraje!='':
            self.base_datos.modificar_ODO(Placa,Fecha, Kilometraje)
            Placa =self.tBox_pgAkm_Pla.clear()
            Fecha =self.tBox_pgAkm_Fec.clear()
            Kilometraje =self.tBox_pgAkm_Km.clear()
        datos=self.base_datos.todo_base_ODO()
        i=len(datos)
        self.tabla_pgAkm_Km.setRowCount(i)
        tablerow=0
        for row in datos:
            self.tabla_pgAkm_Km.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_pgAkm_Km.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1].strftime("%d-%m-%Y")))
            self.tabla_pgAkm_Km.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            tablerow+=1


class VentanaOrden(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\QtWindows&Icons\d_ot.ui",self)

        #Base de datos
        self.base_datos = Comunicacion()

        #Botones Superiores
        self.bt_menu.clicked.connect(self.mover_menu)
        self.bt_naveg.clicked.connect(self.mover_navegar)
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
        self.table_pgPro_Vh.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
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
        # Configurar el completer
        self.completertrab = QCompleter()
        self.completertrab.setCaseSensitivity(False)  # No distinguir mayúsculas de minúsculas
        self.completertrab.setModelSorting(QCompleter.CaseInsensitivelySortedModel)  # Ordenar insensible a mayúsculas/minúsculas
        self.completertrab.setFilterMode(Qt.MatchContains)
        # 1. Obtener la lista de opciones para el completer
        # 2. Establecer la lista de opciones en el completer
        # 3. Asignar el completer al QLineEdit
        opciones = self.base_datos.trae_trab()
        self.completertrab.setModel(QtCore.QStringListModel(opciones))
        self.cBox_pgReg_Tra.setCompleter(self.completertrab)
        self.cBox_pgMod_Tra.setCompleter(self.completertrab)
        # Configurar el completer
        self.completerrepu = QCompleter()
        self.completerrepu.setCaseSensitivity(False)  # No distinguir mayúsculas de minúsculas
        self.completerrepu.setModelSorting(QCompleter.CaseInsensitivelySortedModel)  # Ordenar insensible a mayúsculas/minúsculas
        self.completerrepu.setFilterMode(Qt.MatchContains)
        # 1. Obtener la lista de opciones para el completer
        # 2. Establecer la lista de opciones en el completer
        # 3. Asignar el completer al QLineEdit
        opciones = self.base_datos.trae_repu()
        self.completerrepu.setModel(QtCore.QStringListModel(opciones))
        self.cBox_pgReg_Rep.setCompleter(self.completerrepu)
        self.cBox_pgMod_Rep.setCompleter(self.completerrepu)
        # Configurar el completer
        self.completervehi = QCompleter()
        self.completervehi.setCaseSensitivity(False)  # No distinguir mayúsculas de minúsculas
        self.completervehi.setModelSorting(QCompleter.CaseInsensitivelySortedModel)  # Ordenar insensible a mayúsculas/minúsculas
        self.completervehi.setFilterMode(Qt.MatchContains)
        # 1. Obtener la lista de opciones para el completer
        # 2. Establecer la lista de opciones en el completer
        # 3. Asignar el completer al QLineEdit
        opciones = self.base_datos.trae_vehi()
        self.completervehi.setModel(QtCore.QStringListModel(opciones))
        self.tBox_pgReg_Con.setCompleter(self.completervehi)
        self.tBox_pgMod_Pla.setCompleter(self.completervehi)


        # Conexiones por pagina
        # Pagina Base de Datos
        self.bt_database.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_base_datos))
        # Botones en la Pagina
        self.bt_pgBD_refrescar.clicked.connect(self.mostrar_base)
        
        # Pagina Registro de Mantenimiento
        self.bt_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
        # Botones en la Pagina
        self.bt_pgReg_save.clicked.connect(self.registrar_mantenimiento)

        # Pagina Modificar Mantenimiento
        self.bt_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_modificar))
        # Botones en la Pagina
        self.bt_pgMod_Act.clicked.connect(self.modificar_mante)
        self.bt_pgMod_Con.clicked.connect(self.actualizar_mante)

        # Pagina Eliminar de Mantenimiento
        self.bt_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        # Botones en la Pagina
        self.bt_pgElim_Con.clicked.connect(self.consulElim_mante)
        self.bt_pgElim_Save.clicked.connect(self.eliminar_mante)


        # Pagina de Programacion de Mantenimiento
        self.bt_programacion.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_program))
        self.bt_programacion.clicked.connect(self.todo_base_PRO)
        
        
        

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
            #print(rect,",",normal,",",extender)
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
        #print(datos)
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
            #print(self.orden[0][1])
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
    def consulElim_mante(self):
        consulta=self.tBox_pgElim_Con.text().upper()
        consulta=str(consulta)
        datos=self.base_datos.base_un_filtro(consulta)
        i=len(datos)
        self.tabla_pgElim_OT.setRowCount(i)
        tablerow=0
        for row in datos:
            self.tabla_pgElim_OT.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_pgElim_OT.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_pgElim_OT.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[1].strftime("%d-%m-%Y")))
            self.tabla_pgElim_OT.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_pgElim_OT.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[4]))
            self.tabla_pgElim_OT.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[5]))
            tablerow+=1


    def eliminar_mante(self):
        consulta=self.tBox_pgElim_Con.text()
        if consulta!='':
            self.base_datos.eliminar_mante(consulta)
            self.lb_pgElim_Save.setText('Mantenimiento Eliminado')
            consulta=self.tBox_pgElim_Con.text().upper()
            consulta=str(consulta)
            datos=self.base_datos.base_un_filtro(consulta)
            i=len(datos)
            self.tabla_pgElim_OT.setRowCount(i)
            tablerow=0
            for row in datos:
                self.tabla_pgElim_OT.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabla_pgElim_OT.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[2])))
                self.tabla_pgElim_OT.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[1].strftime("%d-%m-%Y")))
                self.tabla_pgElim_OT.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[3]))
                self.tabla_pgElim_OT.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[4]))
                self.tabla_pgElim_OT.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[5]))
                tablerow+=1
    ######    PAGINA PROGRAMA   ######
    def todo_base_PRO(self):
        datos=self.base_datos.todo_base_PRO()
        i=len(datos)
        #print(datos)
        self.table_pgPro_Vh.setRowCount(i)
        tablerow=0
        for row in datos:
            self.table_pgPro_Vh.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.table_pgPro_Vh.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.table_pgPro_Vh.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.table_pgPro_Vh.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))

            tablerow+=1
    
    
        
class VentanadeTrabajos(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\QtWindows&Icons\d_trabajos.ui",self)

        #Base de datos
        self.base_datos = Comunicacion()

        #Botones Superiores
        self.bt_menu.clicked.connect(self.mover_menu)
        self.bt_naveg.clicked.connect(self.mover_navegar)
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
        self.tabla_pgBD_OT.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_pgElim_OT.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        #Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
                
        #Botones Navegar
        self.bt_nav_tra.clicked.connect(self.navego_tra)
        self.bt_nav_veh.clicked.connect(self.navego_veh)
        self.bt_nav_rep.clicked.connect(self.navego_rep)
        self.bt_nav_prin.clicked.connect(self.navego_prin)
        self.bt_nav_man.clicked.connect(self.navego_man)
        self.bt_ingreso.clicked.connect(self.navego_ing)
        
        # Configurar el completer
        self.completertrab = QCompleter()
        self.completertrab.setCaseSensitivity(False)  # No distinguir mayúsculas de minúsculas
        self.completertrab.setModelSorting(QCompleter.CaseInsensitivelySortedModel)  # Ordenar insensible a mayúsculas/minúsculas
        self.completertrab.setFilterMode(Qt.MatchContains)
        # 1. Obtener la lista de opciones para el completer
        # 2. Establecer la lista de opciones en el completer
        # 3. Asignar el completer al QLineEdit
        opciones = self.base_datos.trae_trab()
        self.completertrab.setModel(QtCore.QStringListModel(opciones))
        self.tBox_pgMod_Con.setCompleter(self.completertrab)
        self.tBox_pgElim_Con.setCompleter(self.completertrab)


        # Conexiones por pagina tBox_pgMod_Con
        # Pagina Base de Datos (page_base_datos)
        self.bt_database.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_base_datos))
        # Botones en la Pagina
        self.bt_pgBD_Act.clicked.connect(self.mostrar_base)
        
        # Pagina Registro de Trabajo (page_registrar)
        self.bt_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
        # Botones en la Pagina
        self.bt_pgReg_Save.clicked.connect(self.registrar_trabajo)
        
        # Pagina Modificar Trabajo (page_actualizar)
        self.bt_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        # Botones en la Pagina
        self.bt_pgMod_Con.clicked.connect(self.actualizar_trab)
        self.bt_pgMod_Save.clicked.connect(self.modificar_trab)
        self.bt_pgMod_Save.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))

        
        # Pagina Eliminar de Trabajo (page_eliminar)
        self.bt_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        # Botones en la Pagina
        self.bt_pgElim_Con.clicked.connect(self.consulElim_tra)
        self.bt_pgElim_Save.clicked.connect(self.eliminar_tra)
        
        

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
            #print(rect,",",normal,",",extender)
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
    
    
    
    ######    PAGINA BASEDATOS   ######
    def mostrar_base(self):
        datos=self.base_datos.mostrar_base_trabajos()
        i=len(datos)
        #print(datos)
        self.tabla_pgBD_OT.setRowCount(i)
        tablerow=0
        for row in datos:
            self.tabla_pgBD_OT.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_pgBD_OT.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_pgBD_OT.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            tablerow+=1
    ######    PAGINA REGISTRO   ######
    def registrar_trabajo(self):
        trabajo =self.tBox_pgReg_Tra.text()
        tipo = self.tBox_pgReg_Tip.text()
        periodicidad = int(self.tBox_pgReg_Per.text().upper())
        if trabajo!='' and tipo!='' and periodicidad!='':
            self.base_datos.registrar_trabajo( trabajo, tipo, periodicidad)
            self.lb_pgReg_Save.setText('Mantenimiento Registrado')
            trabajo =self.tBox_pgReg_Tra.clear()
            tipo =self.tBox_pgReg_Tip.clear()
            periodicidad =self.tBox_pgReg_Per.clear()
        else:
            self.lb_pgReg_Save.setText('Hay Espacios Vacios')

    ######      PAGINA MODIFICAR        ######

    def modificar_trab(self):
        consulta=self.tBox_pgMod_Plac.text()
        consulta=str(consulta)
        self.orden=self.base_datos.buscar_vh(consulta)
        if (len(self.orden)!=0):
            #print(self.orden[0][1])
            self.tBox_pgMod_Pla.setText(str(self.orden[0][0]))
            self.tBox_pgMod_Con.setText(str(self.orden[0][1]))
            self.tBox_pgMod_Mar.setText(str(self.orden[0][2]))
            self.tBox_pgMod_Km.setText(int(str(self.orden[0][2])))

        else:
            self.label_14.setText('Dato no encontrado')
        
    def actualizar_trab(self):
        trabajo =self.tBox_pgMod_Con.text()
        nuevotrabajo =self.tBox_pgAct_Nom.text()
        tipo = self.tBox_pgAct_Tip.text()
        periodicidad = int(self.tBox_pgAct_Per.text().upper())
        if trabajo!='' and nuevotrabajo!='' and tipo!='' and periodicidad!='':
            self.base_datos.actualizar_trab( nuevotrabajo, tipo, periodicidad,trabajo)
            self.lb_pgMod_Signal.setText('Trabajo Registrado')
            var=self.tBox_pgAct_Nom.text()

            self.tBox_pgMod_Con.setText(str(var))
            nuevotrabajo =self.tBox_pgAct_Nom.clear()
            tipo =self.tBox_pgAct_Tip.clear()
            periodicidad =self.tBox_pgAct_Per.clear()
        else:
            self.lb_pgMod_Signal.setText('Hay Espacios Vacios')
    ######    PAGINA ELIMINAR   ######
    def consulElim_tra(self):
        consulta=self.tBox_pgElim_Con.text()
        consulta=str(consulta)
        datos=self.base_datos.buscar_trab(consulta)
        i=len(datos)
        self.tabla_pgElim_OT.setRowCount(i)
        tablerow=0
        for row in datos:
            self.tabla_pgElim_OT.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_pgElim_OT.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_pgElim_OT.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            tablerow+=1

    def eliminar_tra(self):
        consulta=str(self.tBox_pgElim_Con.text())
        if consulta!='':
            self.base_datos.eliminar_trabajo1(consulta)
            self.label_23.setText('Trabajo Eliminado')
            consulta=self.tBox_pgElim_Con.text()
        consulta=str(consulta)
        datos=self.base_datos.buscar_trab(consulta)
        i=len(datos)
        self.tabla_pgElim_OT.setRowCount(i)
        tablerow=0
        for row in datos:
            self.tabla_pgElim_OT.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_pgElim_OT.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_pgElim_OT.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            tablerow+=1
        

class Ventanadevehiculo(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\QtWindows&Icons\d_vh.ui",self)
        
        #Base de datos
        self.base_datos = Comunicacion()

        #Botones Superiores
        self.bt_menu.clicked.connect(self.mover_menu)
        self.bt_naveg.clicked.connect(self.mover_navegar)
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
        self.tabla_pgBD_OT.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_pgElim_OT.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        #Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
                
        #Botones Navegar
        self.bt_nav_tra.clicked.connect(self.navego_tra)
        self.bt_nav_veh.clicked.connect(self.navego_veh)
        self.bt_nav_rep.clicked.connect(self.navego_rep)
        self.bt_nav_prin.clicked.connect(self.navego_prin)
        self.bt_nav_man.clicked.connect(self.navego_man)
        self.bt_ingreso.clicked.connect(self.navego_ing)
        
       # Configurar el completer
        self.completervehi = QCompleter()
        self.completervehi.setCaseSensitivity(False)  # No distinguir mayúsculas de minúsculas
        self.completervehi.setModelSorting(QCompleter.CaseInsensitivelySortedModel)  # Ordenar insensible a mayúsculas/minúsculas
        self.completervehi.setFilterMode(Qt.MatchContains)
        # 1. Obtener la lista de opciones para el completer
        # 2. Establecer la lista de opciones en el completer
        # 3. Asignar el completer al QLineEdit
        opciones = self.base_datos.trae_vehi()
        self.completervehi.setModel(QtCore.QStringListModel(opciones))
        self.tBox_pgReg_Pla.setCompleter(self.completervehi)
        self.tBox_pgMod_Plac.setCompleter(self.completervehi)
        self.tBox_pgElim_Con.setCompleter(self.completervehi)
        


        # Conexiones por pagina tBox_pgMod_Con
        # Pagina Base de Datos (page_base_datos)
        self.bt_database.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_base_datos))
        # Botones en la Pagina
        self.bt_pgBD_Ref.clicked.connect(self.mostrar_base)
        
        # Pagina Registro de Trabajo (page_registrar)
        self.bt_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
        # Botones en la Pagina
        self.bt_pgReg_Save.clicked.connect(self.registrar_trabajo)
        
        # Pagina Modificar Trabajo (page_actualizar)
        self.bt_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        # Botones en la Pagina
        self.bt_pgMod_Pla.clicked.connect(self.modificar_trab)
        self.bt_pgMod_Save.clicked.connect(self.actualizar_trab)
        self.bt_pgMod_Save.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))

        
        # Pagina Eliminar de Trabajo (page_eliminar)
        self.bt_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        # Botones en la Pagina
        self.bt_pgElim_Con.clicked.connect(self.consulElim_tra)
        self.bt_pgElim_Save.clicked.connect(self.eliminar_tra)
        
        

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
            #print(rect,",",normal,",",extender)
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
    
    
    ######    PAGINA BASEDATOS   ######
    def mostrar_base(self):
        datos=self.base_datos.mostrar_base_vehiculos()
        i=len(datos)
        print(datos)
        self.tabla_pgBD_OT.setRowCount(i)
        tablerow=0
        for row in datos:
            self.tabla_pgBD_OT.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_pgBD_OT.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_pgBD_OT.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_pgBD_OT.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow+=1
    ######    PAGINA REGISTRO   ######
    def registrar_trabajo(self):
        placa =self.tBox_pgReg_Pla.text().upper()
        marca = self.tBox_pgReg_Mar.text()
        conductor = self.tBox_pgReg_Cond.text()
        kilometraje = int(self.tBox_pgReg_Km.text().upper())
        if placa!='' and marca!='' and conductor!=''and kilometraje!='':
            self.base_datos.registrar_vehiculo( placa, marca, conductor, kilometraje)
            self.lb_pgReg_Save.setText('Vehiculo Registrado')
            placa =self.tBox_pgReg_Pla.clear()
            marca = self.tBox_pgReg_Mar.clear()
            conductor = self.tBox_pgReg_Cond.clear()
            kilometraje = self.tBox_pgReg_Km.clear()
        else:
            self.lb_pgReg_Save.setText('Hay Espacios Vacios')

    ######      PAGINA MODIFICAR        ######

    def modificar_trab(self):
        consulta=self.tBox_pgMod_Con.text()
        consulta=str(consulta)
        self.orden=self.base_datos.buscar_trab(consulta)
        if (len(self.orden)!=0):
            #print(self.orden[0][1])
            self.tBox_pgAct_Nom.setText(str(self.orden[0][0]))
            self.tBox_pgAct_Tip.setText(str(self.orden[0][1]))
            self.tBox_pgAct_Per.setText(str(self.orden[0][2]))

        else:
            self.lb_pgMod_Signal.setText('Dato no encontrado')
        
    def actualizar_trab(self):
        trabajo =self.tBox_pgMod_Con.text()
        nuevotrabajo =self.tBox_pgAct_Nom.text()
        tipo = self.tBox_pgAct_Tip.text()
        periodicidad = int(self.tBox_pgAct_Per.text().upper())
        if trabajo!='' and nuevotrabajo!='' and tipo!='' and periodicidad!='':
            self.base_datos.actualizar_trab( nuevotrabajo, tipo, periodicidad,trabajo)
            self.lb_pgMod_Signal.setText('Trabajo Registrado')
            var=self.tBox_pgAct_Nom.text()

            self.tBox_pgMod_Con.setText(str(var))
            nuevotrabajo =self.tBox_pgAct_Nom.clear()
            tipo =self.tBox_pgAct_Tip.clear()
            periodicidad =self.tBox_pgAct_Per.clear()
        else:
            self.lb_pgMod_Signal.setText('Hay Espacios Vacios')
    ######    PAGINA ELIMINAR   ######
    def consulElim_tra(self):
        consulta=self.tBox_pgElim_Con.text()
        consulta=str(consulta)
        datos=self.base_datos.buscar_trab(consulta)
        i=len(datos)
        self.tabla_pgElim_OT.setRowCount(i)
        tablerow=0
        for row in datos:
            self.tabla_pgElim_OT.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_pgElim_OT.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_pgElim_OT.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            tablerow+=1

    def eliminar_tra(self):
        consulta=str(self.tBox_pgElim_Con.text())
        if consulta!='':
            self.base_datos.eliminar_trabajo1(consulta)
            self.label_23.setText('Trabajo Eliminado')
            consulta=self.tBox_pgElim_Con.text()
        consulta=str(consulta)
        datos=self.base_datos.buscar_trab(consulta)
        i=len(datos)
        self.tabla_pgElim_OT.setRowCount(i)
        tablerow=0
        for row in datos:
            self.tabla_pgElim_OT.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_pgElim_OT.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_pgElim_OT.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            tablerow+=1
        

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