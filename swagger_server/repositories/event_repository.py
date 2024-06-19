from swagger_server.database import db
from .base_repository import Create, Read, Delete, Update
from swagger_server.models import EventItem

class EventRepository(Create, Read):

    def __init__(self):
        self.model = EventItem

    def create(self, object):
        db.session.add(object)
        db.session.commit()
        return object
    
    def find_all(self):
        return self.model.query.all()
    
    def find_one(self, id):
        return self.model.query.get(id)
    