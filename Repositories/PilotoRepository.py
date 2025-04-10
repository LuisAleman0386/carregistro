from models.models import pilotos
from db import db

class PilotoRepository:
    """Repositorio para manejar operaciones sobre Pilotos en la base de datos"""

    def obtener_piloto_por_id(self, id_piloto: int) -> pilotos:
        """Busca un piloto en la base de datos por su ID"""
        return pilotos.query.filter_by(id_piloto=id_piloto).first()

    def obtener_todos_los_pilotos(self) -> list:
        """Obtiene todos los pilotos"""
        return pilotos.query.all()

    def agregar_piloto(self, nombre: str, licencia: str):
        """Agrega un nuevo piloto a la base de datos"""
        nuevo_piloto = pilotos(nombre=nombre, licencia=licencia)
        try:
            db.session.add(nuevo_piloto)
            db.session.commit()
            return nuevo_piloto
        except Exception as e:
            db.session.rollback()
            raise e
        
    def actualizar_piloto(self, id_piloto: int, nombre: str, licencia: str):
        """Actualiza los datos de un piloto en la base de datos"""
        piloto = pilotos.query.get(id_piloto)
        if piloto:
            piloto.nombre = nombre
            piloto.licencia = licencia
            try:
                db.session.commit()
                return piloto
            except Exception as e:
                db.session.rollback()
                raise e
        return None
    
    def eliminar_piloto(self, id_piloto: int):
        """Elimina un piloto de la base de datos"""
        piloto = self.obtener_piloto_por_id(id_piloto)
        if piloto:
            db.session.delete(piloto)
            db.session.commit()