
import time
import random
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker

faker_class = Faker()


url = "https://www.mlp.com/"
hamburgerMenuXP = "//button[contains(@class,'primary-menu')]"
navMenuID = By.ID, 'menu-primary-menu'
cookiesXP = '//a[text() = "I AGREE "]'
cookies = By.XPATH, '//a[text() = "I AGREE "]'
mLogoXP = "//img[contains(@class,'icon icon-white')]"
mLogo = By.XPATH, "//img[contains(@class,'icon icon-white')]"
titleText = "Millennium Management Global Investment"
investorLoginXP = '//a[text() = " investor login "]'


def delay():
    time.sleep(random.randint(1, 3))


def clickElement(self, elementxp):
    driver = self.driver
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, elementxp)).click().perform()


def closeCookies(self):
    driver = self.driver
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, cookiesXP)).click().perform()














