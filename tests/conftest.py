import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import conf
from pathlib import Path

driver = None
directory = 'report/assets/'


@pytest.fixture(scope='class')
def d(browser):
    global driver
    Path(directory).mkdir(parents=True, exist_ok=True)
    if browser == 'chrome':
        o = webdriver.ChromeOptions()
        o.headless = conf.BROWSER_HEADLESS
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=o
        )
    else:
        o = webdriver.FirefoxOptions()
        o.headless = conf.BROWSER_HEADLESS
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


@pytest.fixture(scope='class')
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='class', autouse=True)
def g(d):
    print('\n*** start fixture = setup ***\n')
    d.get(conf.URL)
    yield d
    d.quit()
    print('\n*** end fixture = teardown ***\n')


def pytest_html_report_title(report):
    report.title = "REPORT"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url(driver.current_url))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.split('::')[-1] + ".png"
            file_name_ = "." + directory + file_name
            file_name_html = 'assets/' + file_name
            driver.get_screenshot_as_file(file_name_)
            if file_name_:
                html = f"<div><img src='{file_name_html}' alt='screenshot'"
                html += "onclick='window.open(this.src)' style='width:400px;'"
                html += " align='right'/></div>"
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
