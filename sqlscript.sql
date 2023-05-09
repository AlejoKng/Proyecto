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
  Periodicidad VARCHAR(255) NOT NULL 
);

CREATE TABLE registro_mantenimiento ( 
  Consecutivo_orden INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
  Fecha DATE NOT NULL, 
  Kilometraje INT NOT NULL, 
  Trabajo VARCHAR(255) NOT NULL, 
  Repuesto VARCHAR(255) NOT NULL, 
  Placa VARCHAR(10) NOT NULL, 
  FOREIGN KEY (Repuesto) REFERENCES repuestos(Repuesto), 
  FOREIGN KEY (Trabajo) REFERENCES trabajos(Trabajo), 
  FOREIGN KEY (Placa) REFERENCES vehiculos(Placa) 
);

INSERT INTO usuarios (user_name, password) 
VALUES ('user5', 'password5');

INSERT INTO usuarios (user_name, password)VALUES ('user1', 'password1');

INSERT INTO usuarios (user_name, password) VALUES ('user2', 'password2');

INSERT INTO usuarios (user_name, password) VALUES ('user3', 'password3');

INSERT INTO usuarios (user_name, password) VALUES ('user4', 'password4');

INSERT INTO repuestos (Repuesto, Marca, Proveedor) VALUES ('Filtro de aceite', 'Fram', 'Distribuidora ABC');

INSERT INTO repuestos (Repuesto, Marca, Proveedor) VALUES ('Pastillas de freno', 'Bosch', 'Distribuidora XYZ');

INSERT INTO repuestos (Repuesto, Marca, Proveedor) VALUES ('Bujías', 'NGK', 'Distribuidora LMN');

INSERT INTO repuestos (Repuesto, Marca, Proveedor) VALUES ('Amortiguadores', 'Monroe', 'Distribuidora EFG');

INSERT INTO repuestos (Repuesto, Marca, Proveedor) VALUES ('Cables de bujía', 'NGK', 'Distribuidora HIJ');

INSERT INTO vehiculos (Placa, Conductor, Marca, Kilometraje) VALUES ('ABC123', 'Juan Perez', 'Toyota', 50000);

INSERT INTO vehiculos (Placa, Conductor, Marca, Kilometraje) VALUES ('DEF456', 'Maria Gomez', 'Chevrolet', 47000);

INSERT INTO vehiculos (Placa, Conductor, Marca, Kilometraje) VALUES ('GHI789', 'Pedro Hernandez', 'Ford', 45000);

INSERT INTO vehiculos (Placa, Conductor, Marca, Kilometraje) VALUES ('JKL012', 'Ana Rodriguez', 'Honda', 42000);

INSERT INTO vehiculos (Placa, Conductor, Marca, Kilometraje) VALUES ('MNO345', 'Luisa Martinez', 'Nissan', 39000);

INSERT INTO trabajos (Trabajo, Tipo_mantenimiento, Periodicidad) VALUES ('Cambio de aceite', 'Preventivo', 'Cada 5,000 km');

INSERT INTO trabajos (Trabajo, Tipo_mantenimiento, Periodicidad) VALUES ('Alineación y balanceo', 'Correctivo', 'Cada 10,000 km');

INSERT INTO trabajos (Trabajo, Tipo_mantenimiento, Periodicidad) VALUES ('Cambio de frenos', 'Correctivo', 'Cada 20,000 km');

INSERT INTO trabajos (Trabajo, Tipo_mantenimiento, Periodicidad) VALUES ('Cambio de filtros', 'Preventivo', 'Cada 10,000 km');

INSERT INTO trabajos (Trabajo, Tipo_mantenimiento, Periodicidad) VALUES ('Cambio de bujías', 'Preventivo', 'Cada 40,000 km');

INSERT INTO registro_mantenimiento (Fecha, Kilometraje, Trabajo, Repuesto, Placa) VALUES ('2022-01-01', 10000, 'Cambio de aceite', 'Filtro de aceite', 'ABC123');

INSERT INTO registro_mantenimiento (Fecha, Kilometraje, Trabajo, Repuesto, Placa) VALUES ('2023-03-28', 9000, 'Cambio de bujías', 'Bujías', 'GHI789');

INSERT INTO registro_mantenimiento (Fecha, Kilometraje, Trabajo, Repuesto, Placa) VALUES ('2023-04-15', 9500, 'Cambio de frenos', 'Pastillas de freno', 'DEF456');

INSERT INTO registro_mantenimiento (Fecha, Kilometraje, Trabajo, Repuesto, Placa) VALUES ('2023-02-14', 8000, 'Cambio de filtros', 'Amortiguadores', 'JKL012');

INSERT INTO registro_mantenimiento (Fecha, Kilometraje, Trabajo, Repuesto, Placa) VALUES ('2023-01-30', 7500, 'Cambio de bujías', 'Cables de bujía', 'MNO345');

