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
		# cls.base_url = "https://stevieawards.dev.lin2.panth.com/"
		# cls.base_url = "http://jaxara.dev.lin2.panth.com/"
		cls.base_url = "http://localhost/drupal7/"
		cls.driver.get(cls.base_url + "user")  # Drupal common xpath:
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
		except NoSuchElementException, e:
			return False
		return True

# User Login method:
	def test_1_login_as_user(self):
		self.driver.find_element_by_xpath(self.user_field_xpath).clear()
		self.driver.find_element_by_xpath(self.user_field_xpath).send_keys(self.username)
		self.driver.find_element_by_xpath(self.pass_field_xpath).clear()
		self.driver.find_element_by_xpath(self.pass_field_xpath).send_keys(self.password)
		login_button_found = False
		logout_link_found = False
		login_error_msg_xpath = "//div[contains(@class, 'alert-danger')]"
		try:
			if(login_button_found == False):
				self.driver.find_element_by_xpath(self.login_button_xpath_bootstrap).click()
				login_button_found = True
				print "Bootstrap theme login button found."
			if(login_button_found == False):
				self.driver.find_element_by_xpath(self.login_button_xpath_2)
		except:
			print "Login Button not found"

		# Verify Logout link is present
		try:
			if(logout_link_found == False):
				self.assertTrue(self.is_element_present(By.XPATH, self.logout_link_xpath))
				print "1. User Login test PASS!"
				logout_link_found = True
			if(login_button_found == False):
				self.assertTrue(self.is_element_present(By.XPATH, login_error_msg_xpath))
		except:
			print "Login Failed!"





	def test_2_nav_to_basic_create_basic_page(self):
		content_menu_hover = self.driver.find_element_by_xpath(self.content_menu_xpath)
		hover_content = ActionChains(self.driver).move_to_element(content_menu_hover)
		hover_content.perform()
		add_content_hover = self.driver.find_element_by_xpath(self.add_content_menu_xpath)
		hover_add_content = ActionChains(self.driver).move_to_element(add_content_hover)
		hover_add_content.perform()

		# Click on hover menu item (Content > Add content > Basic Page)
		self.assertTrue(self.is_element_present(By.XPATH, self.add_basic_page_xpath))
		self.driver.find_element_by_xpath(self.add_basic_page_xpath).click()

		# verifiy create basic page
		self.assertTrue(self.is_element_present(By.XPATH, self.basic_page_title_xpath))

		# Enter data in the Basic Page fields
		basic_page_title_field_xpath = "//input[contains(@id, 'edit-title')]"
		self.driver.find_element_by_xpath(basic_page_title_field_xpath).clear()
		self.driver.find_element_by_xpath(basic_page_title_field_xpath).send_keys("Test Basic Page")
		print "2. Navigate to Create Basic page test PASS!"

	def test_3_ckeditor_input(self):

		editor_found = False

		try:
			WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self.basic_page_body_xpath_imce_1)))
			print "IMCE found."
			editor_found = True
		except:
			print "IMCE not found"
		if (editor_found == False):
			try:
				self.driver.find_element_by_xpath(self.basic_page_body_xpath_ckfinder)
				print "CKFinder found"
				editor_found = True
			except:
				print "CKFinder not found"
		if (editor_found == False):
			try:
				self.driver.find_element_by_xpath(self.basic_page_body_xpath_imce_2)
			except:
				print "CKFinder not found"
		if ( editor_found == False ):
			print 'No editor found yet!'




		# time.sleep(5)
		# print "3. CKEditor input test PASS!"



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
