from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from iniconfig.curl import *
from iniconfig import authorization
from iniconfig.locators import Locators

driver = webdriver.Chrome()
driver.maximize_window()

# Находимся на главной странице
driver.get(main_page)

# Кликаем по кнопке "личный кабинет"
driver.find_element(*Locators.button_personal_area).click()

# Выполняем логин
driver = authorization(driver)

# Ждем кнопку "булки"
WebDriverWait(driver, 9).until(expected_conditions.visibility_of_element_located(Locators.inscription_bread))

# Проверяем что мы на основной странице сайта
assert driver.current_url == (main_page)

driver.quit()