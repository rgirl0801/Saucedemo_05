import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import conf


@pytest.fixture(scope='class')
def browser(request):
    request.config.getoption("--browser")
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--window-size=1600,1080")
        # options.headless = True

        browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=options
        )
        print('\n*** start fixture = setup ***\n')
        browser.get(conf.URL)
        yield browser
        browser.quit()
        print('\n*** end fixture = teardown ***\n')
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1600,1080")
        options.headless = True
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )
        print('\n*** start fixture = setup ***\n')
        browser.get(conf.URL)
        yield browser
        browser.quit()
        print('\n*** end fixture = teardown ***\n')


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="firefox",
        help="define browser: chrome or firefox, --browser=chrome",
    )


def pytest_html_report_title(report):
    report.title = "REPORT"
