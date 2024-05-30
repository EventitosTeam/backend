#!/usr/bin/env python3

import connexion
import pymysql

from swagger_server import encoder
# from flask_sqlalchemy import SQLAlchemy
from swagger_server.database import db

# db = SQLAlchemy()
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():

    logger.info("Inicializando la aplicación Flask")

    HOST = "monorail.proxy.rlwy.net"
    USER = "root"
    PASSWORD = "QMRjiHZseNfiVlVTPVByakrzkfYnbHaq"
    PORT = 27484
    DB_NAME = "railway"

    # Conectar a la base de datos
    # try:
    #     db_connection = pymysql.connect(
    #         host=HOST,
    #         user=USER,
    #         password=PASSWORD,
    #         database=DB_NAME,
    #         port=PORT
    #     )
    #     print("Conexión a la base de datos MySQL exitosa")
    # except pymysql.MySQLError as err:
    #     print(f"Error: {err}")
    #     return

    app = connexion.App(__name__, specification_dir='./swagger/')

    flask_app = app.app

    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?charset=utf8mb4'

    db.init_app(flask_app)

    # Crear todas las tablas en la base de datos
    with flask_app.app_context():
        db.create_all()

    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'API para sistema de Eventos'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
