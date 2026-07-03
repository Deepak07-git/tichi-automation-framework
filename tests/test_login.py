from config.config import BASE_URL, EMAIL, PASSWORD
from pages.login_page import LoginPage
from utils.wait_utils import WaitUtils


def test_valid_login(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.login(EMAIL, PASSWORD)

    WaitUtils.wait_for_url(driver, "/home")

    assert "/home" in driver.current_url,"Valid login failed."

def test_invalid_password(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.enter_email(EMAIL)
    login.click_continue()

    login.enter_password("WrongPassword123")
    login.click_login()

    # Should NOT go to home page
    assert "/home" not in driver.current_url,"User logged in with  an invalid password.7"

def test_invalid_password(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.enter_email(EMAIL)
    login.click_continue()

    login.enter_password("WrongPass@123")
    login.click_login()

    assert "/home" not in driver.current_url

def test_empty_email(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.enter_email("")
    login.click_continue()

    assert "/login" in driver.current_url


def test_invalid_email_format(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.enter_email("deepakgmail.com")
    login.click_continue()

    assert "/login" in driver.current_url, "Invalid email format was accepted."

def test_unregistered_email(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.enter_email("abcxyz123456@gmail.com")
    login.click_continue()

    # Expected: Stay on login page or show an error
    assert "/login" in driver.current_url, "Unregistered email was accepted."
def test_empty_email_and_password(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.enter_email("")
    login.click_continue()

    assert "/login" in driver.current_url, "Empty email should not proceed."