import pytest
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
