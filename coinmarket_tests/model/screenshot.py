from datetime import datetime

import pytest
from selene import browser
from coinmarket_tests.controls.utils import resource
from coinmarket_tests.model.authorization import *


@pytest.mark.parametrize("user", [user_1, user_2, user_3])
def creating_and_saving_a_screenshot(user):
    current_datetime = datetime.now().strftime('%d.%m.%y_%H.%M')
    user_name = user["Email"].split("@")[0]
    screenshot_filename = f'screenshot_{user_name}_{current_datetime}.png'

    browser.driver.save_screenshot(resource(screenshot_filename))
