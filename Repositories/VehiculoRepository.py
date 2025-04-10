from Repositories.Interfaces.IVehiculoRepository import IVehiculoRepository
from models.models import vehiculos
from db import db




class VehiculoRepository(IVehiculoRepository):

    def obtener_todos(self):
        return vehiculos.query.all()

    def obtener_por_id(self, id_vehiculo):
        return vehiculos.query.get(id_vehiculo)

    def guardar(self, vehiculo):
        db.session.add(vehiculo)
        db.session.commit()

    def actualizar(self, vehiculo):
        db.session.commit()

    def eliminar(self, vehiculo):
        db.session.delete(vehiculo)
        db.session.commit()