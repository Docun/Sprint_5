from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from iniconf.geniration_ep import EmailPasswordGenerator
from iniconf.locators import Locators
from iniconf.curl import *
import pytest

@pytest.mark.usefixtures("resister_new_account")
class TestCheckNewRegister:
    def test_registration(self, resister_new_account):
        driver, email, password = resister_new_account
        driver.maximize_window()

        # Ищем поле "email" и заполни его
        driver.find_element(*Locators.field_email).send_keys(email)

        # Ищем поле "Пароль" и заполни его
        driver.find_element(*Locators.field_password).send_keys(password)

        # Находим надпись "войти" и жмем
        driver.find_element(*Locators.button_entrance).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        # Проверяем что мы авторизовались созданным аккаунтом перейдя на главную страницу
        assert driver.current_url == main_site

@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckingCreationExistingAccount:
    def test_existing_acount(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()
        # Используем данные уже созданного аккаунта
        name = 'Игорь'
        email = 'igor008@yandex.ru'
        password = '123456789'

        driver.find_element(*Locators.inscription_login).click()

        # Найди поле "Имя" и заполни его
        driver.find_element(*Locators.field_name).send_keys(name)

        # Найди поле "email" и заполни его
        driver.find_element(*Locators.field_email).send_keys(email)

        # Найди поле "Пароль" и заполни его
        driver.find_element(*Locators.field_password).send_keys(password)

        # Жмем на зарегаться
        driver.find_element(*Locators.button_login).click()

        # Ждем ошибку регистрации
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.inscription_error_account))

@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckRegisterNoName:
    def test_registration_no_name(self, start_from_main_not_login):
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

        # Проверяем что мы на странице регистрации
        assert driver.current_url == register_site

@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckingErrorPassword:
    def test_error_password(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()
        # Используем данные c ошибкой в поле "пароль"
        name = 'Игорь'
        email = 'igor008@yandex.ru'
        password = '123'

        driver.find_element(*Locators.inscription_login).click()

        # Найди поле "Имя" и заполни его
        driver.find_element(*Locators.field_name).send_keys(name)

        # Найди поле "email" и заполни его
        driver.find_element(*Locators.field_email).send_keys(email)

        # Найди поле "Пароль" и заполни его
        driver.find_element(*Locators.field_password).send_keys(password)

        # Жмем на зарегаться
        driver.find_element(*Locators.button_login).click()

        # Ждем ошибку регистрации
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_error_password))


@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckingErrorPassword:
    def test_no_password(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()
        # Используем данные без пароля
        name = 'Игорь'
        email = 'igo@yandex.ru'

        driver.find_element(*Locators.inscription_login).click()

        # Найди поле "Имя" и заполни его
        driver.find_element(*Locators.field_name).send_keys(name)

        # Найди поле "email" и заполни его
        driver.find_element(*Locators.field_email).send_keys(email)

        # Жмем на зарегаться
        driver.find_element(*Locators.button_login).click()

        # Проверка текущего URL, должны остаться на странице регистрации
        assert driver.current_url == register_site
