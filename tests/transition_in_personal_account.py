from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iniconf.curl import *
from iniconf.locators import Locators

def test_transition_by_logo(start_from_login_page):
    driver = start_from_login_page
    driver.maximize_window()

    # Ждем загрузки "булок"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))

    # Кликаем по кнопке "личный кабинет"
    driver.find_element(*Locators.button_personal_area).click()

    # Ждем перехода на страницу профиля
    WebDriverWait(driver, 10).until(EC.url_to_be(profile_page))

    # Проверяем что мы на странице профиля
    assert driver.current_url == (profile_page)

    driver.quit()
