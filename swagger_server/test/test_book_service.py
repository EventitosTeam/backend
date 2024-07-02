import unittest
import os
import sys
from unittest.mock import patch, MagicMock
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from swagger_server.test.base_test import BaseTestCase
from swagger_server.services.book_service import BookService

class TestBookService(BaseTestCase):

    @patch('swagger_server.services.book_service.send_mail')
    def test_add_event_book(self, mock_send_mail):
        mock_send_mail.return_value = True
        event_id = 1
        book = {'user': "{'name': 'Test User', 'email': 'testuser@example.com'}"}
        result = self.book_service.add_event_book(book, event_id)
        self.assertRegex(str(result), r"<BookItem \d+>")
        mock_send_mail.assert_called_once_with("testuser@example.com", "Evento pendiente", "Se ha agregado a la lista de invitados, codigo de invitacion: ")

    @patch('swagger_server.repositories.book_repository.BookRepository.find_one')
    def test_get_event_enrolled(self, mock_find_one):
        booking_code = "test_booking_code"
        expected_booking = {
            "booking_code": booking_code,
            "registered": True,
            "user": {"email": "testuser@example.com"},
            "event_id": 1
        }
        mock_find_one.return_value = expected_booking
        result = self.book_service.get_event_enrolled(booking_code)
        self.assertEqual(result, expected_booking)

    @patch('swagger_server.repositories.book_repository.BookRepository.delete')
    def test_delete_booking(self, mock_delete):
        booking_code = "test_booking_code"
        mock_delete.return_value = True
        result = self.book_service.delete_booking(booking_code)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()