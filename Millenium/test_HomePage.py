import time
import unittest

from selenium.webdriver.common.by import By


from selenium.webdriver.support import expected_conditions as EC
from page_objects.home_page import HomePage as HP
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

faker_class = Faker()


class ChromeSearch(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        time.sleep(5)

    def test_burgermenu(self):
        driver = self.driver
        driver.get("https://www.mlp.com/")
        wait = WebDriverWait(driver, 3)

        action = webdriver.ActionChains(driver)
        HP.pushHumburger(self)

        #action.move_to_element(driver.find_element(By.XPATH, HP.hamburgerMenu)).click().perform()
        wait.until(EC.visibility_of_element_located((By.ID, HP.navMenu)))
        print("Nav menu open")
        driver.get_screenshot_as_file('NavMenuOpen.png')

        self.assertTrue(self, driver.find_element(By.ID, HP.navMenu))

    def tearDown(self):
        self.driver.quit()



