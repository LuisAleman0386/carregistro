from flask import Blueprint

login_bp = Blueprint('login_bp', __name__, url_prefix='/')
dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')
control = Blueprint('control', __name__, url_prefix='/control')
pilotos_bp = Blueprint('pilotos_bp', __name__, url_prefix='/pilotos')
guardia_bp = Blueprint('guardia_bp', __name__, url_prefix='/guardia')