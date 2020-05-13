from flask import jsonify, session
from passlib.hash import sha256_crypt
from domainDAO.userDAO import UserDAO
import re
import json


# AUTHOR: Guillermo
# The User Handler will be called in the main and will be responsible for handling front-end and back-end interactions.
# The first methods implemented are meant to test the db-interaction that would occur through the helpthehomies main
# and our domain. We will receive a request for information and we will supply it by asking the Data access object (DAO)
# for the information wanted, creating a dictionary and passing it off as json file bak to the main.


class UserHandler:
    def createUserDict(self, row):
        user = {}
        # cant be negative
        user['uid'] = row[0]
        # limited to 21 chars
        user['uuser'] = row[1]
        # limited to 21 numbers and cap
        user['upassword'] = row[2]
        # email format
        user['uemail'] = row[3]
        # phone format
        user['uphone'] = row[4]
        # float value
        user['urating'] = row[6]
        #


        return user

        # making sure a valid formated user was given, using order provided by the dictionary above

    def validateUser(self, user):
        if user[0] < 0:
            return False
        elif len(user[1]) > 21:
            return False
        elif not re.match(r'[A-Za-z0-9@#$%^&+=]{8,21}', user[2]):
            return False
        elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", user[3]):
            return False
        elif not re.match(r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$', user[4]):
            return False
        elif len(user[5]) > 21:
            return False
        elif user[6] > 1:
            return False
        else:
            return True

    def validateUserJSON(self, userJSON):
        # turn json to dictionary
        # user =
        if user['uid'] < 0:
            return False
        elif len(user['uusername']) > 21:
            return False
        elif not re.match(r'[A-Za-z0-9@#$%^&+=]{8,21}', user['upassword']):
            return False
        elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", user['uemail']):
            return False
        elif not re.match(r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$',
                          user['uphone']):
            return False
        elif len(user['ulocation']) > 21:
            return False
        elif user['urating'] > 1:
            return False
        else:
            return True

    # we should make a query for the user id and username to validate
    # def verifyIfUserExists(self,uid):

    def get_all_users(self):
        try:
            users = UserDAO().get_all_users()
            results = list()
            for row in users:
                results.append(self.createUserDict(row))
            return jsonify(Users=results)
        except:
            return jsonify(ERROR="Server error!"), 500

    def get_user_by_id(self, uid: int):
        try:
            user = UserDAO().get_user_by_id(uid)
            if user:
                return jsonify(User=self.createUserDict(user))
            else:
                return jsonify(ERROR="User Not Found"), 404
        except:
            return jsonify(ERROR="Handler Error"), 500

    def insert_user(self, json_input):
        if len(json_input) != 4:  # check if there are sufficient elements in input
            return jsonify(Error="Malformed insert user request"), 400
        try:  # check parameters are valid
            uusername = json_input['uusername']
            upassword = json_input['upassword']
            uemail = json_input['uemail']
            uphone = json_input['uphone']
        except:
            return jsonify(Error="Unexpected attributes in insert user request"), 400
        try:
            if uusername and upassword and uemail and uphone:
                dao = UserDAO()
                # if dao.get_user_by_email(uemail):  # checks if email exists in database. EMAILS MUST BE UNIQUE.
                #     return jsonify(Error="User with that email already exists. Please try a different one."), 400
                # elif dao.get_user_by_username(uusername):  # same but with username.
                #     return jsonify(Error="User with that username already exists. Please try a different one."), 400
                uid = dao.insert_user(uusername, upassword, uemail, uphone)
            else:
                return jsonify(Error="One or more attribute is empty"), 400
        except:
            return jsonify(Error="User insertion failed horribly."), 400
        # Finally returns an user dict of the inserted user.
        return jsonify(User=self.createUserDict([uid, uusername, upassword, uemail, uphone])), 201

    #TODO use session in these
    # def do_login(username, password):
    #     pass
    #
    @staticmethod
    def do_register(req):
        password = req['upassword']
        password_hash = sha256_crypt.encrypt(password)
        req['upassword'] = password_hash
        return UserHandler().insert_user(req)
