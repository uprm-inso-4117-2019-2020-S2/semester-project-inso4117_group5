import unittest
import os
import sys

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(basedir)  # to work with these imports
from config import app

#
#Author: Javier Ortiz
#

class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass


###############
#### tests ####
###############

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 404)

    def test_profile_page_no_login(self):
        #not logged in
        response = self.app.get('/HTH/profile')
        print(response)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
