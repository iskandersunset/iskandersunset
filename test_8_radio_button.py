import time

from selenium import webdriver
#from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path='C:\\_teach\\Silenium\\chromedriver.exe')
s = Service('C:/_teach/Silenium/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://demoqa.com/'
# login_standard_user = "standard_user"
# login_password_user = "secret_sauce"
driver.get(base_url)
# driver.maximize_window()

elements_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[1]")
elements_button.click()
time.sleep(2)

radio_menu = driver.find_element(By.XPATH, "//li[@id='item-2']")
radio_menu.click()
time.sleep(2)

yes_radio = driver.find_element(By.XPATH, "//label[@class='custom-control-label']")
yes_radio.click()
time.sleep(2)

# check_box = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
# check_box.click()
# time.sleep(4)