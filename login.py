from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from __builtin__ import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest

#User credentials class, this should be kept in another file with encryption.
class Credentials:
    def __init__(self):
        self.admin_email = "six.testemail@gmail.com"
        self.admin_pass = "@dmin@123"



class CreateContents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "http://localhost/drupal7/"
        # self.driver.get('http://localhost/drupal7/user')
        cls.credentials = Credentials()

    def test_go_to_login(self):
        driver = self.driver
        login_page = "user"
        driver.get(self.base_url + login_page)
        
    def test_login_field(self):

        #check login elements exist in the Login page
        self.assertTrue(self.is_element_present(By.ID,"edit-name"))
        #print "is_element_present is working!! :D"

    def test_login(self):
        driver = self.driver
        user_name_field = driver.find_element_by_id("edit-name")
        pass_field = driver.find_element_by_id("edit-pass")
        login_button = driver.find_element_by_id("edit-submit")

        # Login process:
        user_name_field.clear()
        user_name_field.send_keys(self.credentials.admin_email)
        pass_field.clear()
        pass_field.send_keys(self.credentials.admin_pass)
        login_button.click()
        # self.driver.implicitly_wait(40)

    def test_verify_login(self):
        driver = self.driver
        try:
            logout_link = driver.find_element_by_xpath(".//*[@id='admin-menu-account']/li[1]/a")
            print logout_link
        except NoSuchElementException:
            print "exception"




        # def tearDown(self):
        #     self.driver.quit()

    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :param self:
        :param how: By locator type
        :param what: locator value
        :return:
        """
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

if __name__ == '__main__':
    unittest.main()