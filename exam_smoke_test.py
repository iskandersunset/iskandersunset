import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path='C:\\_teach\\Silenium\\chromedriver.exe')
s = Service('C:/_teach/Git/iskandersunset/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
login_standard_user = "standard_user"
login_password_user = "secret_sauce"
driver.get(base_url)
# driver.maximize_window()

"""1. Авторизоваться на сайте"""
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

"""2.Выбрать 2 товара Sauce Labs Bolt T-Shirt и Sauce Labs Fleece Jacket"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
value_price_product_1 = float(price_product_1.text[1:])
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
select_product_1.click()
print('Добавили в корзину первый выбранный товар\n', '--' * 20)

"""Добавляем второй товар"""
product_2 = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
value_price_product_2 = float(price_product_2.text[1:])
print(value_price_product_2)

select_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
select_product_2.click()
print('Добавили в корзину второй выбранный товар\n', '--' * 20)

"""Переходим в корзину"""
carpet = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
carpet.click()
print('Кликаем по кнопке корзина\n', '--' * 20)

"""Создаем переменные товаров и цен в корзине для сравнения с ценами в магазине"""
carpet_product_1 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_carpet_product_1 = carpet_product_1.text
print(value_carpet_product_1)

price_carpet_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']"
                                                       "/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_carpet_product_1 = float(price_carpet_product_1.text[1:])
print(value_price_carpet_product_1)
assert value_carpet_product_1 == value_product_1
print('Товар в корзине достоверный\n', '--' * 20)

carpet_product_2 = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
value_carpet_product_2 = carpet_product_2.text
print(value_carpet_product_2)

price_carpet_product_2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']"
                                                       "/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_carpet_product_2 = float(price_carpet_product_2.text[1:])
print(value_price_carpet_product_2)
assert value_carpet_product_2 == value_product_2
print('Товар в корзине достоверный\n', '--' * 20)

"""Переходим к вводу персональных данных и оплате"""
button_checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
button_checkout.click()
print('Кликаем по кнопке CHECKOUT\n', '--' * 20)

"""Вводим данные"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
first_name.send_keys('ПокупательИмя')
last_name.send_keys('ПокупательФамилия')
zip_code.send_keys('Индекс')
print('Ввели данные покупателя')
button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print('Кликаем по кнопке CONTINUE\n', '--' * 20)

"""Проверяем данные платежа: товары и сумму"""
final_product_1 = driver.find_element(By.XPATH, "//*[@id='item_1_title_link']")
value_final_product_1 = final_product_1.text
print(value_final_product_1)

price_final_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']"
                                                      "/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_final_product_1 = float(price_final_product_1.text[1:])
print(value_price_final_product_1)
assert value_final_product_1 == value_product_1
print('Товар в чеке достоверный\n', '--' * 20)

final_product_2 = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']")
value_final_product_2 = final_product_2.text
print(value_final_product_2)

price_final_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']"
                                                      "/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_final_product_2 = float(price_final_product_2.text[1:])
print(value_price_final_product_2)
assert value_final_product_2 == value_product_2
print('Товар в чеке достоверный\n', '--' * 20)

"""Сверяем сумму товаров с показанием в чеке и жмем финиш"""
total_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
value_total_price = total_price.text

"""Разбираем строку для поиска суммы"""
p = "[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+"
total_sum = 0
if re.search(p, value_total_price) is not None:
    for catch in re.finditer(p, value_total_price):
        try:
            total_sum = catch[0]
        except ValueError:
            print('Пусто')

assert float(total_sum) == value_price_carpet_product_1 + value_price_carpet_product_2
print('Сумма товаров совпадает:', total_sum)

button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
button_finish.click()
print('Кликаем по кнопке finish\n', '--' * 20)
