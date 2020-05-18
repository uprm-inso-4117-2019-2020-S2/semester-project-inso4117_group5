from flask import jsonify, session, Flask
import unittest
import json
import random
import sys
from domainHandlers.request import RequestHandler
from domainDAO.requestDAO import RequestDAO
sys.path.append("..")  # to work with these imports


class UserHandlerTestCase(unittest.TestCase):
    # unit tests for validating user operations
    def setUp(self):
        self.r1 = [1, 'Toilet Paper', 'this is NOT a description', 'home', 'Requesting', 1]
        self.r2 = [2, 'Hand Sanitizer', 'this MAY be a decription', 'Maya', 'Provided', 3]
        self.r3 = [3, 'Food', 'this is POSSIBLY a description', 'laCalle', 'Provided', 1]
        self.r4 = [4, 'send help pls', 'this is ME DOING a description', 'home', 'Requesting', 3]
        self.r5 = [5, 'beer', 'this is JUST a description', 'bar', 'Requesting', 4]

        self.keys = ['rid', 'rtitle', 'rdescription', 'rlocation', 'rstatus', 'ruser']
        self.rh = RequestHandler()
        self.dao = RequestDAO()
        self.app = Flask(__name__)

    def test_create_request_dict(self):
        self.assertDictEqual(dict(zip(self.keys, self.r1)), self.rh.create_request_dict(self.r1))
        self.assertDictEqual(dict(zip(self.keys, self.r2)), self.rh.create_request_dict(self.r2))
        self.assertDictEqual(dict(zip(self.keys, self.r3)), self.rh.create_request_dict(self.r3))
        self.assertDictEqual(dict(zip(self.keys, self.r4)), self.rh.create_request_dict(self.r4))
        self.assertDictEqual(dict(zip(self.keys, self.r5)), self.rh.create_request_dict(self.r5))

    def test_get_all_requests(self):
        with self.app.app_context():
            self.assertTrue(len(self.rh.get_all_requests()[0].json["Requests"]) > 1)

    def test_get_request_by_uid(self):
        try:
            pass
        except Exception as e:
            print(e)
            print("Insertion Failed")
        else:
            pass
        finally:
            pass
        pass

    # def test_validUser(self):
    #     self.assertTrue(self.uh.validateUser(self.user1))
    #     self.assertFalse(self.uh.validateUser(self.user2))
    #     self.assertTrue(self.uh.validateUser(self.user3))
    #     self.assertFalse(self.uh.validateUser(self.user4))
    #     self.assertFalse(self.uh.validateUser(self.user5))
    #     self.assertFalse(self.uh.validateUser(self.user6))
    #     self.assertFalse(self.uh.validateUser(self.user7))
    #
    # def test_validUserJSON(self):
    #     user1JSON = self.uh.createUserDict(self.user1)
    #     user2JSON = self.uh.createUserDict(self.user2)
    #     user3JSON = self.uh.createUserDict(self.user3)
    #     user4JSON = self.uh.createUserDict(self.user4)
    #     user5JSON = self.uh.createUserDict(self.user5)
    #     user6JSON = self.uh.createUserDict(self.user6)
    #     user7JSON = self.uh.createUserDict(self.user7)
    #
    #     self.assertTrue(self.uh.validateUserJSON(user1JSON))
    #     self.assertFalse(self.uh.validateUserJSON(user2JSON))
    #     self.assertTrue(self.uh.validateUserJSON(user3JSON))
    #     self.assertFalse(self.uh.validateUserJSON(user4JSON))
    #     self.assertFalse(self.uh.validateUserJSON(user5JSON))
    #     self.assertFalse(self.uh.validateUserJSON(user6JSON))
    #     self.assertFalse(self.uh.validateUserJSON(user7JSON))
    #
    # def test_get_all_users(self):
    #     # will get a list of users
    #     result = json.loads(self.uh.get_all_users())
    #     self.assertTrue(len(result['results']) > 1)
    #
    # def test_get_user_by_id(self):
    #     result = json.loads(self.uh.get_all_users())
    #     first_user = result['results'][0]
    #     user_result = json.loads(self.uh.get_user_by_id(first_user['uid']))['User']
    #     self.assertEqual(user_result, first_user)
    #     a_tuple = jsonify(ERROR="User Not Found"), 404
    #     self.assertEqual(self.uh.get_user_by_id(-1), a_tuple)
    #
    # def test_insert_user(self):
    #     result = self.uh.insert_user(self.new_user)
    #     uid = json.loads(result)['User']['uid']
    #     self.assertEqual(result[1], 201)
    #     self.dao.delete_user_by_id(uid)  # so test user is not persisted
    #
    #     self.new_user.pop('uusername')
    #     result2 = self.uh.insert_user(self.new_user)
    #     self.assertEqual(result2[1], 400)  # user should never enter db
    #
    # def test_do_logout(self):
    #     self.assertTrue(self.uh.do_logout())
    #     self.assertFalse(session['logged_in'])
    #
    # def test_do_register(self):
    #     # similar to the insert_user method
    #     result = self.uh.do_register(self.new_user)
    #     uid = json.loads(result)['User']['uid']
    #     self.assertEqual(result[1], 201)
    #     self.dao.delete_user_by_id(uid)  # so test user is not persisted
    #
    #     self.new_user.pop('uusername')
    #     result2 = self.uh.do_register(self.new_user)
    #     self.assertEqual(result2[1], 400)  # user should never enter db
    #
    # def test_do_login(self):
    #     # create new user
    #     result = self.uh.do_register(self.new_user)
    #     uid = json.loads(result)['User']['uid']
    #
    #     # test right password
    #     self.assertTrue(self.uh.do_login(self.new_user['uusername'], self.new_user['upassword']))
    #     self.assertTrue(session['logged_in'])
    #
    #     # test wrong password
    #     self.uh.do_logout()
    #     self.assertFalse(self.uh.do_login(self.new_user['uusername'], "notThePassword"))
    #
    #     # delete test user
    #     self.dao.delete_user_by_id(uid)  # so test user is not persisted


if __name__ == "__main__":
    unittest.main()
