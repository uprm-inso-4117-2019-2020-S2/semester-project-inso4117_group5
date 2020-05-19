from flask import jsonify, session, Flask
import unittest
import json
import random
import sys
from domainHandlers.request import RequestHandler
from domainDAO.requestDAO import RequestDAO
from domainDAO.userDAO import UserDAO
sys.path.append("..")  # to work with these imports


class UserHandlerTestCase(unittest.TestCase):
    # unit tests for validating user operations
    def setUp(self):
        self.r1 = [1, 'Toilet Paper', 'this is NOT a description', 'home', 'Requesting', 1]
        self.r2 = [2, 'Hand Sanitizer', 'this MAY be a decription', 'Maya', 'Provided', 3]
        self.r3 = [3, 'Food', 'this is POSSIBLY a description', 'laCalle', 'Provided', 1]
        self.r4 = [4, 'send help pls', 'this is ME DOING a description', 'home', 'Requesting', 3]
        self.r5 = [5, 'beer', 'this is JUST a description', 'bar', 'Requesting', 4]
        self.requests: list = [self.r1, self.r2, self.r3, self.r4, self.r5]
        self.user1 = [1, 'Morsa', 'faces4444', 'morsa@gmail.com', '7878598899']
        self.keys = ['rid', 'rtitle', 'rdescription', 'rlocation', 'rstatus', 'ruser']
        self.rh = RequestHandler()
        self.dao = RequestDAO()
        self.daoUSER = UserDAO()
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
        with self.app.app_context():
            uid = self.daoUSER.insert_user(self.user1[1], self.user1[2], self.user1[3], self.user1[4])
            for r in self.requests:
                r[5] = uid
                rid = self.dao.insert_request(r[1], r[2], r[3], r[4], r[5])
                request = self.rh.get_request_by_uid(uid)[0].json["Requests"]
                r[0] = rid
                self.assertIn(dict(zip(self.keys, r)), request)
            print("DELETED", self.daoUSER.delete_user_by_id(uid))

    def test_get_requests_by_user_status(self):
        with self.app.app_context():
            uid = self.daoUSER.insert_user(self.user1[1], self.user1[2], self.user1[3], self.user1[4])
            for r in self.requests:
                r[5] = uid
                rid = self.dao.insert_request(r[1], r[2], r[3], r[4], r[5])
                request = self.rh.get_requests_by_user_status(rid=r[5], status=r[4])[0].json["Requests"]
                r[0] = rid
                self.assertIn(dict(zip(self.keys, r)), request)
            print("DELETED", self.daoUSER.delete_user_by_id(uid))

    def test_insert_request(self):
        with self.app.app_context():
            uid = self.daoUSER.insert_user(self.user1[1], self.user1[2], self.user1[3], self.user1[4])
            for r in self.requests:
                r[5] = uid
                rid = self.dao.insert_request(r[1], r[2], r[3], r[4], r[5])
                request = self.rh.get_all_requests()[0].json["Requests"]
                r[0] = rid
                self.assertIn(dict(zip(self.keys, r)), request)
            print("DELETED", self.daoUSER.delete_user_by_id(uid))

    def test_delete_request_by_id(self):
        with self.app.app_context():
            uid = self.daoUSER.insert_user(self.user1[1], self.user1[2], self.user1[3], self.user1[4])
            for r in self.requests:
                r[5] = uid
                rid = self.dao.insert_request(r[1], r[2], r[3], r[4], r[5])
                r[0] = rid
                self.rh.delete_request_by_id(r[0])
                request = self.rh.get_all_requests()[0].json["Requests"]
                self.assertNotIn(dict(zip(self.keys, r)), request)
            print("DELETED", self.daoUSER.delete_user_by_id(uid))

    def test_get_request_by_location(self):
        with self.app.app_context():
            uid = self.daoUSER.insert_user(self.user1[1], self.user1[2], self.user1[3], self.user1[4])
            for r in self.requests:
                r[5] = uid
                rid = self.dao.insert_request(r[1], r[2], r[3], r[4], r[5])
                request = self.rh.get_request_by_location(r[3])[0].json["Requests"]
                r[0] = rid
                self.assertIn(dict(zip(self.keys, r)), request)
            print("DELETED", self.daoUSER.delete_user_by_id(uid))

    def test_get_request_by_status(self):
        with self.app.app_context():
            uid = self.daoUSER.insert_user(self.user1[1], self.user1[2], self.user1[3], self.user1[4])
            for r in self.requests:
                r[5] = uid
                rid = self.dao.insert_request(r[1], r[2], r[3], r[4], r[5])
                request = self.rh.get_request_by_status(r[4])[0].json["Requests"]
                r[0] = rid
                self.assertIn(dict(zip(self.keys, r)), request)
            print("DELETED", self.daoUSER.delete_user_by_id(uid))

    # def test_update_request_by_id(self):
    #     with self.app.app_context():
    #         self.dao.update_request_by_id(rid=3, rtitle=self.r1[1], rdescription=self.r1[2], rlocation=self.r1[3],
    #                                       rstatus=self.r1[4], ruser=6)
    #         pass


if __name__ == "__main__":
    unittest.main()
