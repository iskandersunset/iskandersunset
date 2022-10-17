import time

import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Ввод пользователем необходимого товара
print('1) Sauce Labs Backpack')
print('2) Sauce Labs Bike Light')
print('3) Sauce Labs Bolt T-Shirt')
print('4) Sauce Labs Fleece Jacket')
print('5) Sauce Labs Onesie')
print('6) Test.allTheThings() T-Shirt (Red)')
number = input('Из данного списка выберите номер товара для дальнейшей проверки: ')
if number == 1:
    print('Выбранный товар - Sauce Labs Backpack')
elif number == 2:
    print('Sauce Labs Bike Light')
elif number == 3:
    print('Sauce Labs Bolt T-Shirt')
elif number == 4:
    print('Sauce Labs Fleece Jacket')
elif number == 5:
    print('Sauce Labs Onesie')
elif number == 6:
    print('Test.allTheThings() T-Shirt (Red)')
print('Запускаем тест товара под номером ' + number + '\n', '---' * 20)


# driver = webdriver.Chrome(executable_path='C:\\_teach\\Silenium\\chromedriver.exe')
# s = Service('C:/Users/iskan/PycharmProjects/Selenium/chromedriver.exe')
s = Service('C:/_teach/Silenium/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
login_standard_user = "standard_user"
login_password_user = "secret_sauce"
driver.get(base_url)


# 1. Авторизоваться на сайте
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Ввели логин")
time.sleep(1)

user_pass = driver.find_element(By.XPATH, "//input[@id='password']")
user_pass.send_keys(login_password_user)
print("Ввели пароль")
time.sleep(1)

user_pass.send_keys(Keys.RETURN)
print('Нажали Еnter\n', '--' * 20)
time.sleep(2)

# 2.Получаем списки товаров на главной странице
products_inventory = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
price_products_inventory = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
# print(products_inventory)
# print(float(price_products_inventory[5].text[1:]))
print('Считали список товаров\n', '--' * 20)
time.sleep(2)


