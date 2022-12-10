
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class HomePage():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    action = webdriver.ActionChains(driver)
    #locators
    hamburgerMenu = "//button[contains(@class,'primary-menu')]"
    navMenu = "menu-primary-menu"

   #functions
    def pushHumburger(self):
        return self.action.move_to_element(self.driver.find_element(By.XPATH, self.hamburgerMenu)).click().perform()
