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


def test_checkout_with_single_item(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()
    expect(inventory_page.checkout_button).to_be_visible()


def test_checkout_flow(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()
    inventory_page.checkout()
    
    # Fill checkout info
    inventory_page.fill_checkout_info("John", "Doe", "12345")
    inventory_page.continue_button.click()
    
    # Verify checkout continues
    expect(inventory_page.finish_button).to_be_visible()


def test_complete_checkout(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()
    inventory_page.checkout()
    
    inventory_page.fill_checkout_info("John", "Doe", "12345")
    inventory_page.continue_button.click()
    inventory_page.finish_checkout()
    
    # Verify order complete page
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/checkout-complete.html")