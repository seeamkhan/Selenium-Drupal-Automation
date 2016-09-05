from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod
from selenium.webdriver.common.keys import Keys
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
        cls.base_url = "https://stg.stevieawards.com/"
        # cls.base_url = "http://jaxara.dev.lin2.panth.com/"
        # cls.base_url = "http://localhost/drupal7/"
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
        cls.basic_page_title_xpath = "//h1[contains(text(), 'Create Basic page')]"
        cls.logout_link_xpath = "//a[contains(text(), 'Log out')]"
        cls.basic_page_body_xpath = "//label[contains(text(), 'Body')]//following-sibling::div//iframe"
        cls.ckfinder = 0
        cls.ckeditor_image_upload_button_xpath_1 = "//label[contains(text(),'Body')]//following-sibling::div//a[contains(@class,'cke_button_image')]/span[contains(@class,'cke_icon')]"
        cls.ckeditor_image_upload_button_xpath_2 = "//label[contains(text(),'Body')]//following-sibling::div//a[contains(@class,'cke_button__image')]" #this works for Stevie and local site.
        # cls.ckeditor_image_upload_button_xpath = "//label[contains(text(),'Body')]//following-sibling::div//span[contains(text(), 'Image')]"
        # cls. ckeditor_image_upload_button_xpath = "//label[contains(text(),'Body')]//following-sibling::div//span[contains(@class, 'cke_button__image_icon')]"
        cls.ckeditor_image_upload_button_xpath = ""
        cls.ckeditor_image_upload_button_list = []
        cls.final_browse_button = ""
        cls.browse_buttons_list = []
        cls.browse_button_local_xpath = "//span[contains(@id, 'cke_142_label')]"
        cls.browse_button_stevie_xpath = "//span[contains(@id, 'cke_108_label')]"
        cls.browse_button_sie_xpath = "//span[contains(@id, 'cke_171_label')]"
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
        login_error_msg_xpath = "//div[contains(@class, 'alert-danger')]"
        login_button_link_list = [
            self.login_button_xpath_bootstrap,
            self.login_button_xpath_2
        ]
        for i in xrange(len(login_button_link_list)):
            try:
                self.driver.find_element_by_xpath(login_button_link_list[i]).click()
                print "Some login button found"
                break
            except:
                # pass
                print "No login button found"
        # Verify Logout link is present
        try:
            self.assertTrue(self.is_element_present(By.XPATH, login_error_msg_xpath))
            print "Login Failed! Please check Username/email and Password"
        except:
            pass
        # assert and halt the test if login is not successful.
        self.assertTrue(self.is_element_present(By.XPATH, self.logout_link_xpath))
        print "1. User Login test PASS!"
        # time.sleep(2)

    def test_2_nav_to_basic_create_basic_page(self):
        self.driver.get(self.base_url + "node/add/page")
        # content_menu_hover = self.driver.find_element_by_xpath(self.content_menu_xpath)
        # try:
        #     WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.content_menu_xpath)))
        # except:
        #     print "Admin Menu not found."
        # hover_content = ActionChains(self.driver).move_to_element(content_menu_hover)
        # hover_content.perform()
        # add_content_hover = self.driver.find_element_by_xpath(self.add_content_menu_xpath)
        # hover_add_content = ActionChains(self.driver).move_to_element(add_content_hover)
        # hover_add_content.perform()
        #
        # # Click on hover menu item (Content > Add content > Basic Page)
        # # self.assertTrue(self.is_element_present(By.XPATH, self.add_basic_page_xpath))
        # try:
        #     self.driver.find_element_by_xpath(self.add_basic_page_xpath).click()
        # except:
        #     print "Basic page create page not found."

        # verify create basic page
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.basic_page_title_xpath)))
        except:
            print "Basic Page creating page loading failed."
        self.assertTrue(self.is_element_present(By.XPATH, self.basic_page_title_xpath))
        print "2. Navigate to Create Basic page test PASS!"

    def test_3_basic_page_title(self):
        # Enter data in the Basic Page fields
        basic_page_title_field_xpath = "//input[contains(@id, 'edit-title')]"
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, basic_page_title_field_xpath)))
        self.driver.find_element_by_xpath(basic_page_title_field_xpath).clear()
        self.driver.find_element_by_xpath(basic_page_title_field_xpath).send_keys("Test Basic Page")
        print "3. Basic page title enter PASS!"

    def test_4_find_ckfinder_in_page_source(self):
        global ckfinder
        html_source = self.driver.page_source
        if "ckfinder" in html_source:
            ckfinder = 1
            print "4. ckfinder found."
        else:
            ckfinder = 0
        print "4. IMCE file uploader check PASS!"

    def test_5_ckeditor_body_input(self):
        #Locate the iframes
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.basic_page_body_xpath)))
        ckeditor_frame = self.driver.find_element_by_xpath(self.basic_page_body_xpath)
        #Switch to frame
        self.driver.switch_to.frame(ckeditor_frame)
        #Send key to Ckeditor Body
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body")))
        editor_body = self.driver.find_element_by_xpath("//body")
        editor_body.send_keys("Test Body")
        editor_body.send_keys(Keys.RETURN)
        # if driver is already inside ckeditor_frame, switch out first
        self.driver.switch_to.default_content()
        print "5. CKEditor Body input test PASS!"

    def test_6_ckeditor_image_upload(self):
        global ckfinder
        global final_browse_button
        global browse_button_list
        global ckeditor_image_upload_button_list
        global ckeditor_image_upload_button_xpath

        browse_button_list = [self.browse_button_local_xpath, self.browse_button_stevie_xpath, self.browse_button_sie_xpath]
        ckeditor_image_upload_button_list = [self.ckeditor_image_upload_button_xpath_1, self.ckeditor_image_upload_button_xpath_2]
        if ckfinder is 0:
            for j in xrange(len(ckeditor_image_upload_button_list)):
                try:
                    WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, ckeditor_image_upload_button_list[j])))
                    ckeditor_image_upload_button_xpath = ckeditor_image_upload_button_list[j]
                    break
                except:
                    print "Unknown CKEditor Image Uplaod button."
            print ckeditor_image_upload_button_xpath
            # click on the ckeditor image upload button.
            self.driver.find_element_by_xpath(ckeditor_image_upload_button_xpath).click()

            # wait for the image properties pop-up to appear, then click on the Browse Server button.
            time.sleep(1)
            for i in xrange(len(browse_button_list)):
                try:
                    # WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, browse_button_list[i])))
                    WebDriverWait(self.driver, 3).until(
                        EC.element_to_be_clickable((By.XPATH, browse_button_list[i])))
                    final_browse_button = browse_button_list[i]
                    break
                except:
                    print "Unknown Browse Server button."
            print final_browse_button
            # except:
            #     WebDriverWait(self.driver, 3).until(
            #         EC.presence_of_element_located((By.XPATH, self.browse_button_stevie_xpath)))
            #     final_browse_button = self.browse_button_stevie_xpath
            self.driver.find_element_by_xpath(final_browse_button).click()

            # Switch to image upload window
            self.driver.switch_to.window(self.driver.window_handles[1])
            # print ("Switched to " + self.driver.title + "window")

            # From the image upload window, click on the 'Upload' button.
            upload_button_xpath = "//span[contains(text(), 'Upload')]"
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, upload_button_xpath)))
            self.driver.find_element_by_xpath(upload_button_xpath).click()

            # define various upload window elements with variables.
            upload_box_xpath = "//div[contains(@id, 'op-content-upload')]"
            choose_file_xpath = "//input[contains(@id, 'edit-imce')]"
            imce_upload_button_xpath = "//input[contains(@id, 'edit-upload')]"

            # Select file for uploading.
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, upload_box_xpath)))
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_files', 'test.png')
            self.driver.find_element_by_xpath(choose_file_xpath).send_keys(file_path)

            #click 'Upload' button.
            self.driver.find_element_by_xpath(imce_upload_button_xpath).click()

            # wait for the file to upload
            time.sleep(3)

            # Find last uploaded file.
            row_count_int = len(self.driver.find_elements_by_xpath("//table[@id='file-list']/tbody/tr"))
            row_count = str(row_count_int)
            # print row_count
            # last_file_xpath = "//table[@id='file-list']/tbody/tr[" + row_count + "]/td/span"
            # print last_file_xpath

            # Insert last uploaded file into the 'Image Property' pop-up.
            # self.driver.find_element_by_xpath(last_file_xpath).click()
            insert_file_xpath = "//span[contains(text(), 'Insert file')]"
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, insert_file_xpath)))
            self.driver.find_element_by_xpath(insert_file_xpath).click()

            # Switch from the file uploader window to Main window.
            self.driver.switch_to.window(self.driver.window_handles[0])
            # print self.driver.title

            # Click 'OK' button on 'Image Property' pop-up to put the uploaded file into CKEditor body.
            ckeditor_ok_button_xpath = "//span[contains(text(), 'OK')]"
            self.driver.find_element_by_xpath(ckeditor_ok_button_xpath).click()
            print "6. CKEditor File upload PASS!"
            # time.sleep(3)

    def test_7_save_basic_page(self):
        # Click 'Save' to save the Basic Page
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.save_content_button_xpath)))
        self.driver.find_element_by_xpath(self.save_content_button_xpath).click()

        # Verify successful Basic Page creation
        test_page_title_xpath = "//em[contains(text(), 'Test Basic Page')]"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, test_page_title_xpath)))
        # self.assertTrue(self.is_element_present(By.XPATH, self.success_message_xpath))
        self.assertTrue(self.is_element_present(By.XPATH, test_page_title_xpath))
        print "7. Basic page saved PASS!"
        time.sleep(1)



    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()