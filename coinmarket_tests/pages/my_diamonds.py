from selene import browser, be
from coinmarket_tests.helpers.locator import *
import time


def going_to_my_diamonds_page():
    browser.element(diamond_locator).click()


def collecting_a_daily_bonus():
    browser.driver.refresh()
    browser.element(collect_diamond_locator).click()
    time.sleep(2)


def check_that_the_bonus_was_received():
    browser.element(pop_up_diamond).should(be.visible)
    browser.element(ok_button_locator).click()
