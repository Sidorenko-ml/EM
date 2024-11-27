import unittest
import os
from library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.books = []  # Очистить список книг перед каждым тестом
        self.library.save_books()  # Сохранить очищенный список

    def tearDown(self):
        if os.path.exists(self.library.books_file):
            os.remove(self.library.books_file)  # Удалить файл после тестов

    def test_add_book(self):
        self.library.add_book("Test Book", "Test Author", 2024)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0]['title'], "Test Book")

    def test_remove_book(self):
        self.library.add_book("Test Book", "Test Author", 2024)
        book_id = self.library.books[0]['id']
        self.library.remove_book(book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_search_books(self):
        self.library.add_book("Test Book", "Test Author", 2024)
        results = self.library.search_books("Test")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], "Test Book")

    def test_change_status(self):
        self.library.add_book("Test Book", "Test Author", 2024)
        book_id = self.library.books[0]['id']
        self.library.change_status(book_id, "выдана")
        self.assertEqual(self.library.books[0]['status'], "выдана")


if __name__ == '__main__':
    unittest.main()