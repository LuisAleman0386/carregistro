from abc import ABC, abstractmethod
from models.models import usuarios

class IUsuarioRepository(ABC):
    @abstractmethod
    def obtener_usuario_por_id(self, id_usuario: int) -> usuarios:
        """Busca un usuario en la base de datos por su ID"""
        return usuarios.query.filter_by(id_usuario=id_usuario).first()
