import connexion
import six

from swagger_server.models.book_item import BookItem  # noqa: E501
from swagger_server.models.guest_item import GuestItem  # noqa: E501
from swagger_server import util


from flask import Blueprint, request, jsonify
from swagger_server.schemas.book_schema import BookSchema
from swagger_server.services.book_service import BookService
from swagger_server.schemas.event_schema import EventSchema
from swagger_server.services.event_service import EventService
from swagger_server.mail.function import send_mail



events = Blueprint('events', __name__)
bookings = Blueprint('bookings', __name__)



book_service = BookService()
book_schema = BookSchema()
event_service = EventService()
event_schema = EventSchema()



@bookings.route('/<string:booking_code>', methods=['DELETE'])
def delete_booking(booking_code):
    """Unregister from an event"""
    result = book_service.delete_booking(booking_code)
    if result:
        return '', 204
    else:
        return jsonify({'detail': f'Booking with code {booking_code} not found'}), 404

@bookings.route('/<string:booking_code>', methods=['GET'])
def get_event_enrolled(booking_code):
    """Get a user enrolled by userID"""
    return book_schema.dump(book_service.get_event_enrolled(booking_code))

@events.route('/<int:event_id>/bookings', methods=['POST'])
def post_book(event_id):
    user = request.get_json()
    book = {
        "user": str(user),
        "event_id": event_id
    }
    # return book_service.add_event_book(book, event_id)
    # sent = send_mail(user["email"], "Evento pendiente", "Se ha agregado a la lista de invitados", {booking_code})
    
    return book_schema.dump(book_service.add_event_book(book, event_id))

@events.route('/<int:id>', methods=['GET'])
def get_event_by_id(id):
    """Get a specific event by ID"""
    event = event_service.get_event_by_id(id)
    if event:
        return event_schema.dump(event)
    else:
        return jsonify({'detail': f'Event with id {id} not found'}), 404

@events.route('/', methods=['POST'])
def create_event():
    event = event_schema.load(request.get_json())
    # event = {}
    # print(event)
    # return "ok", 200
    # return event
    return event_service.add_event(event)

@events.route('/', methods=['GET'])
def search_events():
    """searches events

    By passing in the appropriate options, you can search for available events in the system

    :rtype: List[EventItem]
    """
    return event_schema.dump(event_service.get_events(), many=True)
