import pytest
from tests.conftest import opened_page_website
from coinmarket_tests.model.authorization import *
from coinmarket_tests.model.screenshot import creating_and_saving_a_screenshot
from coinmarket_tests.pages.my_diamonds import *


@pytest.mark.parametrize("user", [user_1, user_2, user_3])
def test_receiving_a_daily_bonus(user, setup_browser):
    opened_page_website()

    authorization_on_the_site(user)

    display_push_notification_about_authorization()

    going_to_my_diamonds_page()

    collecting_a_daily_bonus()

    creating_and_saving_a_screenshot(user)
