from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from iniconfig import authorization
from iniconfig.curl import *
from iniconfig.locators import Locators

driver = webdriver.Chrome()
driver.maximize_window()

# Находимся на cтранице регистрации
driver.get(register_page)

# Находим надпись "войти" и жмем
driver.find_element(*Locators.inscription_button_entrance).click()

driver = authorization(driver)

# Ждем "булки"
WebDriverWait(driver, 9).until(expected_conditions.visibility_of_element_located(Locators.inscription_bread))

# Проверяем что мы на основной странице сайта
assert driver.current_url == (main_page)

driver.quit()