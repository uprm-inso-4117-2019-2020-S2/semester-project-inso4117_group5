from flask import jsonify, session
import unittest
import json
import random
from domainHandlers.user import UserHandler
from domainDAO.userDAO import UserDAO

class UserHandlerTestCase(unittest.TestCase):
#unit tests for validating user operations
    def __init__(self):
        self.user1 = [1,'Morsa','faces4444','morsa@gmail.com','7878598899','Carolina',.99]
        self.user2 = [2,'Javier','L','morsagmail.com','787888999','Uganda',.23]
        self.user3 = [3,'Morsa','TryHard22','morsaworker@gmail.com','939-787-7799','Ivory Coast',.75]
        self.user4 = [4,'Walrus','Paul','loquito99@gmail.com','787/123/4567','Maya',-.99]
        self.user5 = [5,'Morsa','','morsa@gmail.com','7844445599','Quebra',.99]
        self.user6 = [6,'','lol','morsa@gmail.com','7844445599','Quebra',.99]
        self.user7 = [7,'Juan','lol','morsa@gmail.com','7844445599','22',.99]

    def setUp(self):
        self.uh = UserHandler()
        self.dao = UserDAO()
        self.new_user = {
        "uusername": str(int(random() ** 1000)),
        "upassword": "password",
        "uemail": "em@il.com",
        "uphone": str(1231231234)
        }

    def test_validUser(self):
        self.assertTrue(self.uh.validateUser(self.user1))
        self.assertFalse(self.uh.validateUser(self.user2))
        self.assertTrue(self.uh.validateUser(self.user3))
        self.assertFalse(self.uh.validateUser(self.user4))
        self.assertFalse(self.uh.validateUser(self.user5))
        self.assertFalse(self.uh.validateUser(self.user6))
        self.assertFalse(self.uh.validateUser(self.user7))

    def test_validUserJSON(self):
        user1JSON = self.uh.createUserDict(self.user1)
        user2JSON = self.uh.createUserDict(self.user2)
        user3JSON = self.uh.createUserDict(self.user3)
        user4JSON = self.uh.createUserDict(self.user4)
        user5JSON = self.uh.createUserDict(self.user5)
        user6JSON = self.uh.createUserDict(self.user6)
        user7JSON = self.uh.createUserDict(self.user7)

        self.assertTrue(self.uh.validateUserJSON(user1JSON))
        self.assertFalse(self.uh.validateUserJSON(user2JSON))
        self.assertTrue(self.uh.validateUserJSON(user3JSON))
        self.assertFalse(self.uh.validateUserJSON(user4JSON))
        self.assertFalse(self.uh.validateUserJSON(user5JSON))
        self.assertFalse(self.uh.validateUserJSON(user6JSON))
        self.assertFalse(self.uh.validateUserJSON(user7JSON))

    def test_get_all_users(self):
        #will get a list of users
        result = json.loads(self.uh.get_all_users())
        self.assertTrue(len(result['results']) > 1)

    def test_get_user_by_id(self):
        result = json.loads(self.uh.get_all_users())
        first_user = result['results'][0]
        user_result = json.loads(self.uh.get_user_by_id(first_user['uid']))['User']
        self.assertEqual(user_result, first_user)
        a_tuple = jsonify(ERROR="User Not Found"), 404
        self.assertEqual(self.uh.get_user_by_id(-1), a_tuple)

    def test_insert_user(self):
        result = self.uh.insert_user(self.new_user)
        uid = json.loads(result)['User']['uid']
        self.assertEqual(result[1], 201)
        self.dao.delete_user_by_id(uid)#so test user is not persisted

        self.new_user.pop('uusername')
        result2 = self.uh.insert_user(self.new_user)
        self.assertEqual(result2[1], 400)#user should never enter db

    def test_do_logout(self):
        self.assertTrue(self.uh.do_logout())
        self.assertFalse(session['logged_in'])

    def test_do_register(self):
        #similar to the insert_user method
        result = self.uh.do_register(self.new_user)
        uid = json.loads(result)['User']['uid']
        self.assertEqual(result[1], 201)
        self.dao.delete_user_by_id(uid)#so test user is not persisted

        self.new_user.pop('uusername')
        result2 = self.uh.do_register(self.new_user)
        self.assertEqual(result2[1], 400)#user should never enter db

    def test_do_login(self):
        #create new user
        result = self.uh.do_register(self.new_user)
        uid = json.loads(result)['User']['uid']

        #test right password
        self.assertTrue(self.uh.do_login(self.new_user['uusername'], self.new_user['upassword']))
        self.assertTrue(session['logged_in'])

        #test wrong password
        self.uh.do_logout()
        self.assertFalse(self.uh.do_login(self.new_user['uusername'],"notThePassword"))

        #delete test user
        self.dao.delete_user_by_id(uid)#so test user is not persisted


if __name__ == "__main__":
    unittest.main()
