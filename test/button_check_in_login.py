from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from iniconf.locators import Locators

def test_check_button(start_from_login_page):
    driver = start_from_login_page
    driver.maximize_window()

    # Проверка загрузки "булки"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))

    # Проверка текущего URL
    main_page = 'https://stellarburgers.nomoreparties.site/'
    assert driver.current_url == main_page

    driver.quit()

