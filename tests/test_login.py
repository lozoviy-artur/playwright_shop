from playwright.sync_api import Page, expect
import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),      
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
])
def test_login_with_various_users(page, username, password):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)

    if username == "locked_out_user":
        expect(login_page.error_message).to_be_visible()
    else:
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        
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





