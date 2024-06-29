from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator('[placeholder=Username]')
        self.password_input = page.locator('[placeholder=Password]')
        self.login_button = page.locator('text=login')
        self.error_body = page.locator('body')

    def navigate(self):
        self.page.goto("http://localhost:8000")

    def perform_login(self):
        self.username_input.fill('testuser')
        self.password_input.fill('password123')
        self.login_button.click()
        
    def perform_login_wrong_password(self):
        self.username_input.fill('testuser1')
        self.password_input.fill('password1234')
        self.login_button.click()
             
    def get_errorbody(self):
        return self.error_body.inner_text() 