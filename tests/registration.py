from iniconf.curl import *
from iniconf.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration(resister_new_account):
    driver, email, password = resister_new_account
    driver.maximize_window()

    # Ищем поле "email" и заполни его
    driver.find_element(*Locators.field_email).send_keys(email)

    # Ищем поле "Пароль" и заполни его
    driver.find_element(*Locators.field_password).send_keys(password)

    # Находим надпись "войти" и жмем
    driver.find_element(*Locators.button_entrance).click()

    # Ждем перехода на главную страницу
    WebDriverWait(driver, 10).until(EC.url_to_be(main_page))

    # Проверяем что мы авторизовались созданным аккаунтом перейдя на главную страницу
    assert driver.current_url == (main_page)

    driver.quit()



