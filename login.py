import credentials as credentials
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest


class Credentials:
    def __init__(self):
        self.admin_email = "six.testemail@gmail.com"
        self.admin_pass = "@dmin@123"

class CreateContents(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "http://localhost/drupal7/"
        # self.driver.get('http://localhost/drupal7/user')
        self.credentials = Credentials()

    def test_login(self):
        driver = self.driver
        login_page = "user"
        driver.get(self.base_url + login_page)


        user_name_field = driver.find_element_by_id("edit-name")
        pass_field = driver.find_element_by_id("edit-pass")
        login_button = driver.find_element_by_id("edit-submit")

        # Login process:
        user_name_field.clear()
        user_name_field.send_keys(self.credentials.admin_email)
        pass_field.clear()
        pass_field.send_keys(self.credentials.admin_pass)
        login_button.click()
        self.driver.implicitly_wait(40)

    def test_verify_login(self):
        driver = self.driver
        logout_link = driver.find_element_by_link_text("Log out")



    # def tearDown(self):
    #     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
