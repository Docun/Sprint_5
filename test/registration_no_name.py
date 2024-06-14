import time

from iniconfig.curl import *
from selenium import webdriver
from iniconfig.locators import Locators
from iniconfig import authorization_two

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(register_page)

driver = authorization_two(driver)

# Жмем на зарегаться
driver.find_element(*Locators.button_login).click()

# Ждем и проверяем что мы на странице регистрации
current_url = driver.current_url
assert current_url == (register_page)

driver.quit()
