from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from iniconf.locators import Locators

def test_existing_acount(start_from_main_not_login):
    driver = start_from_main_not_login
    driver.maximize_window()

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
    assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.inscription_error_account))

    driver.quit()