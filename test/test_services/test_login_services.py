import unittest
from app.services.login_services import authenticate


class TestAuthService(unittest.TestCase):

    def test_auth_success(self):
        self.assertTrue(authenticate("admin", "admin123"))

    def test_auth_fail_username(self):
        self.assertFalse(authenticate("wrong", "admin123"))

    def test_auth_fail_password(self):
        self.assertFalse(authenticate("admin", "badpass"))
