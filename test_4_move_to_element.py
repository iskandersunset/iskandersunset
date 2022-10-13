import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path='C:\\_teach\\Silenium\\chromedriver.exe')
s = Service('C:/_teach/Silenium/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
login_standard_user = "standard_user"
login_password_user = "secret_sauce"
driver.get(base_url)
# driver.maximize_window()

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")  # XPATH
user_name.send_keys(login_standard_user)
print("Input login")

user_pass = driver.find_element(By.XPATH, "//input[@id='password']")
user_pass.send_keys(login_password_user)
print("Input pass")
user_pass.send_keys(Keys.RETURN)
print("RETURN")
time.sleep(2)

'''Перемещение к определенному элементу страницы move_to_element'''
# driver.execute_script("window.scrollTo(0, 2500)")
# time.sleep(2)
action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
action.move_to_element(red_t_shirt).perform()
time.sleep(2)

now_date = datetime.datetime.utcnow().strftime("%y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('C:\\_teach\\Silenium\\screenshots\\' + name_screenshot)
print('Создан скрин', name_screenshot)

