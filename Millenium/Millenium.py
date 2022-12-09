import time
import unittest
import HomePage as HP
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

faker_class = Faker()


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_Millenium(self):
        driver = self.driver
        driver.get("https://www.mlp.com/")
        wait = WebDriverWait(driver, 3)

        action = webdriver.ActionChains(driver)

        time.sleep(2)

        action.move_to_element(HP.hamburger_menu).click().perform()
        wait.until(EC.visibility_of_element_located(HP.navigation_menu))
        print("Nav menu open")
        driver.get_screenshot_as_file('NavMenuOpen.png')

        self.assertTrue(self, HP.navigation_menu)

        #wait.until(EC.visibility_of_element_located(driver.find_element(By.ID, "//ul[@id='menu-primary-menu']"))



        # navmenu = navigation_menu.is_displayed()
        #unittest.TestCase.assertTrue(driver.find_element(By.ID, "//ul[@id='menu-primary-menu']"))

#         assert "California Real Estate" in driver.title
#         print("Driver title in Chrome is:", driver.title)
#
#         driver.find_element(By.ID, 'g2-name')
#         elem = driver.find_element(By.ID, 'g2-name')
#         elem.clear()
#         elem.send_keys(faker_class.name())
#
#         driver.find_element(By.NAME, 'g2-email')
#         elem = driver.find_element(By.ID, 'g2-email')
#         elem.clear()
#         elem.send_keys(faker_class.email())
#
#         driver.find_element(By.ID, 'contact-form-comment-g2-message')
#         elem = driver.find_element(By.ID, 'contact-form-comment-g2-message')
#         elem.clear()
#         elem.send_keys(faker_class.text())
#
#         driver.find_element(By.CLASS_NAME, 'pushbutton-wide').send_keys('\n').click()
#         time.sleep(2)
#         delay = 3
#
#         try:
#             WebDriverWait(driver, delay).until(
#                 EC.presence_of_element_located((
#                     By.XPATH, "//a[contains(text(),'go back')]"))).click()
#             print("California Real Estate Page is ready!")
#             driver.get_screenshot_as_file('ScreenshotCalifornia_page.png')
#         except TimeoutException:
#             print(
#                 "Can't find Element by src='https://qasvus.wordpress.com/?contact-form-hash=870c9c4c3793ec33a9fbd94db1a03cdcd56c1036'")
#             driver.get_screenshot_as_file('California_page_loading_error.png')
#
#         wait.until(EC.visibility_of_element_located((By.XPATH, '//alt[@class="wp-image-55 size-full"]')))
#         time.sleep(2)
#         wait.until(EC.visibility_of_element_located((By.XPATH, '//alt[@class="wp-image-34 size-full"]')))
#         time.sleep(2)
#         wait.until(EC.visibility_of_element_located((By.XPATH, '//alt[@class="wp-image-56 size-full"]')))
#         time.sleep(2)
#         wait.until(EC.visibility_of_element_located((By.XPATH, '//alt[@class="wp-image-30 size-full"]')))
#         time.sleep(2)
#
#         assert "California Real Estate" in driver.title
#         print("Page has", driver.title + "as Page title")
#
#     def tearDown(self):
#         self.driver.quit()
#
#
# class EdgeSearch(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Edge()
#
#     def test_edge_1250x850(self):
#         driver = self.driver
#         driver.set_window_size(1250, 850)
#         driver.get('https://qasvus.wordpress.com/')
#         wait = WebDriverWait(driver, 5)
#
#         wait.until(EC.visibility_of_element_located((By.XPATH, '//*[class="pushbutton-wide"]')))
#         wait.until(EC.visibility_of_element_located(By.ID, "contact-form-comment-g2-message"))
#
#         assert "California Real Estate" in driver.title
#         print("Driver title in Chrome is:", driver.title)
#
#         driver.find_element(By.ID, 'g2-name')
#         elem = driver.find_element(By.ID, 'g2-name')
#         elem.clear()
#         elem.send_keys(faker_class.name())
#
#         driver.find_element(By.NAME, 'g2-email')
#         elem = driver.find_element(By.ID, 'g2-email')
#         elem.clear()
#         elem.send_keys(faker_class.email())
#
#         driver.find_element(By.ID, 'contact-form-comment-g2-message')
#         elem = driver.find_element(By.ID, 'contact-form-comment-g2-message')
#         elem.clear()
#         elem.send_keys(faker_class.text())
#
#         driver.find_element(By.CLASS_NAME, 'pushbutton-wide').send_keys('\n').click()
#         time.sleep(2)
#
#         try:
#             WebDriverWait(driver, delay).until(
#                 EC.presence_of_element_located((
#                     By.XPATH, "//a[contains(text(),'go back')]")))
#             print("California Real Estate Page is ready!")
#             driver.get_screenshot_as_file('ScreenshotCalifornia_page.png').click()
#         except TimeoutException:
#             print(
#                 "Can't find Element by src='https://qasvus.wordpress.com/?contact-form-hash=870c9c4c3793ec33a9fbd94db1a03cdcd56c1036'")
#             driver.get_screenshot_as_file('California_page_loading_error.png')
#             driver.implicitly_wait(3)
#
#             wait.until(EC.visibility_of_element_located((By.XPATH, '//alt[@class="wp-image-55 size-full"]')))
#             time.sleep(2)
#             wait.until(EC.visibility_of_element_located((By.XPATH, '//alt[@class="wp-image-34 size-full"]')))
#             time.sleep(2)
#             wait.until(EC.visibility_of_element_located((By.XPATH, '//alt[@class="wp-image-56 size-full"]')))
#             time.sleep(2)
#             wait.until(EC.visibility_of_element_located((By.XPATH, '//alt[@class="wp-image-30 size-full"]')))
#             time.sleep(2)
#
#             assert "California Real Estate" in driver.title
#             print("Page has", driver.title + "as Page title")

    def tearDown(self):
        self.driver.quit()