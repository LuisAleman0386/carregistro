from abc import ABC, abstractmethod
from models.models import Usuario

class IUsuarioRepository(ABC):
    @abstractmethod
    def obtener_usuario_por_id(self, id_usuario: int) -> Usuario:
        """Método para obtener un usuario por ID"""
        pass