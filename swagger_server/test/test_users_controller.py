import json
import os
import sys
import unittest
from unittest.mock import patch

# Ajustar el path para importar módulos desde el proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from swagger_server.test.base_test import BaseTestCase
from swagger_server.models.event_item import EventItem
from swagger_server.models.book_item import BookItem

class TestUsersController(BaseTestCase):

    @patch('swagger_server.services.book_service.send_mail')
    def test_post_book(self, mock_send_mail):
        mock_send_mail.return_value = True
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
        user = data["user"]
        self.assertEqual(data["event_id"], event_id)
        self.assertEqual(user["name"], user["name"])
        self.assertEqual(user["email"], user["email"])

    @patch('swagger_server.services.book_service.BookService.get_event_enrolled')
    def test_get_event_enrolled(self, mock_get_event_enrolled):
        booking_code = "test-booking-code"
        mock_booking = BookItem(
            booking_code=booking_code,
            registered=False,
            user={"name": "Test User", "email": "testuser@example.com"},
            event_id=1
        )
        mock_get_event_enrolled.return_value = mock_booking

        response = self.client.get(f"/bookings/{booking_code}")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data["booking_code"], booking_code)

    def test_delete_booking(self):
        booking_code = "test-booking-code"
        response = self.client.delete(f"/bookings/{booking_code}")
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
