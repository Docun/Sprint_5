from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from iniconf.locators import Locators
from iniconf.curl import *
import pytest

@pytest.mark.usefixtures("start_from_login_page")
class TestButtonCheckExit:

    def test_check_loging_out(slef, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Ждем загрузки "булок"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))

        # Кликаем по кнопке "личный кабинет"
        driver.find_element(*Locators.button_personal_area).click()

        # Ждем загрузки надписи "профиль"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_profile))

        # Кликаем по кнопке "выход"
        driver.find_element(*Locators.button_exit).click()

        # Ждем перехода на страницу логина
        WebDriverWait(driver, 10).until(EC.url_to_be(login_site))

        # Проверяем URL адрес страницы логина
        assert driver.current_url == login_site


@pytest.mark.usefixtures("start_from_site_not_login")
class TestBigMainButton:
    def test_check_entrance_by_big_button(self, start_from_site_not_login):
        driver = start_from_site_not_login
        driver.maximize_window()
        email = 'igor008@yandex.ru'
        password = '123456789'

        # Жмем кнопку "Войти в аккаунт"
        driver.find_element(*Locators.entrance_on_the_main).click()

        # Ищем поля и проходим авторизацию
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_entrance).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        # Проверяем что мы на основной странице сайта
        assert driver.current_url == main_site



@pytest.mark.usefixtures("start_from_recovery_page")
class TestCheckRegister:
    def test_login_password_recovery(self, start_from_recovery_page):
        driver = start_from_recovery_page
        driver.maximize_window()

        # Жмем загрузки "булок"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.inscription_bread)))

        # Проверяем что мы на основной странице сайта
        assert driver.current_url == main_site


@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckEntranceFromRecoveryPage:
    def test_button_inscription_login(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()
        email = 'igor008@yandex.ru'
        password = '123456789'

        # Жмем кнопку "зарегаться"
        driver.find_element(*Locators.inscription_login).click()

        # Жмем кнопку "войти"
        driver.find_element(*Locators.inscription_button_entrance).click()

        # Ищем поля и проходим авторизацию
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_entrance).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        # Проверяем что мы на основной странице сайта
        assert driver.current_url == main_site


