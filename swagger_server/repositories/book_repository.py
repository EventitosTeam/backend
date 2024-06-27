from swagger_server.database import db
from .base_repository import Create, Read, Delete, Update
from swagger_server.models import BookItem

class BookRepository(Create, Read, Delete):

    def __init__(self):
        self.model = BookItem

    def create(self, object):
        db.session.add(object)
        db.session.commit()
        return object

    def find_all(self):
        return self.model.query.all()

    def find_one(self, booking_code):
        return self.model.query.filter_by(booking_code=booking_code).first()

    def delete(self, booking_code):
        obj = self.find_one(booking_code)
        if obj:
            db.session.delete(obj)
            db.session.commit()
            return True
        return False