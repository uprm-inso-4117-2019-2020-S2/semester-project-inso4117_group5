from flask import jsonify
from domainDAO import ticketDAO
import re
import json

#AUTHOR: Javier Ortiz

class TicketHandler:
    def createTicketDict(self,row):
        ticket = {}
        #cant be negative
        ticket['uid'] = row[0]
        #ticket requester (foreign key) (must be bigger than 0)
        ticket['trequester'] = row[1]
        #ticket provider (same as above)
        ticket['tprovider'] = row[2]
        #supplies (Dictionary)
        ticket['tsupplies'] = row[3]
        #string
        ticket['tlocation'] = row[4]
        #int (enum)
        ticket['tstatus'] = row[5]

        return ticket

        #making sure a valid formated ticket was given, using order provided by the dictionary above
    def validateTicket(self,ticket):
        if ticket[0] < 0:
            return False
        elif ticket[1] < 0:
            return False
        elif ticket[2] < 0:
            return False
        elif not isinstance(ticket[3], dict):
            return False
        elif not isinstance(ticket[4], str):
            return False
        elif ticket[5] < 0 or ticket[5] > 3:
            return False
        else:
            return True

    def validateTicketJSON(self,ticketJSON):
        #turn json to dictionary
        ticket = json.loads(ticketJSON)
        if ticket['uid'] < 0:
            return False
        elif ticket['trequester'] < 0:
            return False
        elif ticket['tprovider'] < 0:
            return False
        elif not isinstance(ticket['tsupplies'], dict):
            return False
        elif not isinstance(ticket['tlocation'], str):
            return False
        elif ticket['tstatus'] < 0 or ticket['tstatus'] > 3:
            return False
        else:
            return True



    #we should make a query for the ticket id and ticketname to validate
    # def verify_if_ticket_exists(self,uid):
    #TODO
    # def get_all_tickets():
    #
    # def get_ticket_by_id(self, uid: int):
    #
    # def insert_ticket(self, json_input):
