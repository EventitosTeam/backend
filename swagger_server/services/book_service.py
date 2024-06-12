from swagger_server.schemas.book_schema import BookSchema
from swagger_server.repositories.book_repository import BookRepository

book_schema = BookSchema()
book_repository = BookRepository()

class BookService:

    def add_event_book(self, book):
        # event = event_schema.load(body)
        # return event_repository.create(event)
        book_repository.create(book)
        return book_schema.dump(book)