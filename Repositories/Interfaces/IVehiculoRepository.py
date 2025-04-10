
from abc import ABC, abstractmethod

class IVehiculoRepository(ABC):

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id_vehiculo):
        pass

    @abstractmethod
    def guardar(self, vehiculo):
        pass

    @abstractmethod
    def actualizar(self, vehiculo):
        pass

    @abstractmethod
    def eliminar(self, vehiculo):
        pass
