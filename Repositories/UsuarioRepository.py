from models.models import usuarios


class UsuarioRepository:
    """Repositorio para manejar operaciones sobre Usuarios en la base de datos"""

    def obtener_usuario_por_usuario(self, usuario: str):
        """Busca un usuario en la base de datos por su nombre de usuario"""
        return usuarios.query.filter_by(usuario=usuario).first()
