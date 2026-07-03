from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = (By.ID, "email")

    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and contains(.,'Continue')]"
    )

    PASSWORD = (By.ID, "password")

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and contains(.,'Login')]"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        self.enter_text(self.EMAIL, email)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.click_continue()
        self.enter_password(password)
        self.click_login()