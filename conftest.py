import pytest
import allure
import os

from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--base-url")
    headless = request.config.getoption("--headless")
    app = Application(headless, url)
    yield app
    app.browser_close()


@pytest.fixture()
def login(request, app):
    login = request.config.getoption("--username")
    passwd = request.config.getoption("--password")
    app.open_main_page()
    if app.left_menu.logout_button() != []:
        app.left_menu.click_logout()
    app.login.do_login(login, passwd)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Отчёт со скриншотами"""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        try:
            with open("failures", mode):
                if "app" in item.fixturenames:
                    web_driver = item.funcargs["app"]
                else:
                    print("Fail to take screen-shot")
                    return
            allure.attach(
                web_driver.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print("Fail to take screen-shot: {}".format(e))


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://www.saucedemo.com/",
        help="enter base_url",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default=True,
        help="launching browser without gui",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="standard_user",
        help="user login",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="secret_sauce",
        help="user password",
    )
