from swagger_server.schemas.book_schema import BookSchema
from swagger_server.repositories.book_repository import BookRepository
import uuid

book_schema = BookSchema()
book_repository = BookRepository()

class BookService:

    def add_event_book(self, book, event_id):
        # book = {
        #     "booking_code": str(uuid.uuid4()),
        #     "registered": False,
        #     "user": str(user),
        #     # "event": user["event"]
        # }
        # event = event_schema.load(body)
        # return event_repository.create(event)
        # book_repository.create(book)
        # return book_schema.dump(book)
        # user["event_id"] = event_id
        create_a_new_book = { "booking_code": str(uuid.uuid4()), "registered": False, "user": book["user"], "event_id": event_id }
        book = book_schema.load(create_a_new_book)
        # book = book_schema.load(book)
        return book_repository.create(book)
    
    def get_event_enrolled(self, booking_code):
        return book_repository.find_one(booking_code)