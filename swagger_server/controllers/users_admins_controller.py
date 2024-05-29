import connexion
import six

from swagger_server.models.event_item import EventItem  # noqa: E501
from swagger_server import util


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
