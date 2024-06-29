import pytest
import os
from playwright.sync_api import sync_playwright

# Fixture for setting up Playwright
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

# Fixture for launching the browser
@pytest.fixture(scope="session", params=["chromium", "firefox", "webkit"])
def browser(playwright_instance, request):
    if request.param == "chromium":
        browser = playwright_instance.chromium.launch(headless=True)
    elif request.param == "firefox":
        browser = playwright_instance.firefox.launch(headless=True)
    elif request.param == "webkit":
        browser = playwright_instance.webkit.launch(headless=True)
    else:
        raise ValueError(f"Unsupported browser: {request.param}")
    
    yield browser
    
    browser.close()

# Fixture for creating a new browser context for each test
@pytest.fixture(scope="function")
def context(browser):
    # Create a new context within the current browser instance
    context = browser.new_context()
    yield context
    context.close()

# Fixture for creating a new page for each test
@pytest.fixture(scope="function")
def page(context):
    # Create a new page within the current context
    page = context.new_page()
    yield page
    page.close()

# pytest hook to capture screenshots on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Get the browser and page objects from the fixture scope
        # Since the 'page' fixture is scoped 'function', it's not directly accessible here
        # Instead, we should fetch it from the fixturemanager using a more direct approach
        page = None
        for fixture_name in item.fixturenames:
            if fixture_name == 'page':
                page = item._request.getfixturevalue(fixture_name)
                break

        if page:
            # Capture screenshot
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = f"{screenshot_dir}/failed-{item.nodeid}.png"
            page.screenshot(path=screenshot_path)

            # Optionally, log the screenshot path or further actions
            print(f"\nScreenshot captured for {item.nodeid}: {screenshot_path}\n")
        else:
            print(f"\nUnable to capture screenshot for {item.nodeid}: 'page' fixture not found\n")
