from modules.ui.page_object.sign_in_page import SignInPage
import pytest
# Використовується щоб додати затримку для перевірки результатів
import time


@pytest.mark.ui 
def test_check_incorrect_username():
    # Створення об'єкту сторінки
    sign_in_page = SignInPage()

    # відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()
    
    # Виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Перевіряємо, що назва сторінки така, яку ми очикуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    # Затримка для перевірки
    #time.sleep(5)


    # Закриваємо браузер
    sign_in_page.close()

