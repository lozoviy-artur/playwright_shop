from pathlib import Path
import shutil

import pytest
from pages.login_page import LoginPage


def pytest_sessionstart(session):
    allure_dir = session.config.getoption("--alluredir")

    if allure_dir:
        report_path = Path(allure_dir)
        shutil.rmtree(report_path, ignore_errors=True)
        report_path.mkdir(parents=True, exist_ok=True)


@pytest.fixture
def logged_in_page(page):

    login_page = LoginPage(page)

    login_page.open()
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    return page
