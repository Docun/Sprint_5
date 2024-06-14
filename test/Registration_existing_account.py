from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from iniconfig.curl import *
import selenium
from iniconfig.locators import Locators

driver = selenium.webdriver.Chrome()
driver.maximize_window()

#Находимся на странице логина
driver.get(login_page)

driver.find_element(*Locators.inscription_login).click()

# Найди поле "Имя" и заполни его
driver.find_element(*Locators.field_name).send_keys("Игорь")

# Найди поле "email" и заполни его
driver.find_element(*Locators.field_email).send_keys('igor008@yandex.ru')

# Найди поле "Пароль" и заполни его
driver.find_element(*Locators.field_password).send_keys('123456789')

# Жмем на зарегаться
driver.find_element(*Locators.button_login).click()

# Ждем ошибку регистрации
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(Locators.inscription_error_account))

driver.quit()