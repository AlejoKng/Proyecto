def registrar_mantenimiento(self):
    codigo =self.txb_pgReg_cod.text().upper()
    nombre =self.txb_pgReg_fech.text().upper()
    modelo =self.txb_pgReg_km.text().upper()
    precio =self.txb_pgReg_rep.text().upper()
    cantidad =self.txb_pgReg_trab.text().upper()
    if codigo!='' and nombre!='' and modelo!='' and cantidad!='' and precio!='':
        self.base_datos.registrar_mantenimiento(codigo,nombre,modelo,precio,cantidad)
        self.signal_registrar.setText('Productos Registrados')
        codigo =self.txb_pgReg_cod.clear()
        nombre =self.txb_pgReg_fech.clear()
        modelo =self.txb_pgReg_km.clear()
        precio =self.txb_pgReg_rep.tclear()
        cantidad =self.txb_pgReg_trab.clear()
    else:
        self.label_8.setText('Hay Espacios Vacios')