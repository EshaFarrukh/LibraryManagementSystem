import unittest
from models.book import add_book, remove_book, load_books

class TestBookUI(unittest.TestCase):

    def test_add_book(self):
        add_book("Test Book", "Author", 2)
        books = load_books()
        titles = [book['title'] for book in books]
        self.assertIn("Test Book", titles)

    def test_remove_book(self):
        add_book("Temp Book", "Temp Author", 1)
        removed = remove_book("Temp Book")
        self.assertTrue(removed)

if __name__ == "__main__":
    unittest.main()