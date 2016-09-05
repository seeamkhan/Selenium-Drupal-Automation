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
        # cls.base_url = raw_input("Type the site URL: ")
        # cls.base_url = "https://stg.stevieawards.com/"
        # cls.base_url = "http://jaxara.dev.lin2.panth.com/"
        cls.base_url = "http://localhost/drupal7/"
        # cls.base_url = "http://seeam.com/drupal7/"
        # cls.base_url = "http://stg.sie.qioprogram.panth.com/"
        # cls.base_url = "http://googel.com/"
        cls.driver.get(cls.base_url + "user")
        # Drupal common xpath:
        cls.content_menu_xpath = "//li[contains(@class, 'admin-menu-toolbar-category expandable')]/a[contains(@href, '/admin/content')]"
        cls.add_content_menu_xpath = "//li[contains(@class, 'admin-menu-toolbar-category expandable')]/ul[contains(@class, 'dropdown')]/li[contains(@class, 'expandable')]/a[contains(@href, '/node/add')]"
        cls.add_basic_page_xpath = "//ul[contains(@id, 'admin-menu-menu')]/li[2]/ul/li[1]/ul/li[2]/a"
        cls.user_field_xpath = "//input[contains(@id, 'edit-name')]"
        cls.pass_field_xpath = "//input[contains(@id, 'edit-pass')]"
        cls.login_button_xpath_bootstrap = "//button[contains(@value, 'Log in')]"
        cls.login_button_xpath_2 = "//input[contains(@value, 'Log in')]"
        cls.basic_page_title_xpath = "//h1[contains(text(), 'Create*')]"
        cls.logout_link_xpath = "//a[contains(text(), 'Log out')]"
        cls.basic_page_body_xpath = "//label[contains(text(), 'Body')]//following-sibling::div//iframe"
        cls.ckfinder = 0
        cls.ckeditor_image_upload_button_xpath_1 = "//label[contains(text(),'Body')]//following-sibling::div//a[contains(@class,'cke_button_image')]/span[contains(@class,'cke_icon')]"
        cls.ckeditor_image_upload_button_xpath_2 = "//label[contains(text(),'Body')]//following-sibling::div//a[contains(@class,'cke_button__image')]"  # this works for Stevie and local site.
        # cls.ckeditor_image_upload_button_xpath = "//label[contains(text(),'Body')]//following-sibling::div//span[contains(text(), 'Image')]"
        # cls. ckeditor_image_upload_button_xpath = "//label[contains(text(),'Body')]//following-sibling::div//span[contains(@class, 'cke_button__image_icon')]"
        cls.ckeditor_image_upload_button_xpath = ""
        cls.ckeditor_image_upload_button_list = []
        cls.final_browse_button = ""
        cls.browse_buttons_list = []
        # Add the browse button xpath for the target site.
        cls.browse_button_local_xpath = "//span[contains(@id, 'cke_142_label')]"
        cls.browse_button_stevie_xpath = "//span[contains(@id, 'cke_108_label')]"
        cls.browse_button_sie_xpath = "//span[contains(@id, 'cke_171_label')]"
        cls.browse_button_cbb_xpath = "//span[contains(@id, 'cke_144_label')]"
        cls.save_content_button_xpath = "//input[contains(@value, 'Save')]"

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
        self.driver.get(self.base_url + "node/add/page")

    def test_2_image_upload(self):
        global ckfinder
        # global final_browse_button
        # global browse_button_list
        global ckeditor_image_upload_button_list
        global ckeditor_image_upload_button_xpath

        ckeditor_image_upload_button_list = [self.ckeditor_image_upload_button_xpath_1,
                                             self.ckeditor_image_upload_button_xpath_2]
        if self.ckfinder is 0:
            for j in xrange(len(ckeditor_image_upload_button_list)):
                try:
                    WebDriverWait(self.driver, 3).until(
                        EC.element_to_be_clickable((By.XPATH, ckeditor_image_upload_button_list[j])))
                    ckeditor_image_upload_button_xpath = ckeditor_image_upload_button_list[j]
                    break
                except:
                    print "Unknown CKEditor Image Uplaod button."
            print ckeditor_image_upload_button_xpath
            # click on the ckeditor image upload button.
            self.driver.find_element_by_xpath(ckeditor_image_upload_button_xpath).click()
            # wait for the image properties pop-up to appear, then click on the Browse Server button.
            time.sleep(1)

            for k in xrange(6):
                try:
                    self.driver.find_element_by_xpath("//span[contains(text(), 'Browse Server')]").click()
                    break
                except:
                    print "Unknown Browse Server button."
            # print test_browse_button



    # @classmethod
    # def tearDownClass(cls):
    #     # Close the browser window
    #     cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

