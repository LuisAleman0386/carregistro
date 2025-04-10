from flask import Flask
from flask_migrate import Migrate
from decouple import config
from db import db
from models.models import *
from utils.utils import *

app = Flask(__name__)


app.secret_key = config('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URI') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
migrate = Migrate(app, db)


# llamar modelos
from models.models import *

with app.app_context():
    db.create_all()



with app.app_context():
    try:
        print("La conexion a la base de datos se establecio correctamente.")
    except Exception as e:
        print("Error al conectar a la base de datos:", str(e))




from Controllers.LoginController import login_bp
from Controllers.DashboardController import dashboard
from Controllers.ControlController import control
from Controllers.pilotoController import pilotos_bp
from Controllers.guardiaController import guardia_bp
from Controllers.vehiculoController import vehiculos_bp

# Registrar Blueprints
app.register_blueprint(login_bp)
app.register_blueprint(dashboard)
app.register_blueprint(control)
app.register_blueprint(pilotos_bp)
app.register_blueprint(guardia_bp)
app.register_blueprint(vehiculos_bp)




@app.before_request
def verificar_usuario_middleware():
    redir = verificar_usuario() 
    if redir:
        return redir 
