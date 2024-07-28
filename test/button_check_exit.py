from selenium.webdriver.support import expected_conditions as EC
from iniconf.locators import Locators
from iniconf.curl import *
from selenium.webdriver.support.wait import WebDriverWait

def test_check_exit_button(start_from_login_page):
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
    WebDriverWait(driver, 10).until(EC.url_to_be(login_page))

    # Проверяем URL адрес страницы логина
    assert driver.current_url == login_page

    driver.quit()