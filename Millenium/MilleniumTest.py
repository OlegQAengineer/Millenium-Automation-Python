import unittest

import HomePage as HP
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import MilleniumTest
from faker import Faker
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

faker_class = Faker()


class TestMilleniumHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(HP.urlMillenium)

    def test_burger_Menu_Functional(self):
        HP.clickHumburgerMenu()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(HP.navigation_menu))
        navmenu = HP.navigation_menu.is_displayed()
        unittest.TestCase.assertTrue(navmenu)

    def tearDown(self):
        self.driver.quit()





