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
        loadUi("C:\Escritorio\DAVID\VS_Code\Proyecto\Proyecto\.ui",self)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())