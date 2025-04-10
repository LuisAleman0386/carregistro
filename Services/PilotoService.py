from Repositories.PilotoRepository import PilotoRepository

class PilotoService:
    """Servicio para manejar operaciones sobre los Pilotos"""

    def __init__(self):
        self.piloto_repository = PilotoRepository()

    def obtener_piloto_por_id(self, id_piloto: int):
        """Obtiene un piloto por su ID"""
        return self.piloto_repository.obtener_piloto_por_id(id_piloto)

    def obtener_todos_los_pilotos(self):
        """Obtiene todos los pilotos"""
        return self.piloto_repository.obtener_todos_los_pilotos()
    
    def agregar_piloto(self, nombre: str, licencia: str):
        """Llama al repositorio para agregar un nuevo piloto"""
        return self.piloto_repository.agregar_piloto(nombre, licencia)
    
    def actualizar_piloto(self, id_piloto: int, nombre: str, licencia: str):
        """Llama al repositorio para actualizar un piloto"""
        return self.piloto_repository.actualizar_piloto(id_piloto, nombre, licencia)