from flask import request, render_template, redirect, url_for, flash
from Routes.routes import servicio_bp
from Repositories.ServicioRepository import ServicioRepository
from Services.ServicioService import ServicioService
from Repositories.VehiculoRepository import VehiculoRepository





@servicio_bp.route('/lista_servicios', methods=['GET', 'POST'])
def lista_servicios():
    servicio_repo = ServicioRepository()
    servicio_service = ServicioService(servicio_repo)

    servicios = servicio_service.obtener_todos_los_servicios()
    return render_template('lista_servicios.html', servicios=servicios)


@servicio_bp.route('/agregar_servicio', methods=['GET', 'POST'])
def agregar_servicio():
    servicio_repo = ServicioRepository()
    servicio_service = ServicioService(servicio_repo)
    vehiculo_repo = VehiculoRepository()
    tipos_mantenimiento = servicio_service.obtener_tipos_mantenimiento()
    vehiculos = vehiculo_repo.obtener_todos()

    if request.method == 'POST':
        data = {
            'id_vehiculo': int(request.form['vehiculo']),
            'id_tipo_mantenimiento': int(request.form['tipo_mantenimiento']),
            'observaciones': request.form['observaciones'],
            'fecha_ingreso_taller': request.form['fecha_ingreso_taller'],
            'fecha_salida_taller': request.form['fecha_salida_taller'],
            'autorizacion': request.form['autorizacion'],
            'costo_del_servicio': float(request.form['costo']),
            'kilometraje_proximo_servicio': float(request.form['kilometraje_proximo'])
        }

        servicio_service.agregar_servicio_y_proximo(data)
        flash('Servicio guardado correctamente.', 'success')

        return redirect(url_for('servicio_bp.agregar_servicio'))

   
    return render_template('agregar_servicio.html', tipos_mantenimiento=tipos_mantenimiento, vehiculos=vehiculos)



@servicio_bp.route('/detalle_servicio/<int:id_servicio>')
def detalle_servicio(id_servicio):
    servicio_repo = ServicioRepository()
    servicio_service = ServicioService(servicio_repo)

    servicio = servicio_service.obtener_por_id(id_servicio)
    if not servicio:
        flash('Servicio no encontrado.', 'danger')
        return redirect(url_for('servicio_bp.lista_servicios'))

    return render_template('ver_servicio.html', servicio=servicio)
