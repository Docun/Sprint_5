from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from iniconfig import authorization
from iniconfig.curl import *
import time
from iniconfig.locators import Locators

driver = webdriver.Chrome()
driver.maximize_window()

# Находимся на странице авторизации
driver.get(login_page)

# Проходим авторизацию
driver = authorization(driver)

# Жмем загрузки "булок"
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(Locators.inscription_bread))

# Кликаем по кнопке "личный кабинет"
driver.find_element(*Locators.button_personal_area).click()

# Ждем загрузки "профиль"
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(Locators.inscription_profile))

time.sleep(1)

# Проверяем что мы на странице профиля
assert driver.current_url == (profile_page)

driver.quit()