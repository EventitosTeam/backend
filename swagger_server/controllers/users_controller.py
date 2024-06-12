import connexion
import six

from swagger_server.models.book_item import BookItem  # noqa: E501
from swagger_server.models.guest_item import GuestItem  # noqa: E501
from swagger_server import util
from flask import Blueprint, request
from swagger_server.schemas.book_schema import BookSchema
from swagger_server.services.book_service import BookService
from swagger_server.schemas.event_schema import EventSchema
from swagger_server.services.event_service import EventService
from flask import request, jsonify

events = Blueprint('events', __name__)
book_service = BookService()
book_schema = BookSchema()

event_service = EventService()
event_schema = EventSchema()

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

@events.route('/{event_id}/booking', methods=['POST'])
def post_book(event_id, body=None):  # noqa: E501
    book = ""
    return ""


def get_event_by_id(id):  # noqa: E501
    """Get a specific event by ID

     # noqa: E501

    :param id: ID of the event to retrieve
    :type id: 

    :rtype: EventItem
    """
    return 'do some magic!'

@events.route('/', methods=['POST'])
def create_event():
    event = event_schema.load(request.get_json())
    return event_service.add_event(event)

@events.route('/', methods=['GET'])
def search_events():  # noqa: E501
    """searches events

    By passing in the appropriate options, you can search for available events in the system  # noqa: E501


    :rtype: List[EventItem]
    """
    return [
        {
            "date": "date",
            "desciption": "desciption",
            "eventPlaceLat": "eventPlaceLat",
            "name": "name",
            "eventPlaceLon": "eventPlaceLon",
            "peopleLimit": 0
        }
    ], 200
