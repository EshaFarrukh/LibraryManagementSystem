import unittest
from models.book import add_book, load_books

class TestInventory(unittest.TestCase):

    def test_inventory_load(self):
        add_book("Inventory Test", "Author X", 1)
        books = load_books()
        self.assertTrue(any(book["title"] == "Inventory Test" for book in books))

if _name_ == "_main_":
    unittest.main()