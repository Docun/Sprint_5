from selenium.webdriver.common.by import By
class Locators:

    # Кнопка "Войти в аккаунт" на главной странице
    entrance_on_the_main = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Основное лого
    logo = (By.XPATH, '//*[@id="root"]/div/header/nav/div')

    # Надпись "выход"
    button_exit = (By.XPATH, ".//button[contains(text(),'Выход')]")

    # Надписи "профиль"
    inscription_profile = (By.XPATH, './/a[@href="/account/profile"]')

    # надписи "булки"
    inscription_bread = (By.XPATH, ".//span[contains(text(),'Булки')]")

    # кнопка_надпись "личный кабинет"
    button_personal_area = (By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")

    # Надпись "Соусы"
    inscription_sause = (By.XPATH, ".//span[contains(text(),'Соусы')]")

    # Надпись "Зарегаться"
    inscription_login = (By.CLASS_NAME, "Auth_link__1fOlj")

    # Раздел "Начинки"
    inscription_fillings = (By.XPATH, ".//span[contains(text(),'Начинки')]")

    # Активный раздел с начинками
    active_section = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]')

    # Надпись "Такой пользователь уже существует"
    inscription_error_account = (By.XPATH, ".//p[contains(text(),'Такой пользователь уже существует')]")

    # Надпись "Некорректный пароль"
    inscription_error_password = (By.XPATH, '//div[contains(@class, "input_status_error")]')

    # Кнопка "востановить пароль"
    button_restore_password = (By.XPATH, './/a[@href="/forgot-password"]')

    # Кнопка_надпись "войти"
    inscription_button_entrance = (By.XPATH, './/a[@href="/login"]')

    #Кнопка войти
    button_entrance = (By.XPATH, ".//button[contains(text(),'Войти')]")

    #Кнопка "Оформить заказ"
    button_arrange_order = (By.XPATH, ".//button[contains(text(),'Оформить заказ')]")

    #Кнопка Зарегаться
    button_login = (By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]")

    #кнопка конструктор
    button_constaction = (By.XPATH, ".//a[@href='/']")

    #поле "Имя"
    field_name = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input")

    # поле "email"
    field_email = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")

    # поле "password"
    field_password = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input")