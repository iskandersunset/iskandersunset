import datetime
import time

from selenium import webdriver
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


filter_site = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filter_site.click()
print('Click Filter')
time.sleep(3)
filter_site.send_keys(Keys.DOWN)
time.sleep(3)
filter_site.send_keys(Keys.RETURN)
print('Сортировка')
now_date = datetime.datetime.utcnow().strftime("%y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('C:\\_teach\\Silenium\\screenshots\\' + name_screenshot)
print('Создан скрин', name_screenshot)

