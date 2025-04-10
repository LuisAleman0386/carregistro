from flask import session, request, render_template, redirect, url_for


def verificar_usuario():
    rutas_no_protegidas = ['login_bp.ingresar']

    # Excluir las rutas de archivos estaticos
    if request.endpoint and 'static' in request.endpoint:
        return None 
    
    # Verificar si usuario no esta en sesion
    if 'usuario' not in session and request.endpoint not in rutas_no_protegidas:
        return redirect(url_for('login_bp.ingresar'))