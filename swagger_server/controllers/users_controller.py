import connexion
import six

from swagger_server.models.book_item import BookItem  # noqa: E501
from swagger_server.models.guest_item import GuestItem  # noqa: E501
from swagger_server import util

def delete(booking_code):  # noqa: E501
    """Unregister from an event

     # noqa: E501

    :param booking_code: booking code
    :type booking_code: 

    :rtype: None
    """
    return 'do some magic!'

def get_event_enrolled(booking_code):  # noqa: E501
    """Get a user enrolled by userID

     # noqa: E501

    :param booking_code: booking code
    :type booking_code: str

    :rtype: BookItem
    """
    return 'do some magic!'


def post_book(event_id, body=None):  # noqa: E501
    """Book a user on an event

     # noqa: E501

    :param event_id: id of an event
    :type event_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: BookItem
    """
    if connexion.request.is_json:
        body = GuestItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

def get_event_by_id(id):  # noqa: E501
    """Get a specific event by ID

     # noqa: E501

    :param id: ID of the event to retrieve
    :type id: 

    :rtype: EventItem
    """
    return 'do some magic!'

def search_events():  # noqa: E501
    """searches events

    By passing in the appropriate options, you can search for available events in the system  # noqa: E501


    :rtype: List[EventItem]
    """
    return 'do some magic!'
