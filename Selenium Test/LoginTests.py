import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class ChromeSelection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driverC = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driverC.implicitly_wait(10)
        cls.driverC.minimize_window()
        cls.driverC.implicitly_wait(2)
        cls.driverC.maximize_window()

    def test_LoginSuccess(self):
        user_name = "username"
        password = "password"
        self.driverC.get('http://127.0.0.1:5000/')
        self.assertTrue(self.driverC.find_element_by_id('text').is_displayed())
        self.assertTrue(self.driverC.find_element_by_id('password').is_displayed())
        self.driverC.find_element_by_id('text').send_keys(user_name)
        self.driverC.find_element_by_id('password').send_keys(password)
        self.driverC.find_element_by_id('btn').click()
        self.assertTrue(self.driverC.find_element_by_id('posts-tab').is_displayed())
    
    def test_LoginFail(self):
        user_name = "Guanda"
        password = "yhlqmdlg"
        self.driverC.get('http://127.0.0.1:5000/')
        self.assertTrue(self.driverC.find_element_by_id('text').is_displayed())
        self.assertTrue(self.driverC.find_element_by_id('password').is_displayed())
        self.driverC.find_element_by_id('text').send_keys(user_name)
        self.driverC.find_element_by_id('password').send_keys(password)
        self.driverC.find_element_by_id('btn').click()
        self.assertFalse(self.driverC.find_element_by_id('posts-tab').is_displayed())

    @classmethod
    def tearDownClass(cls) :
        cls.driverC.close()
        cls.driverC.quit()
        print('login test completed')

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(output='../Selenium Test/Reports'))
