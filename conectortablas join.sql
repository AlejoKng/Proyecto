UPDATE registro_mantenimiento 
        JOIN vehiculos ON registro_mantenimiento.Placa = vehiculos.Placa 
        JOIN trabajos ON registro_mantenimiento.Trabajo = trabajos.Trabajo 
        JOIN repuestos ON registro_mantenimiento.Repuesto = repuestos.Repuesto 
        SET  registro_mantenimiento.Placa ='JKL012' 
        , registro_mantenimiento.Trabajo = 'Cambio de bujías', registro_mantenimiento.Repuesto = 'Cables de bujía'
        WHERE Consecutivo_orden = 6;