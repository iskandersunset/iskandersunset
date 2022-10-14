import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome(executable_path='C:\\_teach\\Silenium\\chromedriver.exe')
s = Service('C:/_teach/Silenium/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
# driver.maximize_window()
# driver.implicitly_wait(10)


# print('Start test')
# visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
# visible_button.click()
# print('Finish test')


print('Start test')
visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='visibleAfter']")))
visible_button.click()
print('Finish test')
