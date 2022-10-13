import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path='C:\\_teach\\Silenium\\chromedriver.exe')
s = Service('C:/Users/iskan/PycharmProjects/Selenium/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://demoqa.com/buttons'
login_standard_user = "standard_user"
login_password_user = "secret_sauce"
driver.get(base_url)
# driver.maximize_window()

action = ActionChains(driver)
double = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double).perform()

double_value = driver.find_element(By.XPATH, "//p[@id='doubleClickMessage']").text
assert double_value
print(double_value)

time.sleep(3)

right = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right).perform()
print("Right Click")
time.sleep(3)
