# conftest.py
import pytest
import os

from slugify import slugify

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        if report.failed and "page" in item.funcargs:
            page = item.funcargs["page"]
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            page.screenshot(path=f"screenshots/{item.name}+{slugify(item.nodeid)}.png")
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # add the screenshots to the html report
            extra.append(pytest_html.extras.png(screen_file))
        report.extra = extra