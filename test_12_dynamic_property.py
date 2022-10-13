import time

from selenium import webdriver
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

action = ActionChains(driver)
elements_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(elements_button).perform()
result_duble_click = driver.find_element(By.XPATH, "//p[@id='doubleClickMessage']").text
assert result_duble_click == 'You have done a double click'
print('Двжды кликнули')
time.sleep(2)

action = ActionChains(driver)
elements_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(elements_button).perform()
result_context_click = driver.find_element(By.XPATH, "//p[@id='rightClickMessage']").text
assert result_context_click == 'You have done a right click'
print('Правой кликнули')
time.sleep(2)
