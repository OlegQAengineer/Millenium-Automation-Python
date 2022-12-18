import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Millenium.page_objects import page_objectHomeP as HP


class ChromeSearchHP(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(HP.url)
        time.sleep(3)

    # Check that a humburger menu is functional and navigation menu appear on the Home page
    def test_burgermenu(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(HP.cookies))
        HP.closeCookies(self)
        HP.clickElement(self, HP.hamburgerMenuXP)
        self.assertTrue(EC.visibility_of_element_located(HP.navMenuID))
        HP.delay()
        driver.get_screenshot_as_file('C:/Users/varts/PycharmProjects/Millenium-Automation-Python/Millenium/Screen_Shots/NavMenuOpen.png')

    # Check that logo 'm' is functional and leave us on the Home page
    def test_mLogo(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(HP.cookies))
        HP.closeCookies(self)
        HP.clickElement(self, HP.mLogoXP)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(HP.mLogo))
        actualTitle = driver.title

        self.assertTrue(actualTitle == HP.titleText)
        time.sleep(1)

    # Check that "Investor Login" botton is functional and navigate us on the Investor Login Page
    def test_InvestorLogin(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(HP.cookies))
        HP.closeCookies(self)
        HP.clickElement(self, HP.investorLoginXP)
        # wait = WebDriverWait(driver, 10)
        # wait.until(EC.visibility_of_element_located(HP.mLogo))
        # actualTitle = driver.title
        #
        # self.assertTrue(actualTitle == HP.titleText)
        # time.sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()





