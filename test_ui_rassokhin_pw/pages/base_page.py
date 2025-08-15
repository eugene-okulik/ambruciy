from playwright.sync_api import Page, Locator, TimeoutError
from test_ui_rassokhin_pw.pages.locators import base_locators as loc
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Открытие страницы')
    def open_page(self):
        if self.base_url:
            self.page.goto(f'{self.base_url}/{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    @allure.step('Принятие кук')
    def accept_cookie(self):
        try:
            self.page.locator(loc.COOKIE).click()
        except TimeoutError:
            print('Модалка с куками не появилась')
