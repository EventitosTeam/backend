from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.event_item import EventItem  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersAdminsController(BaseTestCase):
    """UsersAdminsController integration test stubs"""

    def test_get_event_by_id(self):
        """Test case for get_event_by_id

        Get a specific event by ID
        """
        response = self.client.open(
            '/SFENSKE/EventsApi/1.0.0/events/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_events(self):
        """Test case for search_events

        searches events
        """
        response = self.client.open(
            '/SFENSKE/EventsApi/1.0.0/events',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
