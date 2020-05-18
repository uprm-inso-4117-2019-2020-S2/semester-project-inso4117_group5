import unittest
import os
import sys
import random
from flask import session

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(basedir)  # to work with these imports
from helpthehomies import app
from domainHandlers.user import UserHandler

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
        self.app.get('/')#routes initializes session value

        self.new_user = {
            "uusername": str(random.randint(1000, 10000)),
            "upassword": "password",
            "uemail": "em@il.com",
            "uphone": str(1231231234)
        }

    # executed after each test
    def tearDown(self):
        with self.app as c:
            rv = c.post('/HTH/login', json={"uusername": self.new_user['uusername'],
            "upassword": self.new_user['upassword']})
            if session['logged_in']:
                uid = session['uid']
                UserHandler().delete_user_by_id(uid)


###############
#### tests ####
###############

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_profile_page_no_login(self):
        response = self.app.get('/HTH/profile')
        self.assertEqual(response.status_code, 302)

    def test_register_page_get(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_register_page_post(self):
        response = self.app.post('/register', json=self.new_user)
        self.assertEqual(response.status_code, 302)

    def test_login_page_get(self):
        response = self.app.get('/HTH/login')
        self.assertEqual(response.status_code, 200)

    def test_login_page_post(self):
        self.app.post('/register', json=self.new_user)#also logs u in

        response = self.app.post('/HTH/login', json={"uusername": self.new_user['uusername'],
        "upassword": self.new_user['upassword']})
        self.assertEqual(response.status_code, 302)

        response2 = self.app.post('/HTH/login', json={"uusername": self.new_user['uusername'],
        "upassword": "notthepassword"})
        self.assertEqual(response2.status_code, 200)

    def test_profile_page_with_login(self):
        self.app.post('/register', json=self.new_user)#this also logs u in

        response = self.app.get('/HTH/profile')

        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.app.post('/register', json=self.new_user)#this also logs u in

        response = self.app.get('/HTH/logout')

        self.assertEqual(response.status_code, 302)

    def test_helphommies_nonlogin(self):
        response = self.app.get('/helpsomehommies')
        self.assertEqual(response.status_code, 302)

    def test_helphommies_loggedin(self):
        self.app.post('/register', json=self.new_user)#this also logs u in

        #GET
        response = self.app.get('/helpsomehommies')
        self.assertEqual(response.status_code, 200)

        #POST
        response = self.app.post('/helpsomehommies', json=self.new_user)
        self.assertEquals(response.status_code, 400)

        #lets get that uid *sigh*
        uid = ""
        with self.app as c:
            rv = c.post('/HTH/login', json={"uusername": self.new_user['uusername'],
            "upassword": self.new_user['upassword']})
            uid = session['uid']

        #with acutal correct options
        options = {"rid":12,
        "rtitle": "t",
        "rdescription": "d",
        "rlocation": "l",
        "ruser": uid,
        "rstatus":"fulfilled"}

        response= self.app.post('/helpsomehommies', json=options)
        self.assertEquals(response.status_code, 200)

    def test_requests(self):
        response = self.app.get('/requests')
        self.assertTrue("Requests" in response.json)



if __name__ == "__main__":
    with app.test_request_context():
        unittest.main()
