import sys
sys.path.insert(0, '../../')
from swagger_server.schemas.event_schema import EventSchema
from swagger_server.repositories.event_repository import EventRepository

event_schema = EventSchema()
event_repository = EventRepository()

class EventService:

    def add_event(self, event):
        event_repository.create(event)
        return event_schema.dump(event)
    
    def get_events(self):
        return event_repository.find_all()
    
    def get_event_by_id(self, id):
        return event_repository.find_one(id)