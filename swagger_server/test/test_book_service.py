import unittest, os, sys
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from swagger_server.services.book_service import BookService

class TestBookService(unittest.TestCase):

    @patch('swagger_server.repositories.book_repository.BookRepository')
    def setUp(self, MockBookRepository):
        self.mock_book_repo = MockBookRepository()
        self.book_service = BookService(self.mock_book_repo)

    def test_get_all_books(self):
        self.mock_book_repo.get_all_books.return_value = []
        books = self.book_service.get_all_books()
        self.assertEqual(books, [])
        self.mock_book_repo.get_all_books.assert_called_once()

    def test_get_book_by_id(self):
        self.mock_book_repo.get_book_by_id.return_value = {'id': 1, 'title': 'Test Book'}
        book = self.book_service.get_book_by_id(1)
        self.assertEqual(book, {'id': 1, 'title': 'Test Book'})
        self.mock_book_repo.get_book_by_id.assert_called_once_with(1)

    def test_create_book(self):
        new_book = {'title': 'New Book'}
        self.mock_book_repo.create_book.return_value = {'id': 1, 'title': 'New Book'}
        book = self.book_service.create_book(new_book)
        self.assertEqual(book, {'id': 1, 'title': 'New Book'})
        self.mock_book_repo.create_book.assert_called_once_with(new_book)

    def test_update_book(self):
        updated_book = {'id': 1, 'title': 'Updated Book'}
        self.mock_book_repo.update_book.return_value = updated_book
        book = self.book_service.update_book(1, updated_book)
        self.assertEqual(book, updated_book)
        self.mock_book_repo.update_book.assert_called_once_with(1, updated_book)

    def test_delete_book(self):
        self.mock_book_repo.delete_book.return_value = True
        result = self.book_service.delete_book(1)
        self.assertTrue(result)
        self.mock_book_repo.delete_book.assert_called_once_with(1)

if __name__ == '__main__':
    unittest.main()
