from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# CKEdtor input flow for basic_page_body_xpath_imce_2. This need to be in seperate def and call accordingly.
def input(self):
    global final_ckeditor
    print "Final ckeditor in imce: ", final_ckeditor
    # Locate the iframes
    ckeditor_frame = self.driver.find_element_by_xpath(final_ckeditor)

    # Switch to frame
    self.driver.switch_to.frame(ckeditor_frame)

    # Send key to Ckeditor Body
    editor_body = self.driver.find_element_by_xpath("//body")
    editor_body.send_keys("Test Body")
    editor_body.send_keys(Keys.RETURN)

    # if driver is already inside ckeditor_frame, switch out first
    self.driver.switch_to.default_content()
    print "4. CKEditor check test PASS!"