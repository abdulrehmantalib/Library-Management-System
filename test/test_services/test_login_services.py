# tests/test_views/test_login_view.py

import pytest
import tkinter as tk
from app.views.login_view import LoginView


def test_login_view_creation():
    root = tk.Tk()
    view = LoginView(root, lambda: None)

    # Ensure Tkinter frame created
    assert view is not None

    # Ensure username + password fields exist
    assert hasattr(view, "username_entry")
    assert hasattr(view, "password_entry")

    root.destroy()
