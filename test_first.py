from playwright.sync_api import Playwright, sync_playwright


def test_shop(page) -> None:
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://ecommerce-playground.lambdatest.io/")
    page.locator("#entry_217822 div").filter(
        has_text="All Categories All Categories Desktops Laptops Components Tablets Software Phone").nth(3).click()
    page.get_by_role("textbox", name="Search For Products").fill("iphone ")
    page.get_by_role("button", name="Search").click()

    # ---------------------
    # context.close()
    # browser.close()


# with sync_playwright() as playwright:
#     test_dzen(playwright)
