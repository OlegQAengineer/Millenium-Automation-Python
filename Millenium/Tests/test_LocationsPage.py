import time
import unittest
from Millenium import myHelpFunctions as HF
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Millenium.page_objects import page_objectHomeP as HP
from Millenium.page_objects import page_objectInvestorLogin as IL
from Millenium.page_objects import page_objectLocations as L


class LocationsPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(HP.url)
        time.sleep(3)

    # Check that a humburger menu is functional and navigation menu appear on the Locations page
    def test_burgermenu(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(HP.cookies))
        HP.closeCookies(self)
        HF.clickElement(self, HP.hamburgerMenuXP)
        wait.until(EC.visibility_of_element_located(L.navMenuID))
        HF.clickElement(self, HP.locations)
        HF.delay()
        HF.clickElement(self, L.hamburgerMenuXP)
        self.assertTrue(EC.visibility_of_element_located(L.navMenuID))
        HF.delay()

    # Check that logo 'm' is functional and leave us on the Home page
    def test_mLogo(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(HP.cookies))
        HP.closeCookies(self)
        HF.clickElement(self, HP.hamburgerMenuXP)
        wait.until(EC.visibility_of_element_located(L.navMenuID))
        HF.clickElement(self, HP.locations)
        HF.delay()
        HF.clickElement(self, L.mLogoXP)
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
        HF.clickElement(self, HP.hamburgerMenuXP)
        wait.until(EC.visibility_of_element_located(L.navMenuID))
        HF.clickElement(self, HP.locations)
        HF.delay()
        HF.clickElement(self, L.investorLoginXP)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(IL.mainTextInvestorLogin))
        ActualText = driver.find_element(By.XPATH, IL.TextInvestorLoginXP).is_displayed()

        self.assertTrue(ActualText)

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
