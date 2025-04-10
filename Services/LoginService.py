from flask import session, flash
from Repositories.UsuarioRepository import UsuarioRepository
import bcrypt  # Importamos bcrypt para trabajar con contraseñas

class LoginService:
    """Servicio para manejar la autenticación de usuarios"""
    
    def __init__(self):
        self.usuario_repository = UsuarioRepository()
    
    def validar_usuario(self, usuario, contraseña):
        """Valida las credenciales del usuario"""
        usuario_encontrado = self.usuario_repository.obtener_usuario_por_usuario(usuario)

        if usuario_encontrado and usuario_encontrado.verificar_contraseña(contraseña):
            session['id_usuario'] = usuario_encontrado.id_usuario
            return usuario_encontrado
        else:
            return None
