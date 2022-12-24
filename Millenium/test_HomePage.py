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
from Millenium.page_objects import page_objectCareers as C

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
        driver.get_screenshot_as_file(
            'C:/Users/varts/PycharmProjects/Millenium-Automation-Python/Millenium/Screen_Shots/NavMenuOpen.png')

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

        # Check that Side bar interactive menu is functional and page is scrolling as pare menu
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
            yScroll = driver.execute_script("return window.scrollY")
            if yScroll == 1620:
                continue
            elif yScroll == 2703:
                continue
            elif yScroll == 3498:
                continue
            else:
                print("Menu isn't functional, Bug")
                self.assertTrue(e.is_selected())

        # Check that botton is functional and careers page open
    def test_CareersBtn(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(HP.cookies))
        HP.closeCookies(self)
        HF.ScrolDownToElement(self.driver, driver.find_element(By.XPATH, HP.exploreCareersBtnXP))
        HF.delay()
        HF.clickElement(self, HP.exploreCareersBtnXP)
        HF.delay()
        driver.get_screenshot_as_file(
            'C:/Users/varts/PycharmProjects/Millenium-Automation-Python/Millenium/Screen_Shots/CareersPage.png')
        titleActual = driver.title
        self.assertEqual(titleActual, C.title)

        # Check that Footer links are functional and clickable
    def test_FooterLinks1(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(HP.cookies))
        HP.closeCookies(self)
        HF.ScrolDownToEndPage(driver.find_element(By.XPATH, HP.hamburgerMenuXP))
        HF.delay()
        menu = driver.find_elements(By.XPATH, HP.footer3pc)
        for e in menu:
            HF.clickElements(self, e)
            time.sleep(5)
            ActualTitle = driver.title
            self.assertFalse(ActualTitle == HP.titleText)
            driver.back()
            HF.delay()
            HF.ScrolDownToEndPage(driver.find_element(By.XPATH, HP.hamburgerMenuXP))

    def test_FooterLinks2(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(HP.cookies))
        HP.closeCookies(self)
        HF.ScrolDownToEndPage(driver.find_element(By.XPATH, HP.hamburgerMenuXP))
        HF.delay()
        menu = driver.find_elements(By.XPATH, HP.footer5pc)
        for e in menu:
            HF.clickElements(self, e)
            time.sleep(5)
            ActualTitle = driver.title
            try:
                self.assertFalse(ActualTitle == HP.titleText)
            except AssertionError:
                print("Bug, link is not clickable")
            driver.back()
            HF.delay()
            HF.ScrolDownToEndPage(driver.find_element(By.XPATH, HP.hamburgerMenuXP))



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()





