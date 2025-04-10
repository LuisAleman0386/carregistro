from flask import  request, render_template, redirect, url_for, flash
from Routes.routes import guardia_bp
from Services.GuardiaService import GuardiaService
from Repositories.GuardiaRepository import GuardiaRepository


@guardia_bp.route('/lista_guardias', methods = ['GET', 'POST'])
def lista_guardias():
    """Vista para mostrar la lista de guardias"""
    
    # Crear una instancia del repositorio de guardias
    guardia_repository = GuardiaRepository()
    
    # Crear una instancia del servicio de guardias con el repositorio
    guardia_service = GuardiaService(guardia_repository)
    
    # Obtener todos los guardias
    guardias = guardia_service.obtener_todos_los_guardias()
    
    # Pasar los guardias a la plantilla
    return render_template('lista_guardias.html', guardias=guardias)



@guardia_bp.route('/agregar_guardia', methods=['GET', 'POST'])
def agregar_guardia():
    """Vista para agregar un nuevo guardia"""

    # Crear una instancia del repositorio de guardias
    guardia_repository = GuardiaRepository()

    # Crear una instancia del servicio de guardias
    guardia_service = GuardiaService(guardia_repository)

    if request.method == 'POST':
        # Obtener el nombre desde el formulario
        nombre = request.form['nombre']
        
        # Usamos el servicio para agregar el nuevo guardia
        guardia_service.agregar_guardia(nombre)

        # Mostrar un mensaje de éxito
        flash('Guardia agregado exitosamente!', 'success')

        # Redirigir al listado de guardias o donde prefieras
        return redirect(url_for('guardia_bp.lista_guardias'))

    return render_template('agregar_guardia.html')



@guardia_bp.route('/ver_guardia/<int:id_guardia>', methods=['GET', 'POST'])
def ver_guardia(id_guardia):
    """Vista para ver y editar los detalles de un guardia"""

    # Crear una instancia del repositorio de guardias
    guardia_repository = GuardiaRepository()

    # Crear una instancia del servicio de guardias
    guardia_service = GuardiaService(guardia_repository)
    
    # Obtener el guardia desde el repositorio
    guardia = guardia_service.obtener_guardia_por_id(id_guardia)
    
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']

        # Llamar al servicio para actualizar el guardia
        guardia_service.actualizar_guardia(id_guardia, nombre)

        flash('Guardia actualizado exitosamente!', 'success')
        return redirect(url_for('guardia_bp.lista_guardias'))
    
    return render_template('ver_guardia.html', guardia=guardia)





@guardia_bp.route('/eliminar_guardia/<int:id_guardia>', methods=['POST'])
def eliminar_guardia(id_guardia):
    """Ruta para eliminar un guardia"""

    # Crear una instancia del repositorio de guardias
    guardia_repository = GuardiaRepository()

    # Crear una instancia del servicio de guardias
    guardia_service = GuardiaService(guardia_repository)
    
    # Llamar al servicio para eliminar el guardia
    guardia_service.eliminar_guardia(id_guardia)

    flash('Guardia eliminado exitosamente!', 'success')
    return redirect(url_for('guardia_bp.lista_guardias'))
