from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from iniconf.curl import *
from iniconf.locators import Locators


def test_check_personal_account(start_from_main_page):
    driver = start_from_main_page
    driver.maximize_window()

    # Ждем кнопку "булки"
    WebDriverWait(driver, 9).until(expected_conditions.visibility_of_element_located((Locators.inscription_bread)))

    # Проверяем что мы на основной странице сайта
    assert driver.current_url == (main_page)

    driver.quit()
