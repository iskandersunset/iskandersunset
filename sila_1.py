import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.saucedemo.com/')
driver.maximize_window()
# user_name = driver.find_element(By.ID, "user-name")  # ID
# user_name = driver.find_element(By.NAME, "user-name")  # NAME
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")  # XPATH
user_name.send_keys("standard_user")
# user_pass = driver.find_element(By.XPATH, "//input[@id='password']")  # XPATH
user_pass = driver.find_element(By.CSS_SELECTOR, "#password")  # CSS_SELECTOR
user_pass.send_keys("secret_sauce")
login = driver.find_element(By.CSS_SELECTOR, "#login-button")  # CSS_SELECTOR
login.click()

time.sleep(20)
# driver.close()
