from flask import Blueprint

login_bp = Blueprint('login_bp', __name__, url_prefix='/')
dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')
control = Blueprint('control', __name__, url_prefix='/control')
