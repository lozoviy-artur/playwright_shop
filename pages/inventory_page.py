from playwright.sync_api import Page
from pages.login_page import LoginPage


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

    def open_burger_menu(self):
        self.page.locator("#react-burger-menu-btn").click()

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