import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
# driver.maximize_window()

login_standard_user = "standard_use"
login_password_user = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")  # XPATH
user_name.send_keys(login_standard_user)
print("Input login")
user_pass = driver.find_element(By.XPATH, "//*[@id='password']")
user_pass.send_keys(login_password_user)
print("Input pass")
button_login = driver.find_element(By.XPATH, "//*[@id='login-button']")
button_login.click()
print("Click Login")

"""Проверка реакции на ошибочно введенный логин standart-use"""
warring_text = button_login = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_test = warring_text.text
assert value_warring_test == "Epic sadface: Username and password do not match any user in this service"
print("GOOD test")

driver.refresh()

time.sleep(5)
