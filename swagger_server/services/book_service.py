from swagger_server.schemas.book_schema import BookSchema
from swagger_server.repositories.book_repository import BookRepository
import uuid, ast, json
from swagger_server.mail.function import send_mail

book_schema = BookSchema()
book_repository = BookRepository()

class BookService:

    def add_event_book(self, book, event_id):
        book_str = book["user"]
        print("ACA EL BOOK: ",book_str)
        user_dict = ast.literal_eval(book_str)
        print("ACA LA DATA: ",user_dict)
        print(type(user_dict))
        user_json = json.dumps(user_dict)
        create_a_new_book = { "booking_code": str(uuid.uuid4()), "registered": False, "user": user_json, "event_id": event_id }
        booking_code = create_a_new_book["booking_code"]
        book = book_schema.load(create_a_new_book)
        # book = book_schema.load(book)
        sent = send_mail(user_json.email, "Evento pendiente", "Se ha agregado a la lista de invitados, codigo de invitación: ")
        return book_repository.create(book)
    
    def get_event_enrolled(self, booking_code):
        return book_repository.find_one(booking_code)