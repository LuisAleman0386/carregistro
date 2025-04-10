from models.models import guardias
from db import db

class GuardiaRepository:
    """Repositorio para manejar operaciones sobre Guardias en la base de datos"""

    def obtener_todos_los_guardias(self) -> list:
        """Obtiene todos los guardias"""
        return guardias.query.all()

    def obtener_guardia_por_id(self, id_guardia: int) -> guardias:
        """Obtiene un guardia por su ID"""
        return guardias.query.filter_by(id_guardia=id_guardia).first()
    
    def guardar_guardia(self, nombre: str):
        """Guarda un nuevo guardia en la base de datos"""
        # Crear una instancia del modelo guardia
        nuevo_guardia = guardias(nombre=nombre)
        
        # Agregarlo a la sesión de la base de datos
        db.session.add(nuevo_guardia)
        
        # Confirmar los cambios
        db.session.commit()

    def guardar(self, guardia):
        """Guardar los cambios del guardia en la base de datos"""
        db.session.commit()

    def eliminar(self, guardia):
        """Eliminar un guardia de la base de datos"""
        db.session.delete(guardia)
        db.session.commit()