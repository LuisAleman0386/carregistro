from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, session
from Services.LoginService import LoginService
from Routes.routes import login_bp


login_service = LoginService()

@login_bp.route('/', methods=['GET', 'POST'])
def ingresar():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        user = login_service.validar_usuario(usuario, contraseña)
        
        if user:
            
            session['usuario'] = {
                'id_usuario': user.id_usuario,
                'usuario': user.usuario,
                'id_rol': user.id_rol
            }
            return redirect(url_for('dashboard.ver_pant_principal'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    
    return render_template('login.html')



@login_bp.route('/cerrar', methods=['GET'])
def cerrar():
    session.pop('usuario', None)
    return redirect(url_for('login_bp.ingresar'))

