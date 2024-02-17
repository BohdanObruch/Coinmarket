import os
import pytest

from selene import browser
from selenium import webdriver as webdriver_selenium
from selenium.webdriver.chrome.options import Options
from dotenv import dotenv_values, load_dotenv
from coinmarket_tests.controls import attach


@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()


dotenv = dotenv_values()

web_url = dotenv.get('BASE_URL')


def opened_page_website():
    browser.open(web_url)


DEFAULT_BROWSER_VERSION = "118.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='118.0'
    )
    parser.addoption(
        '--headless',
        default='False'
    )


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    headless = request.config.getoption('--headless')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-setuid-sandbox')
    options.page_load_strategy = 'eager'
    if headless == 'True':
        options.add_argument(f'--browser_version={browser_version}')
        options.add_argument('--headless')
        browser.config.driver_options = options
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        yield browser
        browser.quit()

    else:
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)

        url = os.getenv('URL')

        driver = webdriver_selenium.Remote(
            command_executor=f"{url}/wd/hub",
            options=options
        )
        browser.config.driver = driver
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        yield browser

        attach.add_html(browser)
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_video(browser)
        browser.quit()
