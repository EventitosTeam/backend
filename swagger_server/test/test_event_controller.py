import json
import sys
sys.path.insert(0, '../')
from test import BaseTestCase

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

    def test_post_book(self):
        event_id = 1  
        user = {
            "name": "Test User",
            "email": "testuser@example.com"
        }
        response = self.client.post(
            f"/events/{event_id}/bookings",
            data=json.dumps(user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data["event_id"], event_id)
        self.assertEqual(data["user"]["name"], user["name"])
        self.assertEqual(data["user"]["email"], user["email"])

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

    def test_get_event_enrolled(self):
        booking_code = "test-booking-code"  
        response = self.client.get(f"/bookings/{booking_code}")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data["booking_code"], booking_code)

    def test_delete_booking(self):
        booking_code = "test-booking-code"  
        response = self.client.delete(f"/bookings/{booking_code}")
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    import unittest
    unittest.main()
