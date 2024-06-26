import unittest, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from swagger_server.services.event_service import EventService
from swagger_server.models.event_item import EventItem
from swagger_server import db, create_app

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
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
            description='A test event',
            date='2024-06-24',
            event_place_lat='12.9716',
            event_place_lon='77.5946',
            people_limit=100
        )
        db.session.add(event)
        db.session.commit()

class TestEventService(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.service = EventService()

    def test_create_event(self):
        new_event = EventItem(
            name='Service Test Event',
            description='Description for service test event',
            date='2024-07-01',
            event_place_lat='12.9716',
            event_place_lon='77.5946',
            people_limit=50
        )
        created_event = self.service.create_event(new_event)
        self.assertIsNotNone(created_event.id)
        self.assertEqual(created_event.name, 'Service Test Event')

    def test_get_event_by_id(self):
        event = self.service.get_event_by_id(1)
        self.assertIsNotNone(event)
        self.assertEqual(event.id, 1)

    def test_get_event_by_id_not_found(self):
        event = self.service.get_event_by_id(9999)
        self.assertIsNone(event)

if __name__ == '__main__':
    unittest.main()


