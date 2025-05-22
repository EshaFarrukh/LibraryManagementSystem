import unittest
from models.lending import lend_book, get_active_lendings
from datetime import date, timedelta

class TestLending(unittest.TestCase):
    def test_lend_book(self):
        future_date = date.today() + timedelta(days=5)
        lend_book(1, "Test Member", future_date)
        lends = get_active_lendings()
        self.assertTrue(any(l['member_name'] == "Test Member" for l in lends))

if __name__ == "__main__":
    unittest.main()
