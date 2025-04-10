from abc import ABC, abstractmethod
from models.models import pilotos

class IPilotoRepository(ABC):
    @abstractmethod
    def obtener_piloto_por_id(self, id_piloto: int) -> pilotos:
        """Busca un piloto en la base de datos por su ID"""
        pass

    @abstractmethod
    def obtener_todos_los_pilotos(self) -> list:
        """Obtiene todos los pilotos"""
        pass 