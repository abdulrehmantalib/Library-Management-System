import unittest
from app.model.login_model import User


class TestUserModel(unittest.TestCase):

    def test_correct_credentials(self):
        user = User()
        self.assertTrue(user.check_credentials("admin", "admin123"))

    def test_wrong_username(self):
        user = User()
        self.assertFalse(user.check_credentials("wrong", "admin123"))

    def test_wrong_password(self):
        user = User()
        self.assertFalse(user.check_credentials("admin", "wrong"))
