import time
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome(executable_path='C:\\_teach\\Silenium\\chromedriver.exe')
s = Service('http://automationpractice.com/index.php?id_category=3&controller=category')
driver = webdriver.Chrome(service=s)
base_url = 'https://demoqa.com/date-picker'
# login_standard_user = "standard_user"
# login_password_user = "secret_sauce"
driver.get(base_url)
# driver.maximize_window()

action = ActionChains(driver)
price = driver.find_element(By.XPATH, "//div[@id='layered_price_slider']")
print('Установили локатор на слайдер прайса')
action.click_and_hold(price).move_by_offset(20, 0).release().perform()
print('Поменяли цену')

