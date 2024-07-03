#!/usr/bin/env python3

import pymysql
from swagger_server.database import db
import logging
from flask import Flask
from swagger_server.models import EventItem, BookItem, GuestItem
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Inicializando la aplicación Flask")

    HOST = "monorail.proxy.rlwy.net"
    USER = "root"
    PASSWORD = "bkxnrrBJXBehfGebmPXHHwbtINaXgOOo"
    PORT = 32365
    DB_NAME = "railway"

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?charset=utf8mb4'

    app.app_context().push()

    db.init_app(app)

    # Crear todas las tablas en la base de datos
    with app.app_context():
        db.create_all()

    from swagger_server.controllers.users_controller import events, bookings
    app.register_blueprint(events, url_prefix='/events')
    app.register_blueprint(bookings, url_prefix='/bookings')

    #Permitir solicitudes de otros origenes
    cors = CORS(app, support_credentials=True)
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app, resources={r"*": {"origins": "*"}})

    @app.route('/health')
    def health():
        return 'OK'

    app.run(host = '0.0.0.0', debug = True, port = 8080)

if __name__ == '__main__':
    main()
