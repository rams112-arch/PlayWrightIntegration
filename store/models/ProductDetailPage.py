from playwright.sync_api import Page, expect

class ProductDetailPage:
    def __init__(self, page):
        self.page = page
        self.product = page.locator('h1')
        self.add_to_cart_button = page.locator('text=Add to Cart')
        
    def navigate_to_detailpage(self):
        return self.product.inner_text()
    
    def get_product_title(self):
        return self.product.inner_text()
    
    def add_to_cart(self):
        return self.add_to_cart_button.click()