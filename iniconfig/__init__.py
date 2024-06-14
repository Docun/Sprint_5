from selenium.webdriver.common.by import By

def authorization(driver, email='igor008@yandex.ru', password='123456789'):

    #Ищем поле email и пишем мыло пользователя
    email_field = driver.find_element(By.XPATH, ".//input[@type='text']")
    email_field.send_keys(email)

    # Ищем поле пароль и пишем пароль пользователя
    password_field = driver.find_element(By.XPATH, ".//input[@type='password']")
    password_field.send_keys(password)
    # Кликаем на кнопку войти
    tap_button = driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    tap_button.click()

    return driver

def authorization_two(driver, email='igor008@yandex.ru', password='123456789'):

    #Ищем поле email и пишем мыло пользователя
    email_field = driver.find_element(By.XPATH, "//div[label[contains(text(),'Email')]]//input")
    email_field.send_keys(email)

    # Ищем поле пароль и пишем пароль пользователя
    password_field = driver.find_element(By.XPATH, "//div[label[contains(text(),'Пароль')]]//input")
    password_field.send_keys(password)

    return driver
