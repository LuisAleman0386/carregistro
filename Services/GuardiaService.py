from Repositories.Interfaces.IGuardiaRepository import  IGuardiaRepository


class GuardiaService:
    """Servicio para manejar operaciones sobre los Guardias"""

    def __init__(self, guardia_repository: IGuardiaRepository):
        self.guardia_repository = guardia_repository

    def obtener_todos_los_guardias(self):
        """Obtiene todos los guardias"""
        return self.guardia_repository.obtener_todos_los_guardias()

    def obtener_guardia_por_id(self, id_guardia: int):
        """Obtiene un guardia por su ID"""
        return self.guardia_repository.obtener_guardia_por_id(id_guardia)
    
    def agregar_guardia(self, nombre):
        """Método para agregar un nuevo guardia"""
        # Delegar al repositorio para agregar el guardia
        return self.guardia_repository.guardar_guardia(nombre)
    
    def actualizar_guardia(self, id_guardia, nombre):
        """Delegar al repositorio la actualización del guardia"""

        guardia = self.guardia_repository.obtener_guardia_por_id(id_guardia)
        if guardia:
            guardia.nombre = nombre
            self.guardia_repository.guardar(guardia)


    def eliminar_guardia(self, id_guardia):
        """Delegar al repositorio la eliminación del guardia"""

        guardia = self.guardia_repository.obtener_guardia_por_id(id_guardia)
        if guardia:
            self.guardia_repository.eliminar(guardia)

