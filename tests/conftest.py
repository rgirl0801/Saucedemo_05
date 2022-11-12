import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = None


@pytest.fixture(scope='session')
def b(browser):
    global driver
    if driver is not None:
        return driver
    if browser == 'chrome':
        o = webdriver.ChromeOptions()
        o.headless = True
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=o
        )
    else:
        o = webdriver.FirefoxOptions()
        o.headless = True
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=o
        )
    return driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="firefox",
        help="define browser: chrome or firefox, --browser=chrome",
    )


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(autouse=True)
def g(b):
    print('\n*** start fixture = setup ***\n')
    driver.get('https://www.saucedemo.com/')
    yield b
    driver.quit()
    print('\n*** end fixture = teardown ***\n')


def pytest_html_report_title(report):
    report.title = "Kate Fox"
