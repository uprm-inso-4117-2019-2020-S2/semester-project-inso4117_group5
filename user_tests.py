import unittest
from domainHandlers.user import UserHandler
class UserCheck(unittest.TestCase):
#unit tests for validating user operations


    def test_validUser(self):
        self.assertTrue(UserHandler().validateUser(user1))
        self.assertFalse(UserHandler().validateUser(user2))
        self.assertTrue(UserHandler().validateUser(user3))
        self.assertFalse(UserHandler().validateUser(user4))
        self.assertFalse(UserHandler().validateUser(user5))
        self.assertFalse(UserHandler().validateUser(user6))
        self.assertFalse(UserHandler().validateUser(user7))

if __name__ == "__main__":
    user1 = [1,'Morsa','faces4444','morsa@gmail.com','7878598899','Carolina',.99]
    user2 = [2,'Javier','L','morsagmail.com','787888999','Uganda',.23]
    user3 = [3,'Morsa','TryHard22','morsaworker@gmail.com','939-787-7799','Ivory Coast',.75]
    user4 = [4,'Walrus','Paul','loquito99@gmail.com','787/123/4567','Maya',-.99]
    user5 = [5,'Morsa','','morsa@gmail.com','7844445599','Quebra',.99]
    user6 = [6,'','lol','morsa@gmail.com','7844445599','Quebra',.99]
    user7 = [7,'Juan','lol','morsa@gmail.com','7844445599','22',.99]

    unittest.main()
