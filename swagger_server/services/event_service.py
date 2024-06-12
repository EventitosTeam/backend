from swagger_server.schemas.event_schema import EventSchema
from swagger_server.repositories.event_repository import EventRepository

event_schema = EventSchema()
event_repository = EventRepository()

class EventService:

    def add_event(self, event):
        event_repository.create(event)
        return event_schema.dump(event)