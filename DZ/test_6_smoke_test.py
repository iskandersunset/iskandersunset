import time

from selenium import webdriver
#from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path='C:\\_teach\\Silenium\\chromedriver.exe')
s = Service('/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
login_standard_user = "standard_user"
login_password_user = "secret_sauce"
driver.get(base_url)
# driver.maximize_window()

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input login")
time.sleep(1)

user_pass = driver.find_element(By.XPATH, "//input[@id='password']")
user_pass.send_keys(login_password_user)
print("Input pass")
time.sleep(1)

user_pass.send_keys(Keys.RETURN)
print("RETURN")
time.sleep(1)

"""Информация о первом товаре"""
product_1 = driver .find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
value_select_product_1 = select_product_1.text
select_product_1.click()
print('Clik добавить в корзину')

carpet = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
carpet.click()
print('Click по корзине')

"""Информация по товару 1 в корзине"""
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print('Инфо о товаре 1 гуд')

price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_cart_product_1 = price_cart_product_1.text
print(value_price_cart_product_1)
assert value_price_product_1 == value_price_cart_product_1
print('Инфо о цене на товара совпадает')

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print('Клик по кнопке checkout')

"""Подтверждение инфо о покупателе"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('ПокупательИмя')
print("Ввели имя покупателя")
time.sleep(1)

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('ФамилияПокупателя')
print("Ввели фамилию покупателя")
time.sleep(1)

postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys('ПочтовыйИндекс')
print("Ввели индекс покупателя")
time.sleep(1)

button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print('Клик по кнопке continue')

"""Сверяем результаты цены и описания товара"""
over_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_over_product_1 = over_product_1.text
print(value_over_product_1)
assert value_product_1 == value_over_product_1
print('Инфо о товаре 1 гуд2')

price_over_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_over_product_1 = price_over_product_1.text
print(value_price_over_product_1)
assert value_price_product_1 == value_price_over_product_1
print('Инфо о цене на товара совпадает')

button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
button_finish.click()
print('Клик по кнопке finish')
