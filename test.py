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
import ckeditor_imce


class CreateContents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "https://stevieawards.dev.lin2.panth.com/user"
        # cls.base_url = "http://jaxara.dev.lin2.panth.com/user"
        # cls.base_url = "http://localhost/drupal7/user"
        # cls.base_url = "http://seeam.com/drupal7/user"
        # cls.base_url = "http://googel.com/"
        cls.driver.get(cls.base_url)
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
        cls.basic_page_body_xpath_imce = "//label[contains(text(), 'Body')]//following-sibling::div//iframe"
        cls.basic_page_body_xpath_ckfinder = "//td[contains(@id, 'cke_contents_edit-body-und-0-value')]/iframe"
        cls.final_ckeditor = ""
        cls.image_upload_button_imce_xpath = "//label[contains(text(),'Body')]//following-sibling::div//a[contains(@class,'cke_button__image')]"
        cls.image_upload_button_ckfinder_xpath = "//label[contains(text(),'Body')]//following-sibling::div//span[contains(text(), 'Image')]"
        cls.final_browse_button = ""
        cls.browse_button_imce_xpath = "//span[contains(@id, 'cke_142_label')]"
        cls.browse_button_ckfinder_xpath = "test"

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
        content_menu_hover = self.driver.find_element_by_xpath(self.content_menu_xpath)
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.content_menu_xpath)))
        except:
            print "Admin Menu not found."
        hover_content = ActionChains(self.driver).move_to_element(content_menu_hover)
        hover_content.perform()
        add_content_hover = self.driver.find_element_by_xpath(self.add_content_menu_xpath)
        hover_add_content = ActionChains(self.driver).move_to_element(add_content_hover)
        hover_add_content.perform()

        # Click on hover menu item (Content > Add content > Basic Page)
        # self.assertTrue(self.is_element_present(By.XPATH, self.add_basic_page_xpath))
        try:
            self.driver.find_element_by_xpath(self.add_basic_page_xpath).click()
        except:
            print "Basic page create page not found."

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


    def test_4_check_editor(self):
        global final_ckeditor
        ckeditor_type_list = [
            self.basic_page_body_xpath_imce,
            self.basic_page_body_xpath_ckfinder
        ]
        time.sleep(1)
        for i in xrange(len(ckeditor_type_list)):
            try:
                self.driver.find_element_by_xpath(ckeditor_type_list[i])
                final_ckeditor = ckeditor_type_list[i]
                break
            except:
                print ckeditor_type_list[i], " does not found"
        print "4. Final CKEditor is: ", final_ckeditor

    # CKEdtor input flow for basic_page_body_xpath_imce. This need to be in separate def and call accordingly.
    def test_5_imce_input(self):
        global final_ckeditor
        print "Final ckeditor in imce: ", final_ckeditor
        #Locate the iframes
        ckeditor_frame = self.driver.find_element_by_xpath(final_ckeditor)

        #Switch to frame
        self.driver.switch_to.frame(ckeditor_frame)

        #Send key to Ckeditor Body
        editor_body = self.driver.find_element_by_xpath("//body")
        editor_body.send_keys("Test Body")
        editor_body.send_keys(Keys.RETURN)

        # if driver is already inside ckeditor_frame, switch out first
        self.driver.switch_to.default_content()
        print "4. CKEditor check test PASS!"

    def imce_image_upload(self):
        pass

    def ckfinder_image_upload(self):
        pass

    def test_6_image_upload(self):
        global final_ckeditor
        if (final_ckeditor == self.basic_page_body_xpath_ckfinder):
            self.ckfinder_image_upload()
        else:
            self.imce_image_upload()

    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()














# l = 3
# for count in range(0,l):
# 	for i in range(count,l):
# 	  for j in range(count,i+1):
# 	    print [j],
# 	  print

# for test1 in xrange(3):
# 	# print "output test1"
# 	for test2 in xrange(test1+1):
# 		print "output test2"
# 		for test3 in xrange(test2+1):
# 			print "output test3"

# PHP code
# $str_arr = array('P', 'E', 'N', 'D');
# for($i = 0; $i < count($str_arr); $i++){
#  $index = array();
#  for($j = $i; $j < count($str_arr); $j++){
#   $index[] = $j;
#   $output = '';
#   for( $k = 0; $k < count($index); $k++ ){
#    $output .= $str_arr[$index[$k]];
#   }
#   echo $output."<br/>";
#  }
# }

# l = 3
# for count in range(0,l):
# 	for i in range(count,l):
# 		x = []
# 		for j in range(count,i+1):
# 			x.append(j)
# 		print x
