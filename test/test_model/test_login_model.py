# tests/test_models/test_login_model.py

import pytest
from app.model.login_model import User


def test_correct_credentials():
    user = User()
    assert user.check_credentials("admin", "admin123") is True


def test_wrong_username():
    user = User()
    assert user.check_credentials("wrong", "admin123") is False


def test_wrong_password():
    user = User()
    assert user.check_credentials("admin", "wrongpass") is False
