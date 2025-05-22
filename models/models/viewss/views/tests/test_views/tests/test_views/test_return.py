import unittest
from models.lending import lend_book
from models.return import return_book
from datetime import date, timedelta

class TestReturn(unittest.TestCase):
    def test_return_book(self):
        future_date = date.today() - timedelta(days=2)
        lend_book(1, "Test User", future_date)
        lends = [l for l in lend_book.get_active_lendings() if l['member_name'] == "Test User"]
        fine = return_book(lends[-1]['id'])
        self.assertGreaterEqual(fine, 0)

if __name__ == "__main__":
    unittest.main()
