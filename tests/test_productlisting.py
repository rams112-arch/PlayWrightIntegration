import pytest
from playwright.sync_api import Page
from store.models.LoginPage import LoginPage
from store.models.ProductListingPage import ProductListingPage

@pytest.fixture(scope="function", autouse=True)
def test_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.perform_login()
    
def test_productlisting_page(page: Page) -> None:
    home_page = ProductListingPage(page)
    assert home_page.get_page_title().is_visible(), "Assertion failed: <h1> element is not visible."
