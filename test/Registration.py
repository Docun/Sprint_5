from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from iniconfig.locators import Locators
from iniconfig.geniration_ep import generate_email_password
from iniconfig.curl import *
import selenium

driver = selenium.webdriver.Chrome()
driver.maximize_window()
email, password = generate_email_password()

#Находимся на странице логина
driver.get(login_page)

driver.find_element(*Locators.inscription_login).click()

# Найди поле "Имя" и заполни его
driver.find_element(*Locators.field_name).send_keys("Игорь")

# Найди поле "email" и заполни его
driver.find_element(*Locators.field_email).send_keys(email)

# Найди поле "Пароль" и заполни его
driver.find_element(*Locators.field_password).send_keys(password)

# Жмем на зарегаться
driver.find_element(*Locators.button_login).click()

# Ждем кнопку войти
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(Locators.button_entrance))

# Проверяем что мы на странице авторизации
assert driver.current_url == (login_page)

driver.quit()