from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from  pages.login_page import LoginPage



def test_burger_menu_visibility(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.open_burger_menu()
    expect(inventory_page.about).to_be_visible()

    expect(inventory_page.all_items).to_be_visible()
    expect(inventory_page.about).to_be_visible()
    expect(inventory_page.logout).to_be_visible()
    expect(inventory_page.reset).to_be_visible()

def test_loguout(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.open_burger_menu()
    inventory_page.logout.click()

    login_page = LoginPage(logged_in_page)
    expect(login_page.login_button).to_be_visible()

def test_reset_app_state(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_burger_menu()
    inventory_page.reset.click()

    expect(inventory_page.cart_badge).not_to_be_visible()



