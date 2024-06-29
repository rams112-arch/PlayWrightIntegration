import pytest
from playwright.sync_api import Page, expect
from models.LoginPage import LoginPage
from store.models.HomePage import HomePage
from store.models.ProductDetailPage import ProductDetailPage
from store.models.CartPage import CartPage
# import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def test_productlist_page(page: Page) -> None:
    loginPage = LoginPage(page)
    loginPage.navigate()
    loginPage.performLogin()
    
    homePage = HomePage(page)
    title = homePage.getTitleText()
    homePage.navigateToDetail()
    
    productDetailPage = ProductDetailPage(page)
    assert title in productDetailPage.getProductTitle(), f"Error"
    productDetailPage.addtoCart()

    
def test_addtocart(page:Page) -> None:
        
    loginPage = LoginPage(page)
    loginPage.navigate()
    loginPage.performLogin()
    
    homePage = HomePage(page)
    homePage.navigateToDetail()
    productDetailPage = ProductDetailPage(page)
    productTitle = productDetailPage.getProductTitle()
    
    # add the product to cart
    productDetailPage.addtoCart()
    
    homePage.navigatetocart()  
    
    cartPage = CartPage(page)
    product_info = cartPage.cartproducts()
    product = product_info.split('-')
    quantity = product[2].split(':')

    assert productTitle in product[0], f"Unexpected text '{productTitle}'"
    assert '1' in quantity[1], f"Unexpected text '{quantity[1]}'"
    
    cartPage.backtoproduct_listingpage()   
    homePage.navigateToDetail()
    productDetailPage = ProductDetailPage(page)
    productTitle = productDetailPage.getProductTitle()
    # add the product to cart
    productDetailPage.addtoCart()
    homePage.navigatetocart()     
    cartPage = CartPage(page)
    product_info = cartPage.cartproducts()
    product = product_info.split('-')
    quantity = product[2].split(':')
    assert productTitle in product[0], f"Unexpected text '{productTitle}'"
    assert '2' in quantity[1], f"Unexpected text '{quantity[1]}'"