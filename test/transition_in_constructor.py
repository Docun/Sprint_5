from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iniconf.locators import Locators
from iniconf.curl import *

def test_check(start_from_main_page):
    driver = start_from_main_page
    driver.maximize_window()

    # Ждем перехода на главную страницу
    WebDriverWait(driver, 10).until(EC.url_to_be(main_page))

    # Кликаем по кнопке "личный кабинет"
    driver.find_element(*Locators.button_personal_area).click()

    # Ждем загрузки надписи "конструктор"
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_constaction))

    # Кликаем по кнопке "конструктор"
    driver.find_element(*Locators.button_constaction).click()

    # Ждем перехода на главную страницу
    WebDriverWait(driver, 10).until(EC.url_to_be(main_page))

    # Проверяем что мы на основной странице
    assert driver.current_url == (main_page)

    driver.quit()

