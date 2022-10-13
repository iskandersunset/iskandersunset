import time
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome(executable_path='C:\\_teach\\Silenium\\chromedriver.exe')
s = Service('C:/_teach/Silenium/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://demoqa.com/date-picker'
# login_standard_user = "standard_user"
# login_password_user = "secret_sauce"
driver.get(base_url)
# driver.maximize_window()

# driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']").send_keys(Keys.CONTROL + "a")
# driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']").send_keys(Keys.DELETE)
# new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# time.sleep(3)
# new_date.send_keys('12/01/2222')
# time.sleep(3)

# Выбор даты в календаре и затем сброс на текщую дату
locator = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
locator.click()
print('Выбрали поле ввода даты')
time.sleep(3)
# tomorow_day = driver.find_element(By.XPATH, "//div[@aria-label='Choose Thursday, October 13th, 2022']")
# tomorow_day.click()
# print('Выбрали дату завтрешнего дня')
# time.sleep(3)
# # Тукщая дата
# locator = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# locator.click()
# print('Выбрали поле ввода даты')
# time.sleep(3)
# return_today = driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]")
# return_today.click()
# print('Вернулись на текущий день')

now_date = datetime.datetime.utcnow().strftime("%d")
need_date = int(now_date) + 1
print(need_date)

locator = "//div[@aria-label='Choose Thursday, October " + str(need_date) + "th, 2022']"
tomorrow_day = driver.find_element(By.XPATH, locator)
tomorrow_day.click()
print(locator)


# action = ActionChains(driver)
# elements_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
# action.double_click(elements_button).perform()
# result_duble_click = driver.find_element(By.XPATH, "//p[@id='doubleClickMessage']").text
# assert result_duble_click == 'You have done a double click'
# print('Двжды кликнули')
# time.sleep(2)
#
# action = ActionChains(driver)
# elements_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
# action.context_click(elements_button).perform()
# result_context_click = driver.find_element(By.XPATH, "//p[@id='rightClickMessage']").text
# assert result_context_click == 'You have done a right click'
# print('Правой кликнули')
# time.sleep(2)
