import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new.user = User(password="banana")

    def test_password_setter(self):
        self.assertTrue(self.new.user.verify_password('banana'))

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))
