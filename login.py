from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest, time, re
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import Conf_Reader


class CreateContents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()


        # cls.base_url = "https://stevieawards.dev.lin2.panth.com/user"
        cls.base_url = "http://jaxara.dev.lin2.panth.com/user"
        # cls.base_url = "http://localhost/drupal7/user"
        # cls.base_url = "http://google.com"
        # cls.base_url = "http://seeam.com/drupal7/user"

        cls.verificationErrors = []
        cls.driver.get(cls.base_url)  # Drupal common xpath:
        cls.content_menu_xpath = "//li[contains(@class, 'admin-menu-toolbar-category expandable')]/a[contains(@href, '/admin/content')]"
        cls.add_content_menu_xpath = "//li[contains(@class, 'admin-menu-toolbar-category expandable')]/ul[contains(@class, 'dropdown')]/li[contains(@class, 'expandable')]/a[contains(@href, '/node/add')]"
        cls.add_basic_page_xpath = "//ul[contains(@id, 'admin-menu-menu')]/li[2]/ul/li[1]/ul/li[2]/a"
        cls.user_field_xpath = "//input[contains(@id, 'edit-name')]"
        cls.pass_field_xpath = "//input[contains(@id, 'edit-pass')]"
        cls.login_button_xpath_bootstrap = "//button[contains(@value, 'Log in')]"
        cls.login_button_xpath_2 = "//input[contains(@value, 'Log in')]"
        cls.basic_page_title_xpath = "//h1[contains(text(), 'Create Basic page')]"
        cls.logout_link_xpath = "//a[contains(text(), 'Log out')]"
        cls.basic_page_body_xpath_imce_1 = "//div[contains(@id, 'cke_1_contents')]/iframe"
        cls.basic_page_body_xpath_imce_2 = "//div[contains(@id, 'cke_2_contents')]/iframe"
        cls.basic_page_body_xpath_ckfinder = "//td[contains(@id, 'cke_contents_edit-body-und-0-value')]/iframe"

# Enable this to get username and password from credential file
    credentials_file = os.path.join(os.path.dirname(__file__), 'login.credentials')
    username = Conf_Reader.get_value(credentials_file, 'LOGIN_USER')
    password = Conf_Reader.get_value(credentials_file, 'LOGIN_PASSWORD')
# Declared is_element_present method
    def is_element_present(self, how, what):
        """
    Utility method to check presence of an element on page
    :param how: By locator type
    :param what: locator value
    """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

# User Login method:
    def test_1_login_as_user(self):
        self.driver.find_element_by_xpath(self.user_field_xpath).clear()
        self.driver.find_element_by_xpath(self.user_field_xpath).send_keys(self.username)
        self.driver.find_element_by_xpath(self.pass_field_xpath).clear()
        self.driver.find_element_by_xpath(self.pass_field_xpath).send_keys(self.password)
        # login_button_found = False
        # logout_link_found = False
        login_error_msg_xpath = "//div[contains(@class, 'alert-danger')]"
        login_button_link_list = [
            self.login_button_xpath_bootstrap,
            self.login_button_xpath_2
        ]
        for i in xrange(len(login_button_link_list)):
            try:
                self.driver.find_element_by_xpath(login_button_link_list[i]).click()
                print login_button_link_list[i], " login button found"
                break
            except:
                # pass
                print login_button_link_list[i], "login button not found"

        # Verify Logout link is present
        try:
            self.assertTrue(self.is_element_present(By.XPATH, login_error_msg_xpath))
            print "Login Failed! Please check Username/email and Password"
        except :
            pass
        self.assertTrue(self.is_element_present(By.XPATH, self.logout_link_xpath))
        print "1. User Login test PASS!"
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

