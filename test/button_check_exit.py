from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from iniconfig.curl import *
from iniconfig import authorization
from iniconfig.locators import Locators

driver = webdriver.Chrome()
driver.maximize_window()

# Находимся на странице авторизации
driver.get(login_page)

# Выполняем логин
driver = authorization(driver)

# Жмем загрузки "булок"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.inscription_bread)))

# Кликаем по кнопке "личный кабинет"
driver.find_element(*Locators.button_personal_area).click()

# Ждем загрузки надписи "профиль"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.inscription_profile))

# Кликаем по кнопке "выход"
driver.find_element(*Locators.button_exit).click()

time.sleep(1)

# Проверяем что мы на странице логина
assert driver.current_url == (login_page)

driver.quit()
