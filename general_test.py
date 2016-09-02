#Druapl default features testing

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
    # def setUpC(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        # cls.base_url = "http://localhost/drupal7/user"
        cls.base_url = "http://seeam.com/drupal7/user"
        cls.driver.get(cls.base_url)

# Drupal common xpath:
        cls.content_menu_xpath = "//li[contains(@class, 'admin-menu-toolbar-category expandable')]/a[contains(@href, '/admin/content')]"
        cls.add_content_menu_xpath = "//li[contains(@class, 'admin-menu-toolbar-category expandable')]/ul[contains(@class, 'dropdown')]/li[contains(@class, 'expandable')]/a[contains(@href, '/node/add')]"
        cls.add_basic_page_xpath = "//ul[contains(@id, 'admin-menu-menu')]/li[2]/ul/li[1]/ul/li[2]/a"
        cls.user_field_xpath = "//input[contains(@id, 'edit-name')]"
        cls.pass_field_xpath = "//input[contains(@id, 'edit-pass')]"
        cls.login_button_xpath_bootstrap = "//button[contains(@value, 'Log in')]"
        cls.login_button_xpath_2 = "//input[contains(@value, 'Log in')]"
        cls.logout_link_xpath = "//a[contains(text(), 'Log out')]"
        cls.basic_page_title_xpath = "//h1[contains(text(), 'Create Basic page')]"
        cls.save_content_button_xpath = "//input[contains(@value, 'Save')]"
        cls.success_message_xpath = "//div[contains(@class, 'alert-success')]"

#Enable this to hard-code username and password. (Not recommended, for testing purpose only).
        # cls.username = ""
        # cls.password = ""

# Enable this to get username nad password from user input
#         cls.username = raw_input('Please type your Username or Email: ')
#         cls.password = raw_input('Please type your password: ')

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
        except NoSuchElementException, e:
            return False
        return True

# User Login method:
    def test_1_login_as_user(self):
        self.driver.find_element_by_xpath(self.user_field_xpath).clear()
        self.driver.find_element_by_xpath(self.user_field_xpath).send_keys(self.username)
        self.driver.find_element_by_xpath(self.pass_field_xpath).clear()
        self.driver.find_element_by_xpath(self.pass_field_xpath).send_keys(self.password)
        try:
            self.driver.find_element_by_xpath(self.login_button_xpath_bootstrap).click()
        except:
            self.driver.find_element_by_xpath(self.login_button_xpath_2).click()

        # Verify Logout link is present
        self.assertTrue(self.is_element_present(By.XPATH, self.logout_link_xpath))
        print "User Login test PASS!"


# Add new Contents method:
    def test_3_admin_hover_menu(self):
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
        basic_page_body_xpath = "//div[contains(@id, 'cke_2_contents')]/iframe"
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, basic_page_body_xpath)))
        finally:
            self.assertTrue(self.is_element_present(By.XPATH, basic_page_body_xpath))

        #Locate the iframes
        ckeditor_frame = self.driver.find_element_by_xpath(basic_page_body_xpath)

        #Switch to frame
        self.driver.switch_to.frame(ckeditor_frame)

        #Send key to Ckeditor Body
        editor_body = self.driver.find_element_by_xpath("//body")
        editor_body.send_keys("Test Body")

        # if driver is already inside ckeditor_frame, switch out first
        self.driver.switch_to.default_content()

# Ckeditor file upload method:
    def test_4_ckeditor_image_upload(self):
        # Image upload
        image_upload_button_xpath = "//label[contains(text(),'Body')]//following-sibling::div//a[contains(@class,'cke_button__image')]"
        browse_button_xpath = "//span[contains(@id, 'cke_142_label')]"
        self.driver.find_element_by_xpath(image_upload_button_xpath).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, browse_button_xpath)))
        finally:
            self.driver.find_element_by_xpath(browse_button_xpath).click()

        #window handle
        #print current window title
        print ("Switched to " + self.driver.title + "window")
        #Switch to image upload window
        self.driver.switch_to.window(self.driver.window_handles[1])
        print ("Switched to " + self.driver.title + "window")
        upload_button_xpath = "//span[contains(text(), 'Upload')]"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, upload_button_xpath)))
        self.driver.find_element_by_xpath(upload_button_xpath).click()
        upload_box_xpath = "//div[contains(@id, 'op-content-upload')]"
        choose_file_xpath = "//input[contains(@id, 'edit-imce')]"
        imce_upload_button_xpath = "//input[contains(@id, 'edit-upload')]"

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located( (By.XPATH, upload_box_xpath)) )
        except NoSuchElementException:
            return False
        finally:
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_files', 'business.pdf')
            # print file_path
            self.driver.find_element_by_xpath(choose_file_xpath).send_keys(file_path)
        self.driver.find_element_by_xpath(imce_upload_button_xpath).click()
        time.sleep(3)
        # self.driver.save_screenshot('file_upload_screenshot.png')

        row_count_int = len(self.driver.find_elements_by_xpath("//table[@id='file-list']/tbody/tr"))
        row_count = str(row_count_int)
        print row_count
        last_file_xpath = "//table[@id='file-list']/tbody/tr[" + row_count + "]/td/span"
        print last_file_xpath
        # self.driver.find_element_by_xpath(last_file_xpath).click()
        insert_file_xpath = "//span[contains(text(), 'Insert file')]"
        time.sleep(2)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located( (By.XPATH, insert_file_xpath)) )
        except NoSuchElementException:
            return False
        finally:
            self.driver.find_element_by_xpath(insert_file_xpath).click()

        self.driver.switch_to.window(self.driver.window_handles[0])
        print self.driver.title
        ckeditor_ok_button_xpath = "//span[contains(text(), 'OK')]"
        self.driver.find_element_by_xpath(ckeditor_ok_button_xpath).click()
        # print "CKEditor works!!"

        # Save the Basic Page
        self.driver.find_element_by_xpath(self.save_content_button_xpath).click()

        # Verify successful Basic Page creation
        test_page_title_xpath = "//h1[contains(text(), 'Test Basic Page')]"
        # self.assertTrue(self.is_element_present(By.XPATH, self.success_message_xpath))
        self.assertTrue(self.is_element_present(By.XPATH, test_page_title_xpath))
        print "Basic Page creation success!!"



# Run all the test cases
#     def test_login(self):
#         # self.verify_login_page()
#         self.login_as_user()
#         self.verify_login_success()
#         self.admin_hover_menu()
#         self.ckeditor_image_upload()


    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
