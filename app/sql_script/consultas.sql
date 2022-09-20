CREATE TABLE consultas(
	id_consulta INT NOT NULL AUTO_INCREMENT,
    rut_medico VARCHAR(9) NOT NULL,
    id_tipo_consulta INT NOT NULL,
    id_estado_consulta INT NOT NULL,
    observacion_consulta TEXT null,
    activa BOOLEAN,
    PRIMARY KEY(id_consulta)
);

CREATE TABLE atenciones(
    id_atencion INT NOT NULL AUTO_INCREMENT,
    id_consulta INT NOT NULL,
    rut_paciente VARCHAR(9) NOT null,
    fecha_atencion DATE NOT NULL,
    hora_atencion TIME NOT NULL,
    valor_consulta INT NOT NULL,
    observacion_atencion TEXT  NULL,
    prioridad int NOT  NULL,
    activo BOOLEAN,
    PRIMARY KEY(id_atencion)

);

CREATE TABLE pacientes(
    rut_paciente VARCHAR(9) NOT NULL,
    nombre_paciente VARCHAR(15) NOT NULL,
    paterno_paciente VARCHAR(15) NOT NULL,
    materno_paciente VARCHAR(15) NOT NULL,
    edad_paciente INT NOT NULL,
    peso_paciente DOUBLE NOT NULL,
    estatura_paciente DOUBLE NOT NULL,
    fumador_paciente BOOLEAN,
    tiempo_fumador INT,
    dieta_paciente BOOLEAN,
    fecha_registro_paciente DATE NOT NULL,
    activo BOOLEAN,
    PRIMARY KEY(rut_paciente)
);

CREATE TABLE historial_clinico(
    id_historial_clinico INT NOT NULL AUTO_INCREMENT,
    id_atencion INT NOT NULL,
    PRIMARY KEY(id_historial_clinico)

);

CREATE TABLE medicos(
    rut_medico VARCHAR(9) NOT NULL,
    nombre_medico VARCHAR(15) NOT NULL,
    paterno_medico VARCHAR(15) NOT NULL,
    materno_medico VARCHAR(15) NOT NULL,
    fecha_registro_medico DATE NOT NULL,
    activo BOOLEAN,
    id_especialidad INT NOT NULL,
    PRIMARY KEY(rut_medico)
);

CREATE TABLE especialidades(
    id_especialidad INT NOT NULL AUTO_INCREMENT,
    nombre_especialidad VARCHAR(40) NOT NULL,
    PRIMARY KEY(id_especialidad)
);

CREATE TABLE tipo_consultas(
	id_tipo_consulta INT NOT NULL AUTO_INCREMENT,
    nombre_tipo_consulta VARCHAR(40) NOT NULL,
    PRIMARY KEY(id_tipo_consulta)
);

CREATE TABLE estado_consultas(
    id_estado_consulta INT NOT NULL AUTO_INCREMENT,
    nombre_estado_consulta VARCHAR(40) NOT NULL,
    PRIMARY KEY(id_estado_consulta)
);

-- Constraint consultas.
ALTER TABLE consultas
ADD CONSTRAINT fk_rut_medico
FOREIGN KEY(rut_medico) REFERENCES medicos(rut_medico);

ALTER TABLE consultas
ADD CONSTRAINT fk_id_tipo_consulta
FOREIGN KEY(id_tipo_consulta) REFERENCES tipo_consultas(id_tipo_consulta);

ALTER TABLE consultas
ADD CONSTRAINT fk_id_estado_consulta
FOREIGN KEY(id_estado_consulta) REFERENCES estado_consultas(id_estado_consulta);

-- Constraint atenciones.
ALTER TABLE atenciones
ADD CONSTRAINT fk_id_consulta
FOREIGN KEY(id_consulta) REFERENCES consultas(id_consulta);

ALTER TABLE atenciones
ADD CONSTRAINT fk_rut_paciente
FOREIGN KEY(rut_paciente) REFERENCES pacientes(rut_paciente);

-- Constraint historial_clinico.
ALTER TABLE historial_clinico
ADD CONSTRAINT fk_id_atencion
FOREIGN KEY(id_atencion) REFERENCES atenciones(id_atencion);


-- Constraint medicos.
ALTER TABLE medicos
ADD CONSTRAINT fk_id_especialidad
FOREIGN KEY(id_especialidad) REFERENCES especialidades(id_especialidad);


-- Inserciones
INSERT INTO estado_consultas(nombre_estado_consulta)
VALUES ('En Espera');

INSERT INTO estado_consultas(nombre_estado_consulta)
VALUES ('Ocupada');

INSERT INTO estado_consultas(nombre_estado_consulta)
VALUES ('Desocupada');

INSERT INTO tipo_consultas(nombre_tipo_consulta) 
VALUES ('CGI(Consulta General Integral)');

INSERT INTO tipo_consultas(nombre_tipo_consulta) 
VALUES ('Urgencia');

INSERT INTO tipo_consultas(nombre_tipo_consulta) 
VALUES ('Pediatria');

INSERT INTO especialidades(nombre_especialidad) 
VALUES ('Pediatra');

INSERT INTO especialidades(nombre_especialidad) 
VALUES ('Medico Cirujano');