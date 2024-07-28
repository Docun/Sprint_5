from selenium import webdriver
from iniconf.locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from iniconf.geniration_ep import EmailPasswordGenerator
import pytest



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def start_from_login_page(driver):
    email = 'igor008@yandex.ru'
    password = '123456789'
    login_page = 'https://stellarburgers.nomoreparties.site/login'
    driver.get(login_page)
    authorization_entrance(driver, email, password)
    return driver

@pytest.fixture
def start_from_recovery_page(driver):
    login_page = 'https://stellarburgers.nomoreparties.site/login'
    driver.get(login_page)

    # Кликаем по кнопке "востановить пароль"
    driver.find_element(*Locators.button_restore_password).click()

    # Ждем загрузку кнопки "войти"
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.inscription_button_entrance))

    # Кликаем по маленькой кнопке "войти"
    driver.find_element(*Locators.inscription_button_entrance).click()

    # Вход в систему
    email = 'igor008@yandex.ru'
    password = '123456789'
    authorization_entrance(driver, email, password)

    return driver

@pytest.fixture
def start_from_main_page(driver):
    main_page = 'https://stellarburgers.nomoreparties.site/'
    driver.get(main_page)

    # Кликаем по кнопке "личный кабинет"
    driver.find_element(*Locators.button_personal_area).click()

    # Кликаем по маленькой кнопке "войти"
    driver.find_element(*Locators.button_entrance).click()

    # Вход в систему
    email = 'igor008@yandex.ru'
    password = '123456789'
    authorization_entrance(driver, email, password)

    return driver

@pytest.fixture
def start_from_register_page(driver):
    register_page = 'https://stellarburgers.nomoreparties.site/register'
    driver.get(register_page)

    # Находим надпись "войти" и жмем
    driver.find_element(*Locators.inscription_button_entrance).click()

    # Вход в систему
    email = 'igor008@yandex.ru'
    password = '123456789'
    authorization_entrance(driver, email, password)

    return driver

@pytest.fixture
def start_from_main_not_login(driver):
    login_page = 'https://stellarburgers.nomoreparties.site/login'
    driver.get(login_page)

    return driver

@pytest.fixture
def resister_new_account(driver):
    login_page = 'https://stellarburgers.nomoreparties.site/login'
    driver.get(login_page)

    # Кликаем по надписи "Зарегистрироваться"
    driver.find_element(*Locators.inscription_login).click()

    # Генерация email и password
    generator = EmailPasswordGenerator()
    email, password = generator.generate()


    # Ищем поле "Имя" и заполни его
    driver.find_element(*Locators.field_name).send_keys("Игорь")

    # Ищем поле "email" и заполни его
    driver.find_element(*Locators.field_email).send_keys(email)

    # Ищем поле "Пароль" и заполни его
    driver.find_element(*Locators.field_password).send_keys(password)

    # Жмем на кнопку зарегаться
    driver.find_element(*Locators.button_login).click()

    # Ждем кнопку войти
    WebDriverWait(driver, 4).until(EC.visibility_of_element_located(Locators.button_entrance))

    return driver, email, password



def authorization_entrance(driver, email, password):
    driver.find_element(*Locators.field_email).send_keys(email)
    driver.find_element(*Locators.field_password).send_keys(password)
    driver.find_element(*Locators.button_entrance).click()


