import HtmlTestRunner
from selenium import webdriver
import unittest

# Author: Edgardo Figueroa Cruz
# This selenium test suit only supports Chrome version 81
#   if you wanted to change this to your respective version
#   download respected chrome driver and locate it in the drivers file
# requirements are the following:
#   python
#   pip
#   selenium
#   unittest
#   htmlTestRunner
class ChromeSelection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driverC = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driverC.implicitly_wait(10)
        cls.driverC.minimize_window()
        cls.driverC.implicitly_wait(2)
        cls.driverC.maximize_window()

    def test_SelectionScreenRequester(self):
        self.driverC.get('http://127.0.0.1:5000/')
        self.assertTrue(self.driverC.find_element_by_class_name('role-selection').is_displayed())
        # self.assertEqual('Select the role you want to log in as', self.driverC.find_element_by_name('role-selection').text)
        self.assertTrue(self.driverC.find_element_by_name('requesterBtn').is_displayed())
        self.assertEqual('REQUESTER', self.driverC.find_element_by_name('requesterBtn').text)
        self.driverC.find_element_by_name('requesterBtn').click()
        self.driverC.implicitly_wait(10)
        self.assertTrue(self.driverC.find_element_by_id('posts-tab').is_displayed())
        self.assertEqual('Offer some help', self.driverC.find_element_by_id('posts-tab').text)
        self.assertFalse(self.driverC.find_element_by_id('posts-tab').is_selected())

    def test_SelectionScreenPrvider(self):
        self.driverC.get('http://127.0.0.1:5000/')
        self.assertTrue(self.driverC.find_element_by_name('providerBtn').is_displayed())
        #self.assertEqual('Select the role you want to log in as', self.driverC.find_element_by_name('role-selection').text)
        self.assertEqual('PROVIDER', self.driverC.find_element_by_name('providerBtn').text)
        self.assertTrue(self.driverC.find_element_by_name('providerBtn').is_displayed())
        self.driverC.find_element_by_name('providerBtn').click()
        self.driverC.implicitly_wait(10)
        self.assertTrue(self.driverC.find_element_by_id('posts-tab').is_displayed())
        self.assertEqual('Request some help', self.driverC.find_element_by_id('posts-tab').text)
        self.assertFalse(self.driverC.find_element_by_id('posts-tab').is_selected())



    @classmethod
    def tearDownClass(cls) :
        cls.driverC.close()
        cls.driverC.quit()
        print('test completed')

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(output='../Selenium Test/Reports'))
