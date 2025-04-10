from flask_sqlalchemy import SQLAlchemy
from psycopg2 import connect, Error as Psycopg2Error
from decouple import config

db = SQLAlchemy()
