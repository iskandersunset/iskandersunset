import datetime  # Подключаем модуль работы с датой и временем
import time

from datetime import timedelta  # Сдвиг по дате и времени
from selenium import webdriver  # Собственно сам драйвер
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Методы поиска по id, классам селекторам и т.п.
from selenium.webdriver.common.keys import Keys  # Методы использования клавиатурных сокращений и самих клавиш

# Подготовка драйвера Selenium
s = Service('C:/Users/iskan/PycharmProjects/Selenium/chromedriver.exe')
driver = webdriver.Chrome(service=s)
# Задаем url страницы, с которой будем работать
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)

today = datetime.datetime.today()
print('Текущая дата от рождества Христова: ', today.strftime('%m/%d/%Y'))
delta_day = (today + timedelta(days=10)).strftime('%m/%d/%Y')

# Очищаем поле даты
driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']").send_keys(Keys.CONTROL + "a")
driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']").send_keys(Keys.DELETE)
# Устанавливаем локатор в поле даты
new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
time.sleep(2)
# Пересылаем данные даты со сдивгом в 10 дней
new_date.send_keys(delta_day)
# Подтверждаем нажатием Enter
driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']").send_keys(Keys.RETURN)
time.sleep(2)
print('Перенслись в будущее на :', delta_day)

value_fifnish_date = new_date.get_attribute('value')
assert value_fifnish_date == delta_day
print('Ура! Мы в будущем!')
