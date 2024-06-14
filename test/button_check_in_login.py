from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from iniconfig.curl import *
from iniconfig import authorization
from iniconfig.locators import Locators

driver = webdriver.Chrome()
driver.maximize_window()

# Находимся на странице авторизации
driver.get(login_page)

# проходим авторизацию
driver = authorization(driver)

# Ждем загрузки "булки"
WebDriverWait(driver, 9).until(expected_conditions.visibility_of_element_located(Locators.inscription_bread))

# Проверяем что мы на основной странице сайта
assert driver.current_url == (main_page)

driver.quit()