from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page):
        self.page = page
        self.li_element = page.locator('li')
        self.backtoProduct_listing = page.locator('text=Back to Product Listing')    
                
    def check_cart_products(self):
        return self.li_element.text_content()

    def navigate_to_product_listing(self):
        return self.backtoProduct_listing.click()