from flask import jsonify, session, flash
from passlib.hash import sha256_crypt
from domainDAO.providerDAO import ProviderDAO
import re
import json


# AUTHOR: Fernando



class ProviderHandler:
    def createProviderDict(self, row):
        provider = {}
        # cant be negative (provider id)
        provider['pid'] = row[0]
        # user id (provider that is fulfilling request)
        provider['puser'] = row[1]
        # request id (request that is being fulfilled)
        provider['prequest'] = row[2]

        return provider

    def get_all_providers(self):
        try:
            providers = ProviderDAO().get_all_providers()
            results = list()
            for row in providers:
                results.append(self.createProviderDict(row))
            return jsonify(Providers=results)
        except:
            return jsonify(ERROR="Server error!"), 500

    def get_provider_by_id(self, pid: int):
        try:
            provider = ProviderDAO().get_provider_by_id(pid)
            if provider:
                return jsonify(Provider=self.createProviderDict(provider))
            else:
                return jsonify(ERROR="Provider Not Found"), 404
        except:
            return jsonify(ERROR="Handler Error"), 500

    def get_provider_by_request_id(self, prequest: int):
        try:
            provider = ProviderDAO().get_provider_by_request_id(prequest)
            if provider:
                return jsonify(Provider=self.createProviderDict(provider))
            else:
                return jsonify(ERROR="Provider Not Found"), 404
        except:
            return jsonify(ERROR="Handler Error"), 500

    def get_provider_by_user_id(self, puser: int):
        try:
            provider = ProviderDAO().get_provider_by_user_id(puser)
            if provider:
                return jsonify(Provider=self.createProviderDict(provider))
            else:
                return jsonify(ERROR="Provider Not Found"), 404
        except:
            return jsonify(ERROR="Handler Error"), 500

    def insert_provider(self, json_input):
        if len(json_input) != 2:  # check if there are sufficient elements in input
            return jsonify(Error="Malformed insert provider request"), 400
        try:  # check parameters are valid
            puser = json_input['puser']
            prequest = json_input['prequest']
        except:
            return jsonify(Error="Unexpected attributes in insert provider request"), 400
        try:
            if puser and prequest:
                dao = ProviderDAO()
                pid = dao.insert_provider(puser, prequest)
            else:
                return jsonify(Error="One or more attribute is empty"), 400
        except:
            return jsonify(Error="Provider insertion failed horribly."), 400
        # Finally returns an user dict of the inserted user.
        return jsonify(Provider=self.createProviderDict([pid, puser, prequest])), 201

    def delete_provider(self, puser: int):
        try:
            provider = ProviderDAO().delete_provider_by_id(puser)
            if provider:
                return jsonify(Provider="Provider was successfully deleted.")
            else:
                return jsonify(ERROR="Provider Not Found"), 404
        except:
            return jsonify(ERROR="Handler Error"), 500

    def update_provider(self, pid: int, json_input):
        if len(json_input) != 2 or not pid:  # check if there are sufficient elements in input
            return jsonify(Error="Malformed insert provider request"), 400
        try:  # check parameters are valid
            puser = json_input['puser']
            prequest = json_input['prequest']
        except:
            return jsonify(Error="Unexpected attributes in insert provider request"), 400
        try:
            if puser and prequest:
                dao = ProviderDAO()
                pid = dao.update_provider_by_id(pid, puser, prequest)
            else:
                return jsonify(Error="One or more attribute is empty"), 400
        except:
            return jsonify(Error="Provider update failed horribly."), 400
        # Finally returns an user dict of the inserted user.
        return jsonify(Provider=self.createProviderDict([pid, puser, prequest])), 201
