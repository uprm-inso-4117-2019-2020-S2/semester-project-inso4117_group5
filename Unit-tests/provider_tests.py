from flask import jsonify, session, flash, Flask
import unittest
import json
import random
import sys

from domainDAO.providerDAO import ProviderDAO
from domainDAO.userDAO import UserDAO
from domainHandlers.provider import ProviderHandler
from domainHandlers.user import UserHandler

sys.path.append("..")  # to work with these imports
from helpthehomies import app

class ProviderHandlerTestCase(unittest.TestCase):
    # unit tests for validating user operations
    def setUp(self):

        self.ph = ProviderHandler()
        self.dao = ProviderDAO()
        self.new_provider = {
            "puser": 6,
            "prequest": 3,
        }
        self.new_provider2 = {
            "puser": 7,
            "prequest": 3,
        }
        self.new_provider3 = {
            "puser": 9,
            "prequest": 5,
        }
        self.app = Flask(__name__)
    #
    def test_get_all_providers(self):
        # will get a list of providers
        with self.app.app_context():
            result = json.loads(self.ph.get_all_providers().get_data())['Providers']
            self.assertTrue(len(result) >= 1)

    def test_get_provider_by_id(self):
        with self.app.app_context():
            result = json.loads(self.ph.get_all_providers().get_data())['Providers']
            first_provider = result[0]
            provider_result = json.loads(self.ph.get_provider_by_id(first_provider['pid']).get_data())['Provider']
            self.assertEqual(provider_result, first_provider)
            self.assertEqual(self.ph.get_provider_by_id(-1)[1], 404)

    def test_get_provider_by_request_id(self):
        with self.app.app_context():
            result = json.loads(self.ph.get_all_providers().get_data())['Providers']
            first_provider = result[0]
            provider_result = json.loads(self.ph.get_provider_by_request_id(first_provider['prequest']).get_data())['Provider']
            self.assertEqual(provider_result, first_provider)
            self.assertEqual(self.ph.get_provider_by_request_id(-1)[1], 404)

    def test_get_provider_by_user_id(self):
        with self.app.app_context():
            result = json.loads(self.ph.get_all_providers().get_data())['Providers']
            first_provider = result[0]
            provider_result = json.loads(self.ph.get_provider_by_user_id(first_provider['puser']).get_data())['Provider']
            self.assertEqual(provider_result, first_provider)
            self.assertEqual(self.ph.get_provider_by_user_id(-1)[1], 404)

    def test_insert_provider(self):
        with self.app.app_context():
            # Test for providing its own request
            result = self.ph.insert_provider(self.new_provider)
            self.assertEqual(result[1], 400)

            # Test for providing a request successfully
            result = self.ph.insert_provider(self.new_provider2)
            pid = json.loads(result[0].get_data())['Provider']['pid']
            self.assertEqual(result[1], 201)
            self.dao.delete_provider_by_id(pid)  # so test provider is not persisted

            # Test for unsuccessful parameters
            self.new_provider2.pop('puser')
            result2 = self.ph.insert_provider(self.new_provider2)
            self.assertEqual(result2[1], 400)  # provider should never enter db

    # def test_delete_provider(self):
    #     with self.app.app_context():
    #         self.dao.delete_provider_by_id(2)


if __name__ == "__main__":
    with app.test_request_context():
        unittest.main()
