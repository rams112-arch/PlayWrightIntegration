import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
from models.LoginPage import LoginPage
from models.HomePage import HomePage
import os

def test_login_success(page: Page) -> None:
    loginPage = LoginPage(page)
    loginPage.navigate()
    loginPage.performLogin()
    
    body_text = loginPage.getErrorBody()
    unexpected_text = "Invalid credentials. Please try again."
    assert unexpected_text not in body_text, f"Unexpected text '{unexpected_text}' found in body text:\n{body_text}"
    
    page.close()

def test_login_error(page: Page) -> None:
    loginPage = LoginPage(page)
    loginPage.navigate()
    loginPage.performLogin_wrongPassword()
    body_text = loginPage.getErrorBody()
    
    expected_text = "Invalid credentials. Please try again."
    assert expected_text in body_text, f"Expected text '{expected_text}' not found in body text:\n{body_text}"
    
    page.close()
