DROP DATABASE IF exists myEngineBase;
CREATE DATABASE myEngineBase;
USE myEngineBase;

CREATE TABLE usuarios ( 
  user_name VARCHAR(255) NOT NULL PRIMARY KEY, 
  password VARCHAR(255) NOT NULL 
);

CREATE TABLE vehiculos ( 
  Placa VARCHAR(10) NOT NULL PRIMARY KEY, 
  Conductor VARCHAR(255) NOT NULL, 
  Marca VARCHAR(255) NOT NULL, 
  Kilometraje INT NOT NULL 
);

CREATE TABLE repuestos ( 
  Repuesto VARCHAR(255) NOT NULL PRIMARY KEY, 
  Marca VARCHAR(255) NOT NULL, 
  Proveedor VARCHAR(255) NOT NULL 
);

CREATE TABLE trabajos ( 
  Trabajo VARCHAR(255) NOT NULL PRIMARY KEY, 
  Tipo_mantenimiento VARCHAR(255) NOT NULL, 
  Periodicidad INT NOT NULL 
);

CREATE TABLE registro_mantenimiento ( 
  Consecutivo_orden INT NOT NULL AUTO_INCREMENT PRIMARY KEY , 
  Fecha DATE NOT NULL, 
  Kilometraje INT NOT NULL, 
  Trabajo VARCHAR(255) NOT NULL, 
  Repuesto VARCHAR(255) NOT NULL, 
  Placa VARCHAR(10) NOT NULL, 
  FOREIGN KEY (Repuesto) REFERENCES repuestos(Repuesto) ON DELETE CASCADE ON UPDATE CASCADE, 
  FOREIGN KEY (Trabajo) REFERENCES trabajos(Trabajo) ON DELETE CASCADE ON UPDATE CASCADE, 
  FOREIGN KEY (Placa) REFERENCES vehiculos(Placa) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE odometro ( 
  Placa VARCHAR(10) NOT NULL PRIMARY KEY , 
  Fecha DATE NOT NULL, 
  Kilometraje INT NOT NULL,
  FOREIGN KEY (Placa) REFERENCES vehiculos(Placa) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE programacion_mantenimiento (
  Consecutivo_orden INT NOT NULL,
  Placa VARCHAR(10) NOT NULL,
  Trabajo VARCHAR(255) NOT NULL,
  Proximo_mantenimiento_km INT NOT NULL,
  FOREIGN KEY (Placa) REFERENCES vehiculos(Placa) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Trabajo) REFERENCES trabajos(Trabajo) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Consecutivo_orden) REFERENCES registro_mantenimiento(Consecutivo_orden) ON DELETE CASCADE ON UPDATE CASCADE
);

DELIMITER //

CREATE TRIGGER actualizar_kilometraje AFTER INSERT ON registro_mantenimiento
FOR EACH ROW
BEGIN
  UPDATE vehiculos
  SET Kilometraje = NEW.Kilometraje
  WHERE Placa = NEW.Placa;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER actualizar_kilometraje_vh AFTER INSERT ON registro_mantenimiento
FOR EACH ROW
BEGIN
  UPDATE odometro
  SET Kilometraje = NEW.Kilometraje
  WHERE Placa = NEW.Placa;
END //

DELIMITER ;


INSERT INTO usuarios (user_name, password)VALUES ('user5', 'password5');
INSERT INTO usuarios (user_name, password)VALUES ('1234', '1234');
INSERT INTO usuarios (user_name, password) VALUES ('user2', 'password2');
INSERT INTO usuarios (user_name, password) VALUES ('user3', 'password3');
INSERT INTO usuarios (user_name, password) VALUES ('user4', 'password4');

INSERT INTO repuestos (Repuesto, Marca, Proveedor) VALUES ('Filtro de aceite', 'Fram', 'Distribuidora ABC');
INSERT INTO repuestos (Repuesto, Marca, Proveedor) VALUES ('Pastillas de freno', 'Bosch', 'Distribuidora XYZ');
INSERT INTO repuestos (Repuesto, Marca, Proveedor) VALUES ('Bujías', 'NGK', 'Distribuidora LMN');
INSERT INTO repuestos (Repuesto, Marca, Proveedor) VALUES ('Amortiguadores', 'Monroe', 'Distribuidora EFG');
INSERT INTO repuestos (Repuesto, Marca, Proveedor) VALUES ('Cables de bujía', 'NGK', 'Distribuidora HIJ');

INSERT INTO vehiculos (Placa, Conductor, Marca, Kilometraje) VALUES ('ABC123', 'Juan Perez', 'Toyota', 50000);
INSERT INTO vehiculos (Placa, Conductor, Marca, Kilometraje) VALUES ('STT011', 'Maria Gomez', 'Chevrolet', 47000);
INSERT INTO vehiculos (Placa, Conductor, Marca, Kilometraje) VALUES ('STT030', 'Pedro Hernandez', 'Ford', 45000);
INSERT INTO vehiculos (Placa, Conductor, Marca, Kilometraje) VALUES ('TEK242', 'Ana Rodriguez', 'Honda', 42000);
INSERT INTO vehiculos (Placa, Conductor, Marca, Kilometraje) VALUES ('TTX602', 'Luisa Martinez', 'Nissan', 39000);

INSERT INTO trabajos (Trabajo, Tipo_mantenimiento, Periodicidad) VALUES ('Cambio de aceite', 'Preventivo', 5000);
INSERT INTO trabajos (Trabajo, Tipo_mantenimiento, Periodicidad) VALUES ('Alineación y balanceo', 'Correctivo', 10000);
INSERT INTO trabajos (Trabajo, Tipo_mantenimiento, Periodicidad) VALUES ('Cambio de frenos', 'Correctivo', 20000);
INSERT INTO trabajos (Trabajo, Tipo_mantenimiento, Periodicidad) VALUES ('Cambio de filtros', 'Preventivo', 10000);
INSERT INTO trabajos (Trabajo, Tipo_mantenimiento, Periodicidad) VALUES ('Cambio de bujías', 'Preventivo', 40000);

INSERT INTO odometro (Placa, Fecha, Kilometraje) VALUES ('ABC123', '2023-05-16', 1000);
INSERT INTO odometro (Placa, Fecha, Kilometraje) VALUES ('TTX602', '2023-05-16', 1000);
INSERT INTO odometro (Placa, Fecha, Kilometraje) VALUES ('TEK242', '2023-05-16', 1000);
INSERT INTO odometro (Placa, Fecha, Kilometraje) VALUES ('STT011', '2023-05-16', 1000);
INSERT INTO odometro (Placa, Fecha, Kilometraje) VALUES ('STT030', '2023-05-16', 1000);

INSERT INTO registro_mantenimiento (Fecha, Kilometraje, Trabajo, Repuesto, Placa) VALUES ('2022-03-01', 20000, 'Cambio de aceite', 'Filtro de aceite', 'ABC123');
INSERT INTO registro_mantenimiento (Fecha, Kilometraje, Trabajo, Repuesto, Placa) VALUES ('2023-03-28', 9000, 'Cambio de bujías', 'Bujías', 'ABC123');
INSERT INTO registro_mantenimiento (Fecha, Kilometraje, Trabajo, Repuesto, Placa) VALUES ('2023-04-15', 9500, 'Cambio de frenos', 'Pastillas de freno', 'STT011');
INSERT INTO registro_mantenimiento (Fecha, Kilometraje, Trabajo, Repuesto, Placa) VALUES ('2023-02-14', 8000, 'Cambio de filtros', 'Amortiguadores', 'STT011');
INSERT INTO registro_mantenimiento (Fecha, Kilometraje, Trabajo, Repuesto, Placa) VALUES ('2023-01-30', 7500, 'Cambio de bujías', 'Cables de bujía', 'STT030');


/*
INSERT INTO programacion_mantenimiento (Consecutivo_orden, Placa, Trabajo, Proximo_mantenimiento_km)
SELECT r.Consecutivo_orden, v.Placa, t.Trabajo, r.Kilometraje + t.Periodicidad
FROM vehiculos v
JOIN registro_mantenimiento r ON v.Placa = r.Placa
JOIN trabajos t ON r.Trabajo = t.Trabajo
LEFT JOIN programacion_mantenimiento p ON r.Consecutivo_orden = p.Consecutivo_orden
WHERE p.Consecutivo_orden IS NULL OR r.Kilometraje + t.Periodicidad > p.Proximo_mantenimiento_km;
*/
-- SELECT * FROM myenginebase.programacion_mantenimiento ORDER BY Consecutivo_orden DESC;
-- DELETE FROM vehiculos WHERE Placa = 'ABC123';
-- UPDATE trabajos SET Trabajo="Cambio de aceite 15w40", Periodicidad=10000 WHERE Trabajo="Cambio de aceite";
/*
Este es un comentario
de múltiples líneas
en SQL
*/
