
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

mainTextInvestorLogin = By.XPATH, "//div[contains(text(),'Investor login')]"
TextInvestorLoginXP = "//div[contains(text(),'Investor login')]"
