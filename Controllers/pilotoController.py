from flask import request, render_template, redirect, url_for, flash
from Routes.routes import pilotos_bp
from Services.PilotoService import PilotoService
from Repositories.PilotoRepository import PilotoRepository


@pilotos_bp.route('/pilotos', methods=['GET', 'POST'])
def agregar_piloto():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        licencia = request.form['licencia']

        # Crear una instancia de PilotoService
        piloto_service = PilotoService()

        try:
            # Llamar al servicio para agregar el piloto
            piloto_service.agregar_piloto(nombre, licencia)
            flash('Piloto agregado exitosamente!', 'success')
            return redirect(url_for('pilotos_bp.lista_pilotos')) 
        except Exception as e:
            flash(f'Error al agregar piloto: {str(e)}', 'danger')
            return redirect(url_for('pilotos_bp.agregar_piloto'))

    return render_template('agregar_piloto.html')



@pilotos_bp.route('/lista_pilotos')
def lista_pilotos():

    # Crear una instancia de PilotoService
    piloto_service = PilotoService()

    # Llamar al método obtener_todos_los_pilotos usando la instancia
    pilotos = piloto_service.obtener_todos_los_pilotos()

    return render_template('lista_pilotos.html',
                           pilotos = pilotos)



@pilotos_bp.route('/ver_piloto/<int:id_piloto>', methods=['GET', 'POST'])
def ver_piloto(id_piloto):
    piloto_service = PilotoService()
    piloto = piloto_service.obtener_piloto_por_id(id_piloto)

    if not piloto:
        flash('Piloto no encontrado', 'danger')
        return redirect(url_for('pilotos_bp.lista_pilotos'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        licencia = request.form['licencia']

        # Llamar al servicio para actualizar el piloto
        piloto_actualizado = piloto_service.actualizar_piloto(id_piloto, nombre, licencia)

        if piloto_actualizado:
            flash('Piloto actualizado exitosamente!', 'success')
            return redirect(url_for('pilotos_bp.lista_pilotos')) 
        else:
            flash('Error al actualizar piloto', 'danger')
            return redirect(url_for('pilotos_bp.ver_piloto', id_piloto=id_piloto))

    return render_template('ver_piloto.html', piloto=piloto)


@pilotos_bp.route('/eliminar_piloto/<int:id_piloto>', methods=['POST'])
def eliminar_piloto(id_piloto):
    # Usamos el servicio o el repositorio para eliminar el piloto
    piloto_repository = PilotoRepository()  # O si usas el servicio, puedes usarlo aquí
    piloto = piloto_repository.obtener_piloto_por_id(id_piloto)

    if piloto:
        # Si el piloto existe, lo eliminamos
        piloto_repository.eliminar_piloto(id_piloto)  # Asegúrate de tener un método para eliminar
        flash('Piloto eliminado correctamente', 'success')
    else:
        flash('Piloto no encontrado', 'error')

    return redirect(url_for('pilotos_bp.lista_pilotos'))  # Redirigimos a la lista de pilotos
