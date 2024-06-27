import logging
import sys
import os
from flask import Flask
import connexion
from flask_cors import CORS

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from swagger_server.database import db
from swagger_server.models.event_item import EventItem
from swagger_server.models.book_item import BookItem
from swagger_server import encoder
from swagger_server.controllers.users_controller import events, bookings
import unittest


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BaseTestCase(unittest.TestCase):

    def create_app(self):
        logger.info("Inicializando la aplicación Flask para pruebas")

        HOST = "monorail.proxy.rlwy.net"
        USER = "root"
        PASSWORD = "bkxnrrBJXBehfGebmPXHHwbtINaXgOOo"
        PORT = 32365
        DB_NAME = "railway"

        app = Flask(__name__)
        app.json_encoder = encoder.FlaskJSONEncoder
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?charset=utf8mb4'
        app.config['TESTING'] = True

        # Registrar blueprints
        app.register_blueprint(events, url_prefix='/events')
        app.register_blueprint(bookings, url_prefix='/bookings')

        # Configurar CORS
        CORS(app, support_credentials=True)

        # Configurar la aplicación de base de datos
        db.init_app(app)

        return app

    def setUp(self):
        self.app = self.create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
        self.populate_db()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def populate_db(self):
        event = EventItem(
            name='Test Event',
            desciption='A test event',
            date='2024-06-24',
            event_place_lat='12.9716',
            event_place_lon='77.5946',
            people_limit=100
        )
        db.session.add(event)
        db.session.commit()

        booking = BookItem(
            booking_code='test-booking-code',
            registered=True,
            user='Test User',
            event_id=event.id
        )
        db.session.add(booking)
        db.session.commit()

if __name__ == '__main__':
    unittest.main()
