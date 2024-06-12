#!/usr/bin/env python3

# import connexion
import pymysql

# from swagger_server import encoder
# from flask_sqlalchemy import SQLAlchemy
from swagger_server.database import db

# db = SQLAlchemy()
import logging
from flask import Flask
from swagger_server.models import EventItem, BookItem, GuestItem

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():


    logger.info("Inicializando la aplicación Flask")
    print('hola chau sss')

    HOST = "monorail.proxy.rlwy.net"
    USER = "root"
    PASSWORD = "bkxnrrBJXBehfGebmPXHHwbtINaXgOOo"
    PORT = 32365
    DB_NAME = "railway"


    app = Flask(__name__)
    # app = connexion.App(__name__, specification_dir='./swagger/')

    # flask_app = app.app

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?charset=utf8mb4'

    app.app_context().push()

    db.init_app(app)

    # Crear todas las tablas en la base de datos
    with app.app_context():
        db.create_all()
    # db.drop_all()

    # app.app.json_encoder = encoder.JSONEncoder
    # app.add_api('swagger.yaml', arguments={'title': 'API para sistema de Eventos'}, pythonic_params=True)
    # app.run(port=8080)

    from swagger_server.controllers.users_controller import events
    app.register_blueprint(events, url_prefix='/events')

    @app.route('/health')
    def health():
        return 'OK'

    app.run(host = '0.0.0.0', debug = True, port = 8080)


if __name__ == '__main__':
    main()
