import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# Використовується щоб додати затримку для перевірки результатів
# import time


@pytest.mark.ui 
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    #Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо неправільне ім'я користувача або поштову адресу
    login_elem.send_keys("tamarazhuk@mistakenemail.com")

    # Знаходимо поле, в яке будемо вводити неправільний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо неправільний пароль
    pass_elem.send_keys("wrong password")

    # Знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()

    # Перевіряємо, що назва сторінки така, як ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"
    # Затримка для перевірки
    # time.sleep(3)


    # Закриваємо браузер
    driver.close()

