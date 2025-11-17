import unittest
import tkinter as tk
from app.views.login_view import LoginView


class TestLoginView(unittest.TestCase):

    def test_view_renders(self):
        root = tk.Tk()
        view = LoginView(root, lambda: None)

        # Check widget created
        self.assertIsNotNone(view)

        # Check username/password fields exist
        self.assertTrue(hasattr(view, "username_entry"))
        self.assertTrue(hasattr(view, "password_entry"))

        root.destroy()
