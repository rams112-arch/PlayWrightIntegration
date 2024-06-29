import pytest
from playwright.sync_api import Page, expect
from models.LoginPage import LoginPage
from models.HomePage import HomePage
from models.ProductDetailPage import ProductDetailPage
    
def test_home_page(page: Page) -> None:
    loginPage = LoginPage(page)
    loginPage.navigate()
    loginPage.performLogin()
    
    homePage = HomePage(page)
    assert homePage.getTitle().is_visible(), "Assertion failed: <h1> element is not visible."
    
def test_navigation(page: Page) -> None:
    loginPage = LoginPage(page)
    loginPage.navigate()
    loginPage.performLogin()
    
    homePage = HomePage(page)
    title = homePage.getTitleText()

    homePage.navigateToDetail()
    
    productDetailPage = ProductDetailPage(page)
    assert title in productDetailPage.getProductTitle(), f"Error"
    
    