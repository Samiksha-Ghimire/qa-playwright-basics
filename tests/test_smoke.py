from playwright.sync_api import sync_playwright

def test_homepage_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        assert "Swag Labs" in page.title()
        context.close()
        browser.close()

def test_login_positive():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        title_text = page.locator(".title").inner_text()
        assert title_text == "Products"
        context.close()
        browser.close()

def test_login_negative_locked_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "locked_out_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        error_text = page.locator("[data-test='error']").inner_text()
        assert "locked out" in error_text.lower()
        context.close()
        browser.close()
