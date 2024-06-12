from swagger_server.database import db
from .base_repository import Create, Read, Delete, Update
from swagger_server.models import EventItem

class EventRepository(Create):

    def __init__(self):
        self.model = EventItem

    def create(self, object):
        db.session.add(object)
        db.session.commit()
        return object
    