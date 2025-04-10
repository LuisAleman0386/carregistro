from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy import  ForeignKey, Integer ,String, DateTime, Boolean
import bcrypt


db = SQLAlchemy()

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

