from selene import browser
from coinmarket_tests.helpers.locator import diamond_locator, collect_diamond_locator
import time


def going_to_my_diamonds_page():
    browser.element(diamond_locator).click()


def collecting_a_daily_bonus():
    browser.driver.refresh()
    browser.element(collect_diamond_locator).click()
    time.sleep(2)
