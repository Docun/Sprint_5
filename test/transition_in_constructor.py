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

# Проходим авторизацию
driver = authorization(driver)

# Жмем загрузки "булок"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.inscription_bread)))

# Кликаем по кнопке "личный кабинет"
driver.find_element(*Locators.button_personal_area).click()

# Ждем загрузки надписи "профиль"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.inscription_profile))

# Кликаем по кнопке "конструктор"
driver.find_element(*Locators.button_constaction).click()

# Ждем загрузки "булок"
WebDriverWait(driver, 9).until(expected_conditions.visibility_of_element_located(Locators.inscription_bread))

# Проверяем что мы на основной странице
assert driver.current_url == (main_page)

driver.quit()