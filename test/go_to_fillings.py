from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from iniconfig import authorization
from iniconfig.curl import *
from iniconfig.locators import Locators

driver = webdriver.Chrome()
driver.maximize_window()

# Находимся на странице логина
driver.get(login_page)

# Проходим авторизацию
driver = authorization(driver)

# Ждем загрузки "оформить заказ"
WebDriverWait(driver, 9).until(expected_conditions.visibility_of_element_located(Locators.button_arrange_order))

# Кликаем по кнопке "Соусы"
driver.find_element(*Locators.inscription_sause).click()

# Ждем загрузки "оформить заказ"
WebDriverWait(driver, 9).until=(expected_conditions.visibility_of_element_located(Locators.button_arrange_order))

driver.quit()