from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iniconf.curl import *
from iniconf.locators import Locators

def test_transition_by_logo(start_from_login_page):
    driver = start_from_login_page
    driver.maximize_window()

    # Кликаем по кнопке "личный кабинет"
    driver.find_element(*Locators.button_personal_area).click()

    # Ждем загрузки надписи "профиль"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_profile))

    # Кликаем по кнопке "конструктор"
    driver.find_element(*Locators.logo).click()

    # Ждем перехода на главную страницу
    WebDriverWait(driver, 10).until(EC.url_to_be(main_page))

    # Проверяем что мы на основной странице
    assert driver.current_url == (main_page)

    driver.quit()


