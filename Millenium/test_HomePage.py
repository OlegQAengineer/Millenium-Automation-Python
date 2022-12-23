import time
import unittest
from _ast import arguments

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import actions

from Millenium import myHelpFunctions as HF
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Millenium.page_objects import page_objectHomeP as HP
from Millenium.page_objects import page_objectInvestorLogin as IL


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
        HF.clickElement(self, HP.hamburgerMenuXP)
        self.assertTrue(EC.visibility_of_element_located(HP.navMenuID))
        HF.delay()
        driver.get_screenshot_as_file('C:/Users/varts/PycharmProjects/Millenium-Automation-Python/Millenium/Screen_Shots/NavMenuOpen.png')

    # Check that logo 'm' is functional and leave us on the Home page
    def test_mLogo(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(HP.cookies))
        HP.closeCookies(self)
        HF.clickElement(self, HP.mLogoXP)
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
        HF.clickElement(self, HP.investorLoginXP)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(IL.mainTextInvestorLogin))
        ActualText = driver.find_element(By.XPATH, IL.TextInvestorLoginXP).is_displayed()

        self.assertTrue(ActualText)

        # Check that Arrow botton is functional and scrolldown up to block "Operating System"
    def test_ArrowFunctional(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(HP.cookies))
        HP.closeCookies(self)
        driver.find_element(By.XPATH, HP.arrowDownXP).click()
        HF.delay()
        yScroll = driver.execute_script("return window.scrollY")
        self.assertEqual(yScroll, 654)

    # Check that vidio block botton is functional and vidio open
    def test_VidioBlockBotton(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(HP.cookies))
        HP.closeCookies(self)
        HF.ScrolDownToElement(self.driver, driver.find_element(By.XPATH, HP.vidioPlayBtnXP))
        HF.delay()
        HF.clickElement(self, HP.vidioPlayBtnXP)
        HF.delay()
        styleActual = driver.find_element(By.XPATH, HP.vidioBlockXP).get_attribute("style")
        self.assertEqual(styleActual, "display: none;")

        # Check that Side bar interactive menu is functional
    def test_SidebarInteractiveMenu(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(HP.cookies))
        HP.closeCookies(self)
        HF.ScrolDownToElement(self.driver, driver.find_element(By.XPATH, HP.textInvestingEnv))
        HF.delay()
        menu = driver.find_elements(By.XPATH, HP.sideBarMenu3pc)
        for e in menu:
            HF.clickElements(self, e)
            HF.delay()
        # HF.clickElement(self, '//p[text() = "unique investing environment"]')
        # time.sleep(2)
        # yScroll = driver.execute_script("return window.scrollY")
        # print(yScroll, "pixeli")
        # driver.find_element(By.XPATH, HP.arrowDownXP).click()
        # HF.delay()
        # yScroll = driver.execute_script("return window.scrollY")
        # self.assertEqual(yScroll, 654)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()





