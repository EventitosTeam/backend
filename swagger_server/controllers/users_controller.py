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
bookings = Blueprint('bookings', __name__)
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

@bookings.route('/<string:booking_code>', methods=['GET'])
def get_event_enrolled(booking_code):  # noqa: E501
    """Get a user enrolled by userID

     # noqa: E501

    :param booking_code: booking code
    :type booking_code: str

    :rtype: BookItem
    """
    return book_schema.dump(book_service.get_event_enrolled(booking_code))
    return 'do some magic!'

# /events/{event_id}/bookings
@events.route('/<int:event_id>/bookings', methods=['POST'])
def post_book(event_id):  # noqa: E501
    user = request.get_json()
    book = {
        "user": str(user),
        "event_id": event_id
    }
    # return book_service.add_event_book(book, event_id)
    return book_schema.dump(book_service.add_event_book(book, event_id))
    # return ""

@events.route('/<int:id>', methods=['GET'])
def get_event_by_id(id):  # noqa: E501
    """Get a specific event by ID

     # noqa: E501

    :param id: ID of the event to retrieve
    :type id: 

    :rtype: EventItem
    """
    return event_schema.dump(event_service.get_event_by_id(id))

@events.route('/', methods=['POST'])
def create_event():
    event = event_schema.load(request.get_json())
    # event = {}
    # print(event)
    # return "ok", 200
    # return event
    return event_service.add_event(event)

@events.route('/', methods=['GET'])
def search_events():  # noqa: E501
    """searches events

    By passing in the appropriate options, you can search for available events in the system  # noqa: E501


    :rtype: List[EventItem]
    """
    return event_schema.dump(event_service.get_events(), many=True)
