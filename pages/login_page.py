from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        self.page.locator("#user-name").fill(username)
        self.page.locator("#password").fill(password)
        self.page.locator("#login-button").click()

        from pages.inventory_page import InventoryPage
        return InventoryPage(self.page)

    @property
    def error_message(self):
        return self.page.locator("[data-test='error']")

    @property
    def login_button(self):
        return self.page.locator("#login-button")
