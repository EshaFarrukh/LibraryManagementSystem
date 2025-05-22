import unittest
from services.auth import login_user

class TestAuthService(unittest.TestCase):

    def test_valid_login(self):
        result = login_user("admin", "admin123")
        self.assertTrue(result)

    def test_invalid_login(self):
        result = login_user("wrong", "user")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()