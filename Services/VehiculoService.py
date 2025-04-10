from models.models import vehiculos


class VehiculoService:
    def __init__(self, vehiculo_repository):
        self.vehiculo_repository = vehiculo_repository

    def obtener_todos_los_vehiculos(self):
        return self.vehiculo_repository.obtener_todos()

    def obtener_vehiculo_por_id(self, id_vehiculo):
        return self.vehiculo_repository.obtener_por_id(id_vehiculo)

    def guardar_vehiculo(self, placa, modelo, marca, kilometraje_actual):
        nuevo_vehiculo = vehiculos(placa=placa, modelo=modelo, marca=marca, kilometraje_actual=kilometraje_actual)
        return self.vehiculo_repository.guardar(nuevo_vehiculo)

    def actualizar_vehiculo(self, id_vehiculo, placa, modelo, marca, kilometraje_actual):
        vehiculo = self.vehiculo_repository.obtener_por_id(id_vehiculo)
        vehiculo.placa = placa
        vehiculo.modelo = modelo
        vehiculo.marca = marca
        vehiculo.kilometraje_actual = kilometraje_actual

        self.vehiculo_repository.actualizar(vehiculo)

    def eliminar_vehiculo(self, id_vehiculo):
        vehiculo = self.vehiculo_repository.obtener_por_id(id_vehiculo)
        self.vehiculo_repository.eliminar(vehiculo)

