from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from iniconf.locators import Locators
from iniconf.curl import *

def test_button_in_register(start_from_recovery_page):
    driver = start_from_recovery_page
    driver.maximize_window()

    # Жмем загрузки "булок"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.inscription_bread)))

    # Проверяем что мы на основной странице сайта
    assert driver.current_url == (main_page)

    driver.quit()
