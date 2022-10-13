import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path='C:\\_teach\\Silenium\\chromedriver.exe')
s = Service('C:/_teach/Silenium/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://demoqa.com/dynamic-properties'
# login_standard_user = "standard_user"
# login_password_user = "secret_sauce"
driver.get(base_url)
# driver.maximize_window()


try:
    visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
except NoSuchElementException as exeption:
    print('Ошибка NoSuchElementException')
    time.sleep(10)
    visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
    print('Ткнули по кнопке')


