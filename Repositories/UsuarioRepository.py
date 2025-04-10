from models.models import Usuario
from app import db

class UsuarioRepository:
    """Repositorio para manejar operaciones sobre Usuarios en la base de datos"""

    def obtener_usuario_por_usuario(self, usuario: str):
        """Busca un usuario en la base de datos por su nombre de usuario"""
        return Usuario.query.filter_by(usuario=usuario).first()
