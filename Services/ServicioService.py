from Repositories.ServicioRepository import ServicioRepository
from models.models import servicios, proximo_servicio
from datetime import datetime

class ServicioService:
    def __init__(self, repo: ServicioRepository):
        self.repo = repo
    
    def agregar_servicio_y_proximo(self, data):
        servicio = servicios(
            id_vehiculo=data['id_vehiculo'],
            id_tipo_mantenimiento=data['id_tipo_mantenimiento'],
            observaciones=data['observaciones'],
            fecha_ingreso_taller=datetime.strptime(data['fecha_ingreso_taller'], '%Y-%m-%d'),
            fecha_salida_taller=datetime.strptime(data['fecha_salida_taller'], '%Y-%m-%d'),
            autorizacion=data['autorizacion'],
            costo_del_servicio=data['costo_del_servicio']
        )
        self.repo.guardar_servicio(servicio)

        prox_servicio = proximo_servicio(
            id_vehiculo=data['id_vehiculo'],
            kilometraje_proximo_servicio=data['kilometraje_proximo_servicio']
        )
        self.repo.guardar_proximo_servicio(prox_servicio)

    def obtener_tipos_mantenimiento(self):
        return self.repo.obtener_todos_los_tipos_mantenimiento()
    
    def obtener_todos_los_servicios(self):
        return self.repo.obtener_todos()
    
    def obtener_por_id(self, id_servicio):
     return self.repo.obtener_por_id(id_servicio)
