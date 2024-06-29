import pytest
from playwright.sync_api import Page
from store.models.LoginPage import LoginPage
from store.models.ProductListingPage import ProductListingPage
from store.models.ProductDetailPage import ProductDetailPage

@pytest.fixture(scope="function", autouse=True)
def test_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.perform_login()

def test_product_navigation(page: Page) -> None:
    home_page = ProductListingPage(page)
    title = home_page.get_product_name()
    home_page.navigate_to_detail()
    
    product_detail_page = ProductDetailPage(page)
    assert title in product_detail_page.get_product_title(), f"Error"  