from playwright.sync_api import Page
from store.models.LoginPage import LoginPage
    
def test_login_success(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.perform_login()
    
    body_text = login_page.get_errorbody()
    unexpected_text = "Invalid credentials. Please try again."
    assert unexpected_text not in body_text, f"Unexpected text '{unexpected_text}' found in body text:\n{body_text}"
    
    page.close()

def test_login_error(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.perform_login_wrong_password()
    
    body_text = login_page.get_errorbody()
    expected_text = "Invalid credentials. Please try again."
    assert expected_text not in body_text, f"Expected text '{expected_text}' not found in body text:\n{body_text}"
    
    page.close()
