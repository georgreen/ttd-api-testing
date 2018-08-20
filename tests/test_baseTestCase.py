from unittest import TestCase
from app import create_app
import os
import json

class BaseTestCase(TestCase):

    def setUp(self):
        """Configure test enviroment."""
        os.environ['APP_SETTINGS'] = 'Testing'
        self.app = create_app("Testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.test_client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()


class PhoneBookTestCase(BaseTestCase):
    def test_get_contact_unexpected_input(self):
        """
        Example: {}, []
        """
        results = self.test_client.get('/api/v1/phonebook?user_name=[]')
        results_payload = json.loads(results.data)

        self.assertEqual(results.status_code, 400)
        self.assertEqual(results_payload['message'], 'Bad data')

    def test_get_contact_normal(self):
        """
        Example: "normal"
        """
        results = self.test_client.get('/api/v1/phonebook?user_name=normal')
        results_payload = json.loads(results.data)

        self.assertEqual(results.status_code, 200)
        self.assertEqual(results_payload['message'], 'Successfully retrieved')

    def test_get_contact_unexpected_boundary(self):
        """
        Example: '', ' '
        """
        results = self.test_client.get('/api/v1/phonebook?user_name=""')
        results_payload = json.loads(results.data)

        self.assertEqual(results.status_code, 400)
        self.assertEqual(results_payload['message'], 'Bad data')

    def test_get_contact_unexpected_edgecase(self):
        """
        Example: "      ", "   ?", " '' "
        """
        results = self.test_client.get('/api/v1/phonebook?user_name="  ?"')
        results_payload = json.loads(results.data)

        self.assertEqual(results.status_code, 400)
        self.assertEqual(results_payload['message'], 'Bad data')
