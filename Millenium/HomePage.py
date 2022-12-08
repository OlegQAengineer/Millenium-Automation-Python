from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
# updated webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

urlMillenium = "https://www.mlp.com/"
action = webdriver. ActionChains(driver)

# Locators
hamburger_menu = driver.find_element(By.XPATH, "//button[contains(@class,'MobileNav')]")
navigation_menu = driver.find_element(By.ID, "//ul[@id='menu-primary-menu']")

# Functions


def daley1_5():
    time.sleep(random.randint(1, 5))


def daley1_3():
    time.sleep(random.randint(1, 3))


def clickHumburgerMenu(self):
    action.move_to_element(hamburger_menu).click()




