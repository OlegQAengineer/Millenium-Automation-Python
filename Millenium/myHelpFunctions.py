import time
import random
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker

faker_class = Faker()


def delay():
    time.sleep(random.randint(1, 3))


def clickElement(self, elementxp):
    driver = self.driver
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, elementxp)).click().perform()

def clickElements(self, element):
    driver = self.driver
    action = ActionChains(driver)
    action.move_to_element(element).click().perform()

def ScrolDownToElement(self, element):
    el = int(element.rect['y'])
    ActionChains(self) \
        .scroll_by_amount(0, el) \
        .perform()


# Scrolling page sown element must be visible
def ScrolDownToEndPage(element):
    element.send_keys(Keys.END)


# Scroling page UP  element must be visible
def ScrolDownToUpPage(element):
    element.send_keys(Keys.HOME)
