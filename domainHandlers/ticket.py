from flask import jsonify
from domainDAO import ticketDAO
import re
import json

#AUTHOR: Javier Ortiz

class ticketHandler:
    def createTicketDict(self,row):
        ticket = {}
        #cant be negative
        ticket['uid'] = row[0]
        #ticket requester
        ticket['trequester'] = row[1]
        #ticket provider
        ticket['tprovider'] = row[2]
        #supplies (Dictionary)
        ticket['tsupplies'] = row[3]
        #string
        ticket['tlocation'] = row[4]
        #int (enum)
        ticket['tstatus'] = row[5]

        return ticket

    '''
    TODO the following is copied from the user handler. It needs to be converted for the tickets
    '''
    #     #making sure a valid formated ticket was given, using order provided by the dictionary above
    # def validateTicket(self,ticket):
    #     if ticket[0] < 0:
    #         return False
    #     elif len(ticket[1]) > 21:
    #         return False
    #     elif not re.match(r'[A-Za-z0-9@#$%^&+=]{8,21}', ticket[2]):
    #         return False
    #     elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", ticket[3]):
    #         return False
    #     elif not re.match(r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$', ticket[4]):
    #         return False
    #     elif len(ticket[5]) > 21:
    #         return False
    #     elif ticket[6] > 1:
    #         return False
    #     else:
    #         return True
    #
    # def validateTicketJSON(self,ticketJSON):
    #     #turn json to dictionary
    #     # ticket =
    #     if ticket['uid'] < 0:
    #         return False
    #     elif len(ticket['uticketname']) > 21:
    #         return False
    #     elif not re.match(r'[A-Za-z0-9@#$%^&+=]{8,21}', ticket['upassword']):
    #         return False
    #     elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", ticket['uemail']):
    #         return False
    #     elif not re.match(r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$', ticket['uphone']):
    #         return False
    #     elif len(ticket['ulocation']) > 21:
    #         return False
    #     elif ticket['urating'] > 1:
    #         return False
    #     else:
    #         return True



    #we should make a query for the ticket id and ticketname to validate
    # def verifyIfticketExists(self,uid):

    # def getAlltickets():
