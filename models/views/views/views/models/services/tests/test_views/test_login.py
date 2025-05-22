import unittest
import tkinter as tk
from views.login import LoginWindow

class TestLoginUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = LoginWindow(self.root)

    def test_username_field_exists(self):
        self.assertIsNotNone(self.app.username_entry)

    def test_password_field_exists(self):
        self.assertIsNotNone(self.app.password_entry)

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()