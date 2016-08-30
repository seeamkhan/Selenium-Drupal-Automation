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


class CreateContents(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.maximize_window()
		cls.base_url = "https://stevieawards.dev.lin2.panth.com/"
		cls.driver.get(cls.base_url + "user")  # Drupal common xpath:
		cls.content_menu_xpath = "//li[contains(@class, 'admin-menu-toolbar-category expandable')]/a[contains(@href, '/admin/content')]"
		cls.add_content_menu_xpath = "//li[contains(@class, 'admin-menu-toolbar-category expandable')]/ul[contains(@class, 'dropdown')]/li[contains(@class, 'expandable')]/a[contains(@href, '/node/add')]"
		cls.add_basic_page_xpath = "//ul[contains(@id, 'admin-menu-menu')]/li[2]/ul/li[1]/ul/li[2]/a"
		cls.user_field_xpath = "//input[contains(@id, 'edit-name')]"
		cls.pass_field_xpath = "//input[contains(@id, 'edit-pass')]"
		# cls.login_button_xpath_array = ["//button[contains(@value, 'Log in')]", "//input[contains(@value, 'Log in')]"]
		cls.login_button_xpath_bootstrap = "//button[contains(@value, 'Log in')]"
		cls.login_button_xpath_2 = "//input[contains(@value, 'Log in')]"
		cls.logout_link_xpath = "//a[contains(text(), 'Log out')]"  # Enable this to hard-code username and password. (Not recommended, for testing purpose only).
		cls.username = "panth.admin"
		cls.password = "@tester26#"

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
	def login_as_user(self):
		# login_button = []
		self.driver.find_element_by_xpath(self.user_field_xpath).clear()
		self.driver.find_element_by_xpath(self.user_field_xpath).send_keys(self.username)
		self.driver.find_element_by_xpath(self.pass_field_xpath).clear()
		self.driver.find_element_by_xpath(self.pass_field_xpath).send_keys(self.password)
		try:
			self.driver.find_element_by_xpath(self.login_button_xpath_bootstrap).click()
		except:
			self.driver.find_element_by_xpath(self.login_button_xpath_2).click()
		finally:
			return True

		# self.driver.find_element_by_xpath(self.login_button_xpath_bootstrap).click()

	# print "user name entered successfully!!"

	def verify_login_success(self):
		self.assertTrue(self.is_element_present(By.XPATH, self.logout_link_xpath))
	# print "Login successful verified"



	# Run all the test cases
	def test_login(self):
		# self.verify_login_page()
		self.login_as_user()
		# self.verify_login_success()
		# self.admin_hover_menu()
		# self.ckeditor_image_upload()

	# @classmethod
	# def tearDown(cls):
	# 	# Close the browser window
	# 	cls.driver.quit()


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
