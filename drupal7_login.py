#Druapl default features testing

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest, time, re
import os, Conf_Reader
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC




class CreateContents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "http://localhost/drupal7/"
        cls.driver.get(cls.base_url + "user")

    # Drupal common xpath:
        cls.content_menu_xpath = "//li[contains(@class, 'admin-menu-toolbar-category expandable')]/a[contains(@href, '/admin/content')]"
        cls.add_content_menu_xpath = "//li[contains(@class, 'admin-menu-toolbar-category expandable')]/ul[contains(@class, 'dropdown')]/li[contains(@class, 'expandable')]/a[contains(@href, '/node/add')]"
        cls.add_basic_page_xpath = "//ul[contains(@id, 'admin-menu-menu')]/li[2]/ul/li[1]/ul/li[2]/a"
        cls.user_field_xpath = "//input[contains(@id, 'edit-name')]"
        cls.pass_field_xpath = "//input[contains(@id, 'edit-pass')]"
        cls.login_button_xpath = "//input[contains(@value, 'Log in')]"
        cls.logout_link_xpath = "//a[contains(text(), 'Log out')]"
        cls.basic_page_title_xpath = "//h1[contains(text(), 'Create Basic page')]"
        cls.save_content_button_xpath = "//input[contains(@value, 'Save')]"
        cls.success_message_xpath = "//div[contains(@class, 'alert-success')]"

    # Get the test account credentials from the .credentials file
    credentials_file = os.path.join(os.path.dirname(__file__), 'login.credentials')
    username = Conf_Reader.get_value(credentials_file, 'LOGIN_USER')
    password = Conf_Reader.get_value(credentials_file, 'LOGIN_PASSWORD')

    # Decleared is_element_present method
    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :param how: By locator type
        :param what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def login_as_user(self):

        # Login Process
        self.driver.find_element_by_xpath(self.user_field_xpath).clear()
        self.driver.find_element_by_xpath(self.user_field_xpath).send_keys(self.username)
        self.driver.find_element_by_xpath(self.pass_field_xpath).clear()
        self.driver.find_element_by_xpath(self.pass_field_xpath).send_keys(self.password)
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
        # print "user name entered successfully!!"

    def verify_login_success(self):
        self.assertTrue(self.is_element_present(By.XPATH, self.logout_link_xpath))
        # print "Login successful verified"


    # Add new Contents
    def admin_hover_menu(self):

        content_menu_hover = self.driver.find_element_by_xpath(self.content_menu_xpath)
        hover_content = ActionChains(self.driver).move_to_element(content_menu_hover)
        hover_content.perform()
        add_content_hover = self.driver.find_element_by_xpath(self.add_content_menu_xpath)
        hover_add_content = ActionChains(self.driver).move_to_element(add_content_hover)
        hover_add_content.perform()

        #Click on hover menu item (Content > Add content > Basic Page)
        self.assertTrue(self.is_element_present(By.XPATH, self.add_basic_page_xpath))
        self.driver.find_element_by_xpath(self.add_basic_page_xpath).click()

        #verifiy create basic page
        self.assertTrue(self.is_element_present(By.XPATH, self.basic_page_title_xpath))

        #Enter data in the Basic Page fields
        basic_page_title_field_xpath = "//input[contains(@id, 'edit-title')]"


        self.driver.find_element_by_xpath(basic_page_title_field_xpath).clear()
        self.driver.find_element_by_xpath(basic_page_title_field_xpath).send_keys("Test Basic Page")


        #Wait for the CKEditor iframe to load and switch to iframe
        time.sleep(3)
        basic_page_body_xpath = "//div[contains(@id, 'cke_2_contents')]/iframe"
        self.assertTrue(self.is_element_present(By.XPATH, basic_page_body_xpath))
        # self.driver.switch_to_frame(self.driver.find_element_by_tag_name("iframe"))
        #Locate the iframes
        ckeditor_frame = self.driver.find_element_by_xpath(basic_page_body_xpath)

        #Switch to frame
        self.driver.switch_to.frame(ckeditor_frame)

        #Send key to Ckeditor Body
        editor_body = self.driver.find_element_by_xpath("//body")
        editor_body.send_keys("Test Body")

        # if driver is already inside ckeditor_frame, switch out first
        self.driver.switch_to.default_content()
        main_site_content_xpath = "//a[contains(@class, 'link-edit-summary')]"
        self.assertTrue(self.is_element_present(By.XPATH, main_site_content_xpath))
        self.driver.find_element_by_xpath(main_site_content_xpath).click()
        # print "CKEditor works!!"

        # Save the Basic Page
        self.driver.find_element_by_xpath(self.save_content_button_xpath).click()

        # Verify successful Basic Page creation
        test_page_title_xpath = "//h1[contains(text(), 'Test Basic Page')]"
        # self.assertTrue(self.is_element_present(By.XPATH, self.success_message_xpath))
        self.assertTrue(self.is_element_present(By.XPATH, test_page_title_xpath))
        print "Basic Page creation success!!"







    # Run all the test cases
    def test_login(self):
        # self.verify_login_page()
        self.login_as_user()
        self.verify_login_success()
        self.admin_hover_menu()


    # @classmethod
    # def tearDown(cls):
    #     # Close the browser window
    #     cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
