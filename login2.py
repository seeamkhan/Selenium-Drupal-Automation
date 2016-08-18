from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest


class CreateContents(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost/drupal7/user')

    def test_login(self):
        driver = self.driver


        user_name_field = driver.find_element_by_id("edit-name")
        admin_email = "six.testemail@gmail.com"
        pass_field = driver.find_element_by_id("edit-pass")
        admin_pass = "@dmin@123"
        login_button = driver.find_element_by_id("edit-submit")

        # Login process:

        # driver.get(self.base_url + login_page)
        user_name_field.clear()
        user_name_field.send_keys(admin_email)
        pass_field.clear()
        pass_field.send_keys(admin_pass)
        login_button.click()
        self.driver.implicitly_wait(40)









        #OLD FILE
        #       account_type        = "Member"
        # member_email        = "three.testemail@gmail.com"
        # member_pass         = "test"
        # email_field_id      = "edit-name"
        # pass_field_id       = "edit-pass"
        # login_button_xpath  = "//button[@value = 'Log in']"
        # logout_link_xpath   = "//a[contains(@href, '/user/logout')]"
        # judge_status        = "//section[@id='block-system-main']/div[2]/div/div[2]/div"
        #
        #
        # # account_type_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector("input[type='radio'][value='Member']")) /for using css instead of xpath/
        # account_type_element = WebDriverWait(driver, 10).until(
        #     lambda driver: driver.find_element_by_xpath("//input[@id='edit-member-type-judge']"))
        # email_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(email_field_id))
        # pass_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(pass_field_id))
        # login_button_element = WebDriverWait(driver, 10).until(
        #     lambda driver: driver.find_element_by_xpath(login_button_xpath))
        #
        # # account_type_element.clear()
        # account_type_element.click()
        # email_field_element.clear()
        # email_field_element.send_keys(member_email)
        # pass_field_element.clear()
        # pass_field_element.send_keys(member_pass)
        # login_button_element.click()
        # WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logout_link_xpath))
        # #WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(judge_status))
        # WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_class_name("judge-side-box"))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
