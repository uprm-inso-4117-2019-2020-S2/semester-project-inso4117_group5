from flask import jsonify
from domainDAO import requestDAO
import re
import json

#AUTHOR: Javier Ortiz


class RequestHandler:
    def create_request_dict(self, row):
        return {'rid': row[0], 'rtitle': row[1], 'rdescription': row[2],
                'rlocation': row[3], 'ruser': row[4], 'rstatus': row[5]
                }

    # making sure a valid formated request was given, using order provided by the dictionary above
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
