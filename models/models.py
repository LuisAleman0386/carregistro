from datetime import datetime
import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, DateTime, Boolean
import bcrypt


db = SQLAlchemy()

### 📌 Tabla de Roles
class Rol(db.Model):
    __tablename__ = 'Roles'
    id_rol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)  
    usuarios = db.relationship('Usuario', back_populates='rol')
    permisos = db.relationship('Permiso', back_populates='rol')


class Usuario(db.Model):
    __tablename__ = 'Usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100), unique=True, nullable=False)
    contraseña_hash = db.Column(db.String(255), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('Roles.id_rol'), nullable=False)
    rol = db.relationship('Rol', back_populates='usuarios')

    def __init__(self, usuario, contraseña, rol_id):
        self.usuario = usuario
        self.contraseña_hash = self.hash_contraseña(contraseña)
        self.rol_id = rol_id

    def hash_contraseña(self, contraseña):
        # Generar el hash de la contraseña con bcrypt
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(contraseña.encode('utf-8'), salt).decode('utf-8')

    def verificar_contraseña(self, contraseña):
        # Verificar si la contraseña ingresada coincide con el hash almacenado
        return bcrypt.checkpw(contraseña.encode('utf-8'), self.contraseña_hash.encode('utf-8'))


### 📌 Tabla de Módulos
class Modulo(db.Model):
    __tablename__ = 'Modulos'
    id_modulo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    permisos = db.relationship('Permiso', back_populates='modulo')


### 📌 Tabla de Permisos
class Permiso(db.Model):
    __tablename__ = 'Permisos'
    id_permiso = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rol_id = db.Column(db.Integer, db.ForeignKey('Roles.id_rol'), nullable=False)
    modulo_id = db.Column(db.Integer, db.ForeignKey('Modulos.id_modulo'), nullable=False)
    habilitado = db.Column(db.Boolean, default=True, nullable=False)

    rol = db.relationship('Rol', back_populates='permisos')
    modulo = db.relationship('Modulo', back_populates='permisos')


### 📌 Tabla de Vehículos
class Vehiculo(db.Model):
    __tablename__ = 'Vehiculos'
    id_vehiculo = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(15), unique=True, nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    kilometraje_actual = db.Column(db.Integer, default=0, nullable=False)
    salidas = db.relationship('RegistroSalidaVehiculo', backref='vehiculo', lazy=True)
    entradas = db.relationship('RegistroEntradaVehiculo', backref='vehiculo', lazy=True)


### 📌 Tabla de Pilotos
class Piloto(db.Model):
    __tablename__ = 'Pilotos'
    id_piloto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    licencia = db.Column(db.String(20), unique=True, nullable=False)
    salidas = db.relationship('RegistroSalidaVehiculo', backref='piloto', lazy=True)
    entradas = db.relationship('RegistroEntradaVehiculo', backref='piloto', lazy=True)


### 📌 Tabla de Guardias
class Guardia(db.Model):
    __tablename__ = 'Guardias'
    id_guardia = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    salidas_entregadas = db.relationship('RegistroSalidaVehiculo', backref='entregado_por_guardia', foreign_keys='RegistroSalidaVehiculo.entregado_por')
    entradas_recibidas = db.relationship('RegistroEntradaVehiculo', backref='recibido_por_guardia', foreign_keys='RegistroEntradaVehiculo.recibido_por')


### 📌 Registro de Salida de Vehículos
class RegistroSalidaVehiculo(db.Model):
    __tablename__ = 'Registro_Salida_Vehiculos'
    id_salida = db.Column(db.Integer, primary_key=True)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('Vehiculos.id_vehiculo'), nullable=False)
    piloto_id = db.Column(db.Integer, db.ForeignKey('Pilotos.id_piloto'), nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    hora_salida = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    observaciones_salida = db.Column(db.Text)
    kilometraje_salida = db.Column(db.Integer, nullable=False)
    entregado_por = db.Column(db.Integer, db.ForeignKey('Guardias.id_guardia'), nullable=False)


### 📌 Registro de Entrada de Vehículos
class RegistroEntradaVehiculo(db.Model):
    __tablename__ = 'Registro_Entrada_Vehiculos'
    id_entrada = db.Column(db.Integer, primary_key=True)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('Vehiculos.id_vehiculo'), nullable=False)
    piloto_id = db.Column(db.Integer, db.ForeignKey('Pilotos.id_piloto'), nullable=False)
    recibido_por = db.Column(db.Integer, db.ForeignKey('Guardias.id_guardia'))
    hora_llegada = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    observaciones_llegada = db.Column(db.Text)
    kilometraje_llegada = db.Column(db.Integer)
