import pytest
from playwright.sync_api import Page, expect
from store.models.LoginPage import LoginPage
from store.models.ProductListingPage import ProductListingPage
from store.models.ProductDetailPage import ProductDetailPage
from store.models.CartPage import CartPage

@pytest.fixture(scope="function", autouse=True)
def test_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.perform_login()
    
def test_add_to_cart_navigation(page: Page) -> None:
    home_page = ProductListingPage(page)
    home_page.navigate_to_detail()
    
    product_detail_page = ProductDetailPage(page)
    product_detail_page.add_to_cart()
    
    home_page = ProductListingPage(page)
    home_page.get_page_title
    
    assert home_page.get_page_title().is_visible(), "Assertion failed: <h1> element is not visible."

def test_cart_product_validation(page:Page) -> None:
    home_page = ProductListingPage(page)
    home_page.navigate_to_detail()
    product_detail_page = ProductDetailPage(page)
    product_title = product_detail_page.get_product_title()
    
    product_detail_page.add_to_cart()
    home_page.navigate_to_cart()  
    
    cart_page = CartPage(page)
    product_info = cart_page.check_cart_products()
    product = product_info.split('-')
    quantity = product[2].split(':')

    assert product_title in product[0], f"Unexpected text '{product_title}'"
    assert '1' in quantity[1], f"Unexpected text '{quantity[1]}'"
    
    cart_page.navigate_to_product_listing()   
    home_page.navigate_to_detail()
    product_detail_page = ProductDetailPage(page)
    product_title = product_detail_page.get_product_title()

    product_detail_page.add_to_cart()
    home_page.navigate_to_cart()     
    cart_page = CartPage(page)
    product_info = cart_page.check_cart_products()
    product = product_info.split('-')
    quantity = product[2].split(':')
    
    assert product_title in product[0], f"Unexpected text '{product_title}'"
    assert '2' in quantity[1], f"Unexpected text '{quantity[1]}'"