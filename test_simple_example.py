import re
from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("@login_logo", has_text="Swag Labs")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.click("#login-button")
    expect(page).to_have_title("Swag Labs")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_burger_menu(page: Page):
    test_login(page)
    page.locator("a.shopping_cart_link").is_visible()
    page.click("#react-burger-menu-btn")
    expect(page.locator("#inventory_sidebar_link")).to_be_visible()
    expect(page.locator("#about_sidebar_link")).to_be_visible()
    expect(page.locator("#logout_sidebar_link")).to_be_visible()
    expect(page.locator("#reset_sidebar_link")).to_be_visible()


def test_select_item(page: Page):
    test_login(page)
    page.click(".inventory_item_name:has-text('Sauce Labs Onesie')")
    expect(page.locator(".inventory_details_desc")).to_have_text(
        "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, "
        "two-needle hemmed sleeved and bottom won't unravel. "
    )