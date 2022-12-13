
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class HomePage:

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    action = webdriver.ActionChains(driver)

    #locators
    navMenu = By.XPATH, "//ul[@id='menu-primary-menu']"
    hamburgerMenu = "//button[contains(@class,'primary-menu')]"
    cookies = driver.find_element(By.XPATH, "//body/div[@id='global_cookie_policy']/div[1]/div[1]/a[1]")




   #functions
    def pushHumburger(self):
        return self.action.move_to_element(self.driver.find_element(By.XPATH, self.hamburgerMenu))\
            .pause(1).click().perform()

