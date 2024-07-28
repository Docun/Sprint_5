from iniconf.locators import Locators
from iniconf.curl import *
from iniconf.geniration_ep import EmailPasswordGenerator

def test_registration_no_name(start_from_main_not_login):
    driver = start_from_main_not_login
    driver.maximize_window()

    # Кликаем по надписи "Зарегистрироваться"
    driver.find_element(*Locators.inscription_login).click()

    # Генерация email и password
    generator = EmailPasswordGenerator()
    email, password = generator.generate()

    # Ищем поле "email" и заполни его
    driver.find_element(*Locators.field_email).send_keys(email)

    # Ищем поле "Пароль" и заполни его
    driver.find_element(*Locators.field_password).send_keys(password)

    # Жмем на кнопку зарегаться
    driver.find_element(*Locators.button_login).click()

    # Жмем на зарегаться
    driver.find_element(*Locators.button_login).click()

    # Проверяем что мы на странице регистрации
    assert driver.current_url == (register_page)

    driver.quit()

