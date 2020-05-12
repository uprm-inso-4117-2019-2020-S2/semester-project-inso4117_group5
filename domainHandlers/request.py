from flask import jsonify
from domainDAO import requestDAO
import re
import json

#AUTHOR: Javier Ortiz

class RequestHandler:
    def createrequestDict(self,row):
        request = {}
        #cant be negative
        request['rid'] = row[0]
        #request requester (foreign key) (must be bigger than 0)
        request['rtitle'] = row[1]
        #request provider (same as above)
        request['rdescription'] = row[2]
        #supplies (Dictionary)
        request['rlocation'] = row[3]
        #string
        request['ruser'] = row[4]
        #int (enum)
        request['rstatus'] = row[5]
        #
        request['rresources'] = row[6]

        return request

        #making sure a valid formated request was given, using order provided by the dictionary above
    def validateRequest(self,request):
        if request[0] < 0:
            return False
        elif request[1] < 0:
            return False
        elif request[2] < 0:
            return False
        elif not isinstance(request[3], dict):
            return False
        elif len(request[4]) > 21:
            return False
        elif request[5] < 0 or request[5] > 3:
            return False
        else:
            return True

    def validateRequestJSON(self,requestJSON):
        #turn json to dictionary
        request = json.loads(requestJSON)
        if request['uid'] < 0:
            return False
        elif request['trequester'] < 0:
            return False
        elif request['tprovider'] < 0:
            return False
        elif not isinstance(request['tsupplies'], dict):
            return False
        elif len(request['ulocation']) > 21:
            return False
        elif request['tstatus'] < 0 or request['tstatus'] > 3:
            return False
        else:
            return True



    #we should make a query for the request id and requestname to validate
    # def verify_if_request_exists(self,uid):
    #TODO
    # def get_all_requests():
    
    # def get_request_by_id(self, uid: int):
    # get request by location
    # get request by status: pending, fuffilied y unfufilled
    # def insert_request(self, json_input):
