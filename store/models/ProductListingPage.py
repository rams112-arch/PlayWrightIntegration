from playwright.sync_api import Page

class ProductListingPage:
    def __init__(self, page):
        self.page = page
        self.page_title = page.locator('h1')
        self.product_name = page.locator('text=Product 1')
        self.cart = page.locator('text=View Cart')
        
    def get_page_title(self):
        return self.page_title
        
    def navigate_to_detail(self):
        return self.product_name.click()
        
    def get_product_name(self):
        return self.product_name.inner_text()
    
    def navigate_to_cart(self):
        return self.cart.click()  