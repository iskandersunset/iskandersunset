"""Тестирование покупки 1 еденицы товара при случайном выборе пользователя"""
import time

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

number = int(input('Из данного списка выберите номер товара для дальнейшей проверки: '))
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
print('Запускаем тест товара под номером ' + str(number) + '\n', '---' * 20)

# driver = webdriver.Chrome(executable_path='C:\\_teach\\Silenium\\chromedriver.exe')
# s = Service('C:/Users/iskan/PycharmProjects/Selenium/chromedriver.exe')
s = Service('C:/_teach/Silenium/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
login_standard_user = "standard_user"
login_password_user = "secret_sauce"
driver.get(base_url)
# driver.maximize_window()

# 1. Авторизоваться на сайте
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys(login_standard_user)
print("Ввели логин")
time.sleep(1)

user_pass = driver.find_element(By.ID, "password")
user_pass.send_keys(login_password_user)
print("Ввели пароль")
time.sleep(1)

user_pass.send_keys(Keys.RETURN)
print('Нажали Еnter\n', '--' * 20)
time.sleep(1)

# 2.Получаем списки товаров на главной странице
products_inventory = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
price_products = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
print('Считали списки товаров и цен\n', '--' * 20)
time.sleep(1)

# 2. Выбираем товар по имени выбранному при вводе
name_product_inventory = products_inventory[number - 1].text
price_product_inventory = float(price_products[number - 1].text[1:])
products_inventory[number - 1].click()
print('Кликаем по имени выбранного товара и проходим в подробное описание\n', '--' * 20)
time.sleep(3)

# 2.Получаем данные на странице подробного описания
products_details = driver.find_elements(By.CLASS_NAME, "inventory_details_name")[0].text
price_details = float(driver.find_elements(By.CLASS_NAME, "inventory_details_price")[0].text[1:])

# Сравниваем имя товара и цену с исходной
assert name_product_inventory == products_details
print('Наименование товара совпадает с выбранным:', name_product_inventory)

assert price_product_inventory == price_details
print('Цена товара совпадает с исходной:', price_details, '\n', '---' * 20)

# Кликаем по кнопке добавить товар в корзину
driver.find_element(By.CLASS_NAME, "btn_inventory").click()
print('Кликаем по кнопке Add to cart\n', '---' * 20)
time.sleep(3)

shopping_cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
assert int(shopping_cart_badge.text) == 1
print('Товар добавлен в корзину 1 штук')
time.sleep(3)

# Кликаем по иконке корзина
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
print('Кликаем по иконкн корзина\n', '---' * 20)
time.sleep(3)

# Сверяем данные в корзине с исходными
name_product_cart = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
price_cart = float(driver.find_elements(By.CLASS_NAME, "inventory_item_price")[0].text[1:])

assert name_product_cart == name_product_inventory
print('Имя товара совпало с исходным:', name_product_cart)

assert price_cart == price_product_inventory
print('Цена товара совпала с исходным:', price_cart)

# Кликаем по иконке CHECKOUT
driver.find_element(By.CLASS_NAME, "checkout_button").click()
print('Кликаем по кнопке CHECKOUT\n', '---' * 20)
time.sleep(3)

# Вводим данные
first_name = driver.find_element(By.ID, "first-name")
last_name = driver.find_element(By.ID, "last-name")
zip_code = driver.find_element(By.ID, "postal-code")
first_name.send_keys('Петров')
last_name.send_keys('Петр')
zip_code.send_keys('454000')
print('Ввели данные покупателя')
button_continue = driver.find_element(By.CLASS_NAME, "btn_action")
button_continue.click()
print('Кликаем по кнопке CONTINUE\n', '--' * 20)

# Сверяем данные в чеке с данными в магазине
name_products_check = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text
price_check = float(driver.find_elements(By.CLASS_NAME, "inventory_item_price")[0].text[1:])
price_final = float(driver.find_elements(By.CLASS_NAME, "summary_subtotal_label")[0].text.replace('Item total: $', ''))

assert name_products_check == name_product_inventory
print('Наименование товара совпадает', name_products_check)
assert price_check == price_details == price_final
print('Цена товара актуальна', price_final, '\n', '--' * 20)

button_finish = driver.find_element(By.CLASS_NAME, "cart_button")
button_finish.click()
print('Кликаем по кнопке FINISH\n', '--' * 20)

# Проверка финишного сообщения о покупке
finish = driver.find_element(By.CLASS_NAME, "complete-header").text
assert finish == 'THANK YOU FOR YOUR ORDER'
print('Тест пройден')
