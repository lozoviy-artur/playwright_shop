from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login_successful(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


def test_wrong_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "wrong_password")
    expect(login_page.error_message).to_be_visible()


def test_wrong_username(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("not_existed_user", "secret_sauce")
    expect(login_page.error_message).to_be_visible()





