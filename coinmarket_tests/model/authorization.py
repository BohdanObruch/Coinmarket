from selene import browser, be, have
import time
from tests.conftest import dotenv
from coinmarket_tests.helpers.locator import *

user_email = dotenv.get('USER_Email')
user_pass = dotenv.get('USER_Password')
base_url = dotenv.get('BASE_URL')

user = {
    "Email": user_email,
    "Password": user_pass}


def authorization_on_the_site():
    browser.element(login_button_locator).click()

    browser.element(email_locator).type(user['Email'])
    password = browser.element(password_locator).type(user['Password'])
    time.sleep(2)
    password.press_enter()


def display_push_notification_about_authorization():
    browser.element(pop_up_locator).should(have.text('You have successfully logged in!'))
