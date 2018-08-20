from unittest import TestCase
from app import create_app
import os

class BaseTestCase(TestCase):

    def setUp(self):
        """Configure test enviroment."""
        os.environ['APP_SETTINGS'] = 'Testing'
        self.app = create_app("Testing")
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()


class PhoneBookTestCase(BaseTestCase):
    def test_get_contact(self):
        pass
