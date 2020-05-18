from flask import jsonify
from domainDAO.requestDAO import RequestDAO
import json

# AUTHOR: Javier Ortiz and Ramón "El Duro" Rosado


class RequestHandler:
    @staticmethod
    def create_request_dict(row):
        return {'rid': row[0], 'rtitle': row[1], 'rdescription': row[2],
                'rlocation': row[3], 'rstatus': row[4], 'ruser': row[5]
                }

    # making sure a valid formatted request was given, using order provided by the dictionary above
    # def validateRequest(self, request):
    #     if request[0] < 0:
    #         return False
    #     elif request[1] < 0:
    #         return False
    #     elif request[2] < 0:
    #         return False
    #     elif not isinstance(request[3], dict):
    #         return False
    #     elif len(request[4]) > 21:
    #         return False
    #     elif request[5] < 0 or request[5] > 3:
    #         return False
    #     else:
    #         return True
    #
    # def validateRequestJSON(self,requestJSON):
    #     # turn json to dictionary
    #     request = json.loads(requestJSON)
    #     if request['uid'] < 0:
    #         return False
    #     elif request['trequester'] < 0:
    #         return False
    #     elif request['tprovider'] < 0:
    #         return False
    #     elif not isinstance(request['tsupplies'], dict):
    #         return False
    #     elif len(request['ulocation']) > 21:
    #         return False
    #     elif request['tstatus'] < 0 or request['tstatus'] > 3:
    #         return False
    #     else:
    #         return True

    # we should make a query for the request id and requestname to validate
    # def verify_if_request_exists(self,uid):

    def get_all_requests(self):
        try:
            requests = RequestDAO().get_all_requests()
            results = list()
            for row in requests:
                results.append(self.create_request_dict(row))
            return jsonify(Requests=results), 200
        except Exception as e:
            print(e)
            return jsonify(ERROR=e), 500

    def get_request_by_uid(self, uid: int):
        try:
            requests = RequestDAO().get_requests_by_user_id(uid)
            results = list()
            for row in requests:
                results.append(self.create_request_dict(row))
            return jsonify(Requests=results)
        except Exception as e:
            print(e)
            return jsonify(ERROR=e), 500

    def get_request_by_location(self, location: str):
        try:
            requests = RequestDAO().get_request_by_location(location)
            results = list()
            for row in requests:
                results.append(self.create_request_dict(row))
            return jsonify(Requests=results)
        except Exception as e:
            print(e)
            return jsonify(ERROR=e), 500

    def get_request_by_status(self, status: str):
        try:
            requests = RequestDAO().get_request_by_status(status)
            results = list()
            for row in requests:
                results.append(self.create_request_dict(row))
            return jsonify(Requests=results)
        except Exception as e:
            print(e)
            return jsonify(ERROR=e), 500

    def get_requests_by_user_status(self, rid: int, status: str):
        try:
            requests = RequestDAO().get_requests_by_user_status(rid, status)
            results = list()
            for row in requests:
                results.append(self.create_request_dict(row))
            return jsonify(Requests=results)
        except Exception as e:
            print(e)
            return jsonify(ERROR=e), 500

    # def insert(self, json_input):
    #     if session['logged_in']:  # check if there are sufficient elements in input
    #         try:  # check parameters are valid
    #             rid = json_input['rid']
    #             rtitle = json_input['rtitle']
    #             rdescription = json_input['rdescription']
    #             rlocation = json_input['rlocation']
    #             ruser = json_input['ruser']
    #             rstatus = json_input['rstatus']
    #
    #         except:
    #             return jsonify(Error="Unexpected attributes in insert user request"), 400
    #         try:
    #             if rid and rtitle and rdescription and rlocation and ruser and rstatus:
    #                 dao = RequestDAO().insert(rtitle,rdescription,rlocation,ruser)
    #
    #             else:
    #                 return jsonify(Error="One or more attribute is empty"), 400
    #         except:
    #             return jsonify(Error="Failed to make the request."), 400

    def insert_request(self, json_input):
        if len(json_input) != 5:  # check if there are sufficient elements in input
            return jsonify(Error="Malformed insert request"), 400
        try:  # check parameters are valid
            rtitle: str = json_input['rtitle']
            rdescription: str = json_input['rdescription']
            rlocation: str = json_input['rlocation']
            rstatus: str = json_input['rstatus']
            ruser: int = json_input['ruser']  # must be an int
        except Exception as e:
            print(e)
            return jsonify(Error="Unexpected attributes in insert request"), 400
        try:
            if rtitle and rdescription and rlocation and rstatus and ruser:
                rid: int = RequestDAO().insert_request(rtitle, rdescription, rlocation, rstatus, ruser)
            else:
                return jsonify(Error="One or more attribute is empty"), 400
        except Exception as e:
            print(e)
            return jsonify(Error="Request insertion failed horribly."), 400
        # Finally returns an request dict of the inserted request.
        return jsonify(Request=self.create_request_dict([rid, rtitle, rdescription, rlocation, rstatus, ruser])), 201

    def delete_request_by_id(self, rid: int):
        try:
            dao = RequestDAO()
            row = dao.get_request_by_id(rid)
            if not row:
                return jsonify(Error="Request" + str(rid) + " not found."), 404
            else:
                if dao.delete_request_by_id(rid) > 0:
                    return jsonify(DeletedRequest=self.create_request_dict(row)), 200
                else:
                    return jsonify(Error="Delete failed"), 404
        except Exception as e:
            print(e)
            return jsonify(ERROR=e), 500
