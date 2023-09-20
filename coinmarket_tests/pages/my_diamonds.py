from selene import browser, have
from coinmarket_tests.helpers.locator import *
import time


def going_to_my_diamonds_page():
    browser.element(diamond_locator).click()


def collecting_a_daily_bonus():
    browser.driver.refresh()

    browser.element(collect_diamond_locator).click()

    browser.element(collect_diamond_locator).with_(timeout=10).should(have.text('to collect'))

