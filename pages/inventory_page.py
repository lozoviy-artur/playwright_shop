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

    def sort_by(self, sort_option):
        self.page.locator(".product_sort_container").select_option(sort_option)

    def remove_from_cart(self, item_name):
        item_locator = self.page.locator(f".inventory_item:has-text('{item_name}')")
        remove_button = item_locator.locator("button:has-text('Remove')")
        remove_button.click()

    @property
    def first_product_name(self):
        return self.page.locator(".inventory_item_name").first

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
    
    @property
    def sauce_labs_backpack(self):
        return self.page.locator('[data-test*="backpack-img"]')
    
    @property
    def item_names(self):
        return self.page.locator(".inventory_item_name")
    
    @property
    def item_prices(self):
        return self.page.locator(".inventory_item_price")