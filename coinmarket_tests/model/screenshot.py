from datetime import datetime
from selene import browser
from coinmarket_tests.controls.utils import resource


def creating_and_saving_a_screenshot():
    current_datetime = datetime.now().strftime('%d.%m.%y_%H.%M')
    screenshot_filename = f'screenshot_{current_datetime}.png'

    browser.driver.save_screenshot(resource(screenshot_filename))
