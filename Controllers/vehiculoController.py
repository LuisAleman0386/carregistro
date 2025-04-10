from flask import request, render_template, redirect, url_for, flash
from Routes.routes import vehiculos_bp
from Repositories.VehiculoRepository import VehiculoRepository
from Services.VehiculoService import VehiculoService

@vehiculos_bp.route('/vehiculos' )
def lista_vehiculos():
    vehiculo_repository = VehiculoRepository()
    vehiculo_service = VehiculoService(vehiculo_repository)

    vehiculos = vehiculo_service.obtener_todos_los_vehiculos()
    
    return render_template('lista_vehiculos.html', vehiculos=vehiculos)



@vehiculos_bp.route('/agregar_vehiculo', methods=['GET', 'POST'])
def agregar_vehiculo():
    vehiculo_repository = VehiculoRepository()
    vehiculo_service = VehiculoService(vehiculo_repository)

    if request.method == 'POST':
        placa = request.form['placa']
        modelo = request.form['modelo']
        marca = request.form['marca']
        kilometraje_actual = request.form['kilometraje_actual']

        try:
            kilometraje_actual = float(kilometraje_actual) if kilometraje_actual else 0
            vehiculo_service.guardar_vehiculo(placa, modelo, marca, kilometraje_actual)
            flash('Vehículo agregado exitosamente', 'success')
            return redirect(url_for('vehiculos_bp.lista_vehiculos'))
        except Exception as e:
            flash(f'Error al agregar vehículo: {str(e)}', 'danger')
            return redirect(url_for('vehiculos_bp.agregar_vehiculo'))

    return render_template('agregar_vehiculo.html')


@vehiculos_bp.route('/ver_vehiculo/<int:id_vehiculo>', methods=['GET', 'POST'])
def ver_vehiculo(id_vehiculo):
    vehiculo_repository = VehiculoRepository()
    vehiculo_service = VehiculoService(vehiculo_repository)

    vehiculo = vehiculo_service.obtener_vehiculo_por_id(id_vehiculo)

    if request.method == 'POST':
        placa = request.form['placa']
        modelo = request.form['modelo']
        marca = request.form['marca']
        kilometraje_actual = request.form['kilometraje_actual']

        vehiculo_service.actualizar_vehiculo(
                id_vehiculo,
                placa,
                modelo,
                marca,
                float(kilometraje_actual)
            )

        flash('Vehículo actualizado exitosamente', 'success')
        return redirect(url_for('vehiculos_bp.lista_vehiculos'))

    return render_template('ver_vehiculo.html', vehiculo=vehiculo)



@vehiculos_bp.route('/eliminar_vehiculo/<int:id_vehiculo>', methods=['POST'])
def eliminar_vehiculo(id_vehiculo):
    vehiculo_repository = VehiculoRepository()
    vehiculo_service = VehiculoService(vehiculo_repository)

    vehiculo_service.eliminar_vehiculo(id_vehiculo)
    flash('Vehículo eliminado correctamente', 'warning')

    return redirect(url_for('vehiculos_bp.lista_vehiculos'))
