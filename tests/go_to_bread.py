from iniconf.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_check_chapter_bread(start_from_login_page):
    driver = start_from_login_page
    driver.maximize_window()

    # Нажали на раздел начинки "Соусы"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_sause)).click()

    # Проверяем наличие раздела
    new_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.inscription_bread))
    assert new_element.is_displayed()

    # Нажали на раздел "Хлеб"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread)).click()

    # Проверяем тап по разделу
    new_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.chapter))
    assert new_element.is_displayed()

    driver.quit()
