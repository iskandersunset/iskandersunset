import time

from selenium import webdriver
#from selenium.webdriver import ActionChains
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

menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")  # XPATH
menu.click()
print("Click Menu Button")
time.sleep(3)

link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
link_about.click()
print("Click Link About")
time.sleep(3)

driver.back()
print('Нажали кнопку back в броузере')
time.sleep(10)
driver.forward()
print('Нажали кнопку forward в броузере')