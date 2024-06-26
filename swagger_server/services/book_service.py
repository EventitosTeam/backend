from swagger_server.schemas.book_schema import BookSchema
from swagger_server.repositories.book_repository import BookRepository
import uuid, ast, json
from swagger_server.mail.function import send_mail

book_schema = BookSchema()
book_repository = BookRepository()

class BookService:

    def add_event_book(self, book, event_id):
        book = book_schema.load(book)
        book.booking_code = str(uuid.uuid4()).replace("-", "").upper()
        print("ACA EL CODE: ", book)
        return book_repository.create(book)
    
    def get_event_enrolled(self, booking_code):
        return book_repository.find_one(booking_code)