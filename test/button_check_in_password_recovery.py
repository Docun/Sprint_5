from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from iniconfig.curl import *
from iniconfig import authorization
from iniconfig.locators import Locators

driver = webdriver.Chrome()
driver.maximize_window()

# Стартуем со страницы логина и пароля
driver.get(login_page)

# Кликаем по кнопке "востановить пароль"
driver.find_element(*Locators.button_restore_password).click()

# Ждем загрузку кнопку "войти"
WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.inscription_button_entrance))

# Кликаем по маленькой кнопке "войти"
driver.find_element(*Locators.inscription_button_entrance).click()

driver = authorization(driver)

# Ждем загрузку "булок"
WebDriverWait(driver, 9).until(expected_conditions.visibility_of_element_located((Locators.inscription_bread)))

# Проверяем что мы на основной странице сайта
assert driver.current_url == (main_page)

driver.quit()