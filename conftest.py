import pytest
from playwright.sync_api import sync_playwright

# Fixture for setting up Playwright
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

# Fixture for launching the browser
@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()

# Fixture for creating a new browser context for each test
@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

# Fixture for creating a new page for each test
@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()