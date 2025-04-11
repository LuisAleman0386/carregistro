from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy import  ForeignKey, Integer ,String, DateTime, Boolean, Numeric
from db import db
import bcrypt



### Tabla de Roles
class roles(db.Model):
    __tablename__ = 'roles'
    id_rol = db.Column(Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(String(50), unique=True, nullable=False)  

    def __init__(self, nombre):
        self.nombre = nombre

class usuarios(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(Integer, primary_key=True)
    id_rol = db.Column(Integer, ForeignKey('roles.id_rol'))
    usuario = db.Column(String(100), unique=True, nullable=False)
    contraseña_hash = db.Column(String(255), nullable=False)

    rol = relationship('roles', backref=backref('usuarios', cascade='all, delete-orphan'))


    def __init__(self, usuario, contraseña, id_rol):
        self.usuario = usuario
        self.contraseña_hash = self.hash_contraseña(contraseña)
        self.id_rol = id_rol

    def hash_contraseña(self, contraseña):
        # Generar el hash de la contraseña con bcrypt
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(contraseña.encode('utf-8'), salt).decode('utf-8')

    def verificar_contraseña(self, contraseña):
        # Verificar si la contraseña ingresada coincide con el hash almacenado
        return bcrypt.checkpw(contraseña.encode('utf-8'), self.contraseña_hash.encode('utf-8'))



class pilotos(db.Model):
    __tablename__ = 'pilotos'
    id_piloto = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(100), nullable=False)
    licencia = db.Column(String(20), unique=True, nullable=False)

    def __init__(self, nombre, licencia):
        self.nombre = nombre
        self.licencia = licencia



class guardias(db.Model):
    __tablename__ = 'guardias'
    id_guardia = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(100), nullable=False)

    def __init__(self, nombre):
            self.nombre = nombre


### Tabla de Vehículos
class vehiculos(db.Model):
    __tablename__ = 'vehiculos'
    id_vehiculo = db.Column(Integer, primary_key=True)
    placa = db.Column(String(15), unique=True, nullable=False)
    modelo = db.Column(String(50), nullable=False)
    marca = db.Column(String(50), nullable=False)
    kilometraje_actual = db.Column(Numeric(precision=20, scale=2))
    


class tipo_mantenimiento(db.Model):
    __tablename__ = 'tipo_mantenimiento'

    id_tipo_mantenimiento = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(50), nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre
   

class servicios(db.Model):
    __tablename__ = 'servicios'

    id_servicio = db.Column(Integer, primary_key=True)
    id_vehiculo = db.Column(Integer, ForeignKey('vehiculos.id_vehiculo'))
    id_tipo_mantenimiento = db.Column(Integer, ForeignKey('tipo_mantenimiento.id_tipo_mantenimiento'))
    observaciones = db.Column(String, nullable=False)
    fecha_ingreso_taller = db.Column(DateTime, nullable=False)
    fecha_salida_taller = db.Column(DateTime, nullable=False)
    autorizacion = db.Column(String, nullable=False)
    costo_del_servicio = db.Column(Numeric(precision=10, scale=2))

    vehiculo = relationship('vehiculos', backref=backref('servicios', cascade='all, delete-orphan'))
    tipo_mante = relationship('tipo_mantenimiento', backref=backref('servicios', cascade='all, delete-orphan'))

    def __init__(self, id_vehiculo, id_tipo_mantenimiento, observaciones, fecha_ingreso_taller, fecha_salida_taller, autorizacion, costo_del_servicio):
        self.id_vehiculo = id_vehiculo
        self.id_tipo_mantenimiento = id_tipo_mantenimiento
        self.observaciones = observaciones
        self.fecha_ingreso_taller = fecha_ingreso_taller
        self.fecha_salida_taller = fecha_salida_taller
        self.autorizacion = autorizacion
        self.costo_del_servicio = costo_del_servicio



class proximo_servicio(db.Model):
    __tablename__ = 'proximo_servicio'

    id_proximo_servicio = db.Column(Integer, primary_key=True)
    id_vehiculo = db.Column(Integer, ForeignKey('vehiculos.id_vehiculo'), nullable=False)
    kilometraje_proximo_servicio = db.Column(Numeric(precision=20, scale=2))

    vehiculo = relationship('vehiculos', backref=backref('proximo_servicio', cascade='all, delete-orphan'))

    def __init__(self, id_vehiculo, kilometraje_proximo_servicio):
        self.id_vehiculo = id_vehiculo
        self.kilometraje_proximo_servicio = kilometraje_proximo_servicio

