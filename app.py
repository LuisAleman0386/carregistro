from flask import Flask
from flask_migrate import Migrate
from decouple import config
from db import db, establecer_conexion  # db.py: contiene `db = SQLAlchemy()` y lógica de conexión
from models.models import *  # Asegúrate de que todos tus modelos estén en models/models.py
from Controllers.LoginController import login_bp
from Controllers.DashboardController import dashboard
from Controllers.ControlController import control

app = Flask(__name__)

# 🔹 Configuración de la base de datos desde el archivo .env
app.secret_key = config('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URI')  # ejemplo: 'mysql+pymysql://user:pass@localhost/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 🔹 Inicializar SQLAlchemy y Migrate
db.init_app(app)
migrate = Migrate(app, db)

# 🔹 Verificar conexión con la base de datos
with app.app_context():
    try:
        conn = establecer_conexion()
        print("✅ Conexión a la base de datos establecida correctamente.")
        conn.close()

        # 🔹 Crear todas las tablas si no existen (solo útil si no usas Flask-Migrate aún)
        db.create_all()

    except Exception as e:
        print("❌ Error al conectar a la base de datos:", str(e))

# 🔹 Registrar Blueprints
app.register_blueprint(login_bp)
app.register_blueprint(dashboard)
app.register_blueprint(control)



# 🔹 Punto de entrada
if __name__ == "__main__":
    app.run(debug=True)
