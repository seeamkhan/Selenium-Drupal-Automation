#Druapl default features testing

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest, time, re
import os, Conf_Reader
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC




class CreateContents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "http://localhost/drupal7/"
        cls.driver.get(cls.base_url + "user")











    @classmethod
    def tearDown(cls):
        # Close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
