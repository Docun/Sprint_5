На что написал тесты 

Регистрация - данные тесты лежат в test_registration
- Успешная регистрация (test_registration)
- Поле «Имя» должно быть не пустым (test_registration_no_name)
- попытка зарегать существующий аккаунт (test_existing_acount)
- Минимальный пароль — шесть символов (test_error_password)
- Проверка регистрации при отсутствии пароля (test_no_password)



Вход - данные тесты лежат в test_check_entrance
- вход по кнопке «Войти в аккаунт» на главной (test_check_entrance_by_big_button)
- вход через кнопку «Личный кабинет» (test_check_login_cabinet)
- вход через кнопку в форме регистрации (test_button_inscription_login)
- вход через кнопку в форме восстановления пароля (test_login_password_recovery)
- выход по кнопке «Выйти» в личном кабинете (test_check_loging_out)




Переход в личный кабинет - данные тесты лежат в test_move_to_personal_acc
- переход из личного кабинета в конструктор (test_check_transition_by_constructor)
- переход по клику на логотип Stellar Burgers (test_transition_by_logo)
- переход по клику на «Личный кабинет».(test_transition_before_profile)


Раздел «Конструктор» - test_move_to_desing
- проверил что работают переходы к разделам:
«Булки», (test_check_chapter_bread)
«Соусы», (test_check_chapter_sauce)
«Начинки». (test_check_chapter_fillings)