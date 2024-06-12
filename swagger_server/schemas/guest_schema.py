from marshmallow import Schema, fields, post_load, post_dump
from swagger_server.models.guest_item import GuestItem

class GuestSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    dni = fields.String(required=True)

    @post_load
    def make_event(self, data, **kwargs):
        return GuestItem(**data)
    
    SKIP_VALUES = set([None, ""])
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items()
            if value not in self.SKIP_VALUES
        }