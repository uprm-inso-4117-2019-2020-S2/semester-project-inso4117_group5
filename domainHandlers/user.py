from flask import jsonify
from domainDAO.userDAO import UserDAO
import re
import json

#AUTHOR: Guillermo
#The User Handler will be called in the main and will be responsible for handling front-end and back-end interactions.
#The first methods implemented are meant to test the db-interacion that would ocurr through the helpthehomies main
#and our domain. We will reicive a request for information and we will supply it by asking the Data access object (DAO)
#for the information wanted, creating a dictionarry and assing it off as json file bak to the main.


class UserHandler:
    def createUserDict(self,row):
        user = {}
        #cant be negative
        user['uid'] = row[0]
        #limited to 21 chars
        user['uuser'] = row[1]
        #limited to 21 numbers and cap
        user['upassword'] = row[2]
        #email format
        user['uemail'] = row[3]
        #phone format
        user['uphone'] = row[4]
        #limited to 21
        # user['ulocation'] = row[5]
        # #float value
        # user['urating'] = row[6]

        return user

        #making sure a valid formated user was given, using order provided by the dictionary above
    def validateUser(self,user):
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

    def validateUserJSON(self,userJSON):
        #turn json to dictionary
        # user =
        if user['uid'] < 0:
            return False
        elif len(user['uusername']) > 21:
            return False
        elif not re.match(r'[A-Za-z0-9@#$%^&+=]{8,21}', user['upassword']):
            return False
        elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", user['uemail']):
            return False
        elif not re.match(r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$', user['uphone']):
            return False
        elif len(user['ulocation']) > 21:
            return False
        elif user['urating'] > 1:
            return False
        else:
            return True



    #we should make a query for the user id and username to validate
    # def verifyIfUserExists(self,uid):

    def getAllUsers(self):
        try:
            users = UserDAO().get_all_users()
            results = list()
            for row in users:
                results.append(self.createUserDict(row))
            return jsonify(Users=results)
        except:
            return jsonify(message="Server error!"), 500
