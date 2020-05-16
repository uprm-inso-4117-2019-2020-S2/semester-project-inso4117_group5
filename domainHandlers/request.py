from flask import jsonify
from domainDAO.requestDAO import RequestDAO
import re
import json

#AUTHOR: Javier Ortiz

class RequestHandler:
    def createRequestDict(self,row):
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

    def get_all_requests(self):
        try:
            requests = RequestDAO().get_all_requests()
            results = list()
            for row in requests:
                results.append(self.createRequestDict(row))
                print(row)
            return jsonify(requests=results)
        except:
            return jsonify(ERROR="Server error!"), 500


    def get_request_by_id(self, id: int):
        try:
            requests = RequestDAO.get_all_requests()
            results = list()
            for row in users:
                results.append(self.createRequestDict(row))
            return jsonify(requests=results)
        except:
            return jsonify(ERROR="Server error!"), 500

    def get_request_by_location(self, location):
        try:
            requests = RequestDAO.get_request_by_location(location)
            results = list()
            for row in users:
                results.append(self.createRequestDict(row))
            return jsonify(requests=results)
        except:
            return jsonify(ERROR="Server error!"), 500

    def get_request_by_status(self,status):
        try:
            requests = RequestDAO.get_request_by_status(status)
            results = list()
            for row in users:
                results.append(self.createRequestDict(row))
            return jsonify(requests=results)
        except:
            return jsonify(ERROR="Server error!"), 500

    def insert(self, json_input):
        if session['logged_in']:  # check if there are sufficient elements in input
            try:  # check parameters are valid
                rid = json_input['rid']
                rtitle = json_input['rtitle']
                rdescription = json_input['rdescription']
                rlocation = json_input['rlocation']
                ruser = json_input['ruser']
                rstatus = json_input['rstatus']

            except:
                return jsonify(Error="Unexpected attributes in insert user request"), 400
            try:
                if rid and rtitle and rdescription and rlocation and ruser and rstatus:
                    dao = RequestDAO().insert(rtitle,rdescription,rlocation,ruser)

                else:
                    return jsonify(Error="One or more attribute is empty"), 400
            except:
                return jsonify(Error="Failed to make the request."), 400
