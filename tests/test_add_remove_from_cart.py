from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from  pages.login_page import LoginPage



def test_add_single_item_to_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")


def test_remove_single_item_from_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.remove_from_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).not_to_be_visible()