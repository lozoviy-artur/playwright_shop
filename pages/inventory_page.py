from playwright.sync_api import Page
from pages.login_page import LoginPage


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

    def open_burger_menu(self):
        self.page.locator("#react-burger-menu-btn").click()
 
    def add_to_cart(self, item_name):
        item_locator = self.page.locator(f".inventory_item:has-text('{item_name}')")
        add_to_cart_button = item_locator.locator("button")
        add_to_cart_button.click()

    @property
    def all_items(self):
        return self.page.locator("#inventory_sidebar_link")

    @property
    def about(self):
        return self.page.locator("#about_sidebar_link")

    @property
    def logout(self):
        return self.page.locator("#logout_sidebar_link")

    @property
    def reset(self):
        return self.page.locator("#reset_sidebar_link")
    
    @property
    def cart_badge(self):
        return self.page.locator(".shopping_cart_badge")