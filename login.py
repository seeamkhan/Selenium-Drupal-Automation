from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from __builtin__ import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest
import os,Conf_Reader

class CreateContents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # cls.driver.maximize_window()
        cls.base_url = "http://localhost/drupal7/"

    #Get the test account credentials from the .credentials file
    credentials_file = os.path.join(os.path.dirname(__file__),'login.credentials')
    username = Conf_Reader.get_value(credentials_file,'LOGIN_USER')
    password = Conf_Reader.get_value(credentials_file,'LOGIN_PASSWORD')

    def test_go_to_login(self):
        self.driver.get(self.base_url + "user")

    #Decleared is_element_present method
    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :param how: By locator type
        :param what: locator value
        """
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    #Verify Login was successful.
    def test_verify_login_page(self):
        self.assertTrue(self.is_element_present(By.XPATH, "//input[contains(@id, 'edit-name')]"))
        self.assertTrue(self.is_element_present(By.XPATH, "//input[contains(@id, 'edit-pass')]"))
        self.assertTrue(self.is_element_present(By.XPATH, "//input[contains(@value, 'Log in')]"))
        # print "is_element_present is working"

    def test_login_as_user(self):
        user_field_xpath = "//input[contains(@id, 'edit-name')]"
        pass_field_xpath = "//input[contains(@id, 'edit-pass')]"
        login_button_xpath = "//input[contains(@value, 'Log in')]"

    #Login Process
        self.driver.find_element_by_xpath(user_field_xpath).clear()
        self.driver.find_element_by_xpath(user_field_xpath).send_keys(self.username)
        self.driver.find_element_by_xpath(pass_field_xpath).clear()
        self.driver.find_element_by_xpath(pass_field_xpath).send_keys(self.password)
        self.driver.find_element_by_xpath(login_button_xpath).click()
        print "user name entered successfully!!"











if __name__ == '__main__':
    unittest.main()