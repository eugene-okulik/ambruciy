from playwright.sync_api import Page, expect, BrowserContext


def test_part_1(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('//*[@class="a-button" and text()="Click"]').click()
    result = page.locator('#result')
    expect(result).to_contain_text('Ok')


def test_part_2(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    btn = page.locator('#new-page-button')
    with context.expect_page() as new_page:
        btn.click()
    page2 = new_page.value
    result = page2.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    expect(btn).to_be_enabled()


def test_part_3(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    btn = page.locator('#colorChange')
    expect(btn).to_have_css('color', 'rgb(220, 53, 69)')
    btn.click()
