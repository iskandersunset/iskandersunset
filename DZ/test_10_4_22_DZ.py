import time
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome(executable_path='C:\\_teach\\Silenium\\chromedriver.exe')
s = Service('/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://demoqa.com/date-picker'
# login_standard_user = "standard_user"
# login_password_user = "secret_sauce"
driver.get(base_url)
# driver.maximize_window()

# Выбор даты в календаре и затем сброс на текщую дату
locator = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
locator.click()
print('Выбрали поле ввода даты')
time.sleep(3)
today_date = datetime.datetime.utcnow().strftime("%d/%M/%Y")
# print(type(today_date))
day_date = today_date[:1]
print(day_date)

print(today_date)
locator.send_keys()
# print(need_date)

# locator = "//div[@aria-label='Choose Thursday, October " + str(need_date) + "th, 2022']"
# tomorrow_day = driver.find_element(By.XPATH, locator)
# tomorrow_day.click()
# print(locator)