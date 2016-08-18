import credentials as credentials
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest


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
        # self.driver.implicitly_wait(40)

    def test_verify_login(self):
        driver = self.driver
        logout_link = driver.find_element_by_link_text("Log out")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by.link_text, "Log out")
        except NoSuchElementException as e: return False
        return True
        # self.assertTrue(self.is_element_present(By.LINK_TEXT, "My link"))



        # def tearDown(self):
        #     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
