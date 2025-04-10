from abc import ABC, abstractmethod
from models.models import guardias

class IGuardiaRepository(ABC):
    @abstractmethod
    def obtener_todos_los_guardias(self) -> list:
        """Obtiene todos los guardias"""
        pass

    @abstractmethod
    def obtener_guardia_por_id(self, id_guardia: int) -> guardias:
        """Obtiene un guardia por su ID"""
        pass
