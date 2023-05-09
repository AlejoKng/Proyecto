import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from PyQt5 import uic
from conexion_sqlite import Comunicacion

class Desarrollo():
    def __init__(self):
        super(Desarrollo, self).__init__()
        
        

    class VentanadeInicio(QMainWindow):
        def __init__(self):
            uic.loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\QtWindows&Icons\d_ingreso.ui",self)

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        mi_app = VentanadeInicio()
        mi_app.show()
        app.exec_()
        
if __name__ == "__main__":
    Desarrollo()