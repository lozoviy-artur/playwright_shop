from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from  pages.login_page import LoginPage
import time


def test_a_to_z_sorting(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_by("Name (A to Z)")

    item_names = inventory_page.item_names.all_text_contents()
    sorted_item_names = sorted(item_names)

    assert item_names == sorted_item_names, "Items are not sorted from A to Z"

def test_z_to_a_sorting(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_by("Name (Z to A)")
    
    item_names = inventory_page.item_names.all_text_contents()
    sorted_item_names = sorted(item_names, reverse=True)
    

    assert item_names == sorted_item_names, "Items are not sorted from Z to A"