import pytest

class Login:
    pass

@pytest.fixture
def login():
    login = Login(email='igor008@yandex.ru', password="123456789")
    return login



pytest.main()




