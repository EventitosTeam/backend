from marshmallow import Schema, fields, post_load, post_dump
from swagger_server.models.book_item import BookItem
from .event_schema import EventSchema

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    booking_code = fields.String(required=True)
    registered = fields.Boolean(required=True)
    event = fields.Nested('EventSchema', required=True)

    @post_load
    def make_event(self, data, **kwargs):
        return BookItem(**data)
    
    SKIP_VALUES = set([None, ""])
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items()
            if value not in self.SKIP_VALUES
        }