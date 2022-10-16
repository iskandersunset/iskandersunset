import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path='C:\\_teach\\Silenium\\chromedriver.exe')
s = Service('C:/Users/iskan/PycharmProjects/Selenium/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
login_standard_user = "standard_user"
login_password_user = "secret_sauce"
driver.get(base_url)
# driver.maximize_window()

# 1. Авторизоваться на сайте
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input login")
time.sleep(1)

user_pass = driver.find_element(By.XPATH, "//input[@id='password']")
user_pass.send_keys(login_password_user)
print("Input pass")
time.sleep(1)

user_pass.send_keys(Keys.RETURN)
print('RETURN\n', '--' * 20)
time.sleep(1)

# 2.Выбрать 2 товара Sauce Labs Bolt T-Shirt и Sauce Labs Fleece Jacket
product_1 = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
for i in range(len(product_1)):
    print(product_1[i].text)

# print(product_1)

