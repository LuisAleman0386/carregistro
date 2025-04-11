from models.models import tipo_mantenimiento
from models.models import servicios, proximo_servicio
from db import db

class ServicioRepository:

    def obtener_todos(self):
        return servicios.query.all()

    def guardar_servicio(self, servicio: servicios):
        db.session.add(servicio)
        db.session.commit()

    def guardar_proximo_servicio(self, prox_serv: proximo_servicio):
        db.session.add(prox_serv)
        db.session.commit()

    def obtener_todos_los_tipos_mantenimiento(self):
        return tipo_mantenimiento.query.all()
    
    def obtener_por_id(self, id_servicio):
        return servicios.query.get(id_servicio)

