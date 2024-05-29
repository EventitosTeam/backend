# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.book_item import BookItem  # noqa: E501
from swagger_server.models.guest_item import GuestItem  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_delete(self):
        """Test case for delete

        Unregister from an event
        """
        response = self.client.open(
            '/SFENSKE/EventsApi/1.0.0/bookings/{bookingCode}'.format(booking_code='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_event_enrolled(self):
        """Test case for get_event_enrolled

        Get a user enrolled by userID
        """
        response = self.client.open(
            '/SFENSKE/EventsApi/1.0.0/bookings/{bookingCode}'.format(booking_code='booking_code_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_book(self):
        """Test case for post_book

        Book a user on an event
        """
        body = GuestItem()
        response = self.client.open(
            '/SFENSKE/EventsApi/1.0.0/events/{event_id}/bookings'.format(event_id='event_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
