from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from iniconf.curl import *
from iniconf.locators import Locators

def test_button_litle_entrance(start_from_recovery_page):
    driver = start_from_recovery_page
    driver.maximize_window()

    # Ждем загрузку "булок"
    WebDriverWait(driver, 9).until(expected_conditions.visibility_of_element_located((Locators.inscription_bread)))

    # Проверяем что мы на основной странице сайта
    assert driver.current_url == (main_page)

    driver.quit()



