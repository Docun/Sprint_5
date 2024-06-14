from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from iniconfig import authorization
from iniconfig.curl import *
from iniconfig.locators import Locators

driver = webdriver.Chrome()
driver.maximize_window()


# Находимся на странице логина
driver.get(login_page)

# Проходим авторизацию
driver = authorization(driver)

# Ждем загрузки "оформить заказ"
WebDriverWait(driver, 9).until(expected_conditions.visibility_of_element_located(Locators.button_arrange_order))

# Кликаем по надписи "Соусы"
driver.find_element(*Locators.inscription_sause).click()


# Ждем обновления кнопки "Булки"
WebDriverWait(driver, 9).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")))

# Кликаем надписи "Булки"
driver.find_element(*Locators.inscription_bread).click()


# Ждем обновления кнопки "Булки"
WebDriverWait(driver, 9).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")))



driver.quit()