from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Знаходимо поле, в яке будемо вводити неправільне ім'я користувача або поштову адресу
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Вводимо неправільне ім'я користувача або поштову адресу
        login_elem.send_keys(username)

        # Знаходимо поле, в яке будемо вводити неправільний пароль
        pass_elem = self.driver.find_element(By.ID, "password")

        # Вводимо неправільний пароль
        pass_elem.send_keys(password)

        # Знаходимо кнопку sign in
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

