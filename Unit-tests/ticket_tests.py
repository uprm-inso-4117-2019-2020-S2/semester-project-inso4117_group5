import unittest
from domainHandlers.ticket import TicketHandler

class TicketCheck(unittest.TestCase):
#unit tests for validating Ticket operations

    def test_validTicket(self):
        self.assertTrue(TicketHandler().validateTicket(Ticket1))
        self.assertFalse(TicketHandler().validateTicket(Ticket2))
        self.assertTrue(TicketHandler().validateTicket(Ticket3))
        self.assertFalse(TicketHandler().validateTicket(Ticket4))
        self.assertFalse(TicketHandler().validateTicket(Ticket5))
        self.assertFalse(TicketHandler().validateTicket(Ticket6))
        self.assertFalse(TicketHandler().validateTicket(Ticket7))

if __name__ == "__main__":
    Ticket1 = [1, 1, 2,{"agua": 4, "pan": 2},'Caguas', 1]
    Ticket2 = [2, 2, 5,{"agua": 4, "MRE": 2},'Mayaguez', -1]
    Ticket3 = [1, 1, 2,"comida",'San Juan', 5]
    Ticket4 = [6, 341, 32,{"agua": 4, "pan": 2},123, 2]
    Ticket5 = [-1, 1, 2,{"agua": 4, "pan": 2},'Cidra', 1]
    Ticket6 = [1, 1, -2,{"agua": 4, "pan": 2},'Ponce', 1]
    Ticket7 = [1, -99, 2,{"agua": 4, "pan": 2},'Ponce', 1]

    unittest.main()
