from swagger_server.database import db
from .base_repository import Create, Read, Delete, Update
from swagger_server.models import BookItem

class BookRepository(Create):

    def __init__(self):
        self.model = BookItem

    def create(self, object):
        db.session.add(object)
        db.session.commit()
        return object
    