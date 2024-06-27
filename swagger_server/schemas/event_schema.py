from marshmallow import Schema, fields, post_load, post_dump
from swagger_server.models.event_item import EventItem

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    desciption = fields.String(required=True)
    date = fields.String(required=True)
    event_place_lat = fields.String(required=True)
    event_place_lon = fields.String(required=True)
    people_limit = fields.Int(required=True)

    @post_load
    def make_event(self, data, **kwargs):
        return EventItem(**data)

    SKIP_VALUES = []
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items()
            if value not in self.SKIP_VALUES
        }