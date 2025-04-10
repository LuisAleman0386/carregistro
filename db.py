from flask_sqlalchemy import SQLAlchemy
from pymysql.err import MySQLError
from decouple import config
import pymysql

# ✅ Instancia de SQLAlchemy para Flask-Migrate
db = SQLAlchemy()

# ✅ Conexión manual con pymysql
def establecer_conexion():
    try:
        return pymysql.connect(
            host=config('MYSQL_HOST'),
            user=config('MYSQL_USER'),
            password=config('MYSQL_PASSWORD'),
            database=config('MYSQL_DATABASE'),
            port=3306  # Asegúrate de que MySQL está corriendo en este puerto
        )
    except MySQLError as e:
        raise e
