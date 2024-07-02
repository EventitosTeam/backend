import json, os, sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from swagger_server.test.base_test import BaseTestCase

class TestEventController(BaseTestCase):

    def test_get_events(self):
        response = self.client.get("/events/")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0, "Expected to get a list with at least one event")

    def test_get_event_by_id(self):
        event_id = 1
        response = self.client.get(f"/events/{event_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data["id"], event_id, f"Expected event ID to be {event_id}")

    def test_get_event_by_id_not_found(self):
        response = self.client.get("/events/9999")
        self.assertEqual(response.status_code, 404)
        data = response.json
        self.assertEqual(data["detail"], "Event with id 9999 not found", "Expected not found message")

    def test_create_event(self):
        new_event_data = {
            "name": "New Event",
            "description": "Description for new event",
            "date": "2024-07-01",
            "event_place_lat": "12.9716",
            "event_place_lon": "77.5946",
            "people_limit": 100
        }
        response = self.client.post(
            "/events/",
            data=json.dumps(new_event_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = response.json
        self.assertEqual(data["name"], new_event_data["name"])
        self.assertEqual(data["description"], new_event_data["description"])
        self.assertEqual(data["date"], new_event_data["date"])
        self.assertEqual(data["event_place_lat"], new_event_data["event_place_lat"])
        self.assertEqual(data["event_place_lon"], new_event_data["event_place_lon"])
        self.assertEqual(data["people_limit"], new_event_data["people_limit"])

if __name__ == '__main__':
    unittest.main()
