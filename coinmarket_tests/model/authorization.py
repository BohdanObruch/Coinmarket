import pytest
from selene import browser, have
import time
from tests.conftest import dotenv
from coinmarket_tests.helpers.locator import *


user_1_email = dotenv.get('USER_1_Email')
user_1_pass = dotenv.get('USER_1_Password')
user_2_email = dotenv.get('USER_2_Email')
user_2_pass = dotenv.get('USER_2_Password')
user_3_email = dotenv.get('USER_3_Email')
user_3_pass = dotenv.get('USER_3_Password')
base_url = dotenv.get('BASE_URL')

user_1 = {
    "Email": user_1_email,
    "Password": user_1_pass}
#
user_2 = {
    "Email": user_2_email,
    "Password": user_2_pass}

user_3 = {
    "Email": user_3_email,
    "Password": user_3_pass}


@pytest.mark.parametrize("user", [user_1, user_2, user_3])
def authorization_on_the_site(user):
    browser.element(login_button_locator).click()

    browser.element(email_locator).type(user['Email'])
    password = browser.element(password_locator).type(user['Password'])
    time.sleep(1)
    password.press_enter()


def display_push_notification_about_authorization():
    browser.element(pop_up_locator).should(have.text('You have successfully logged in!'))
