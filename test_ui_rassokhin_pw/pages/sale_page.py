from test_ui_rassokhin_pw.pages.base_page import BasePage
from test_ui_rassokhin_pw.pages.locators import sale_locators as loc
from playwright.sync_api import expect
import allure


class SalePage(BasePage):
    page_url = 'sale.html'

    @allure.label('owner', 'Андрей')
    @allure.story('Страница распродаж')
    @allure.step('Открытие страницы с мужской распродажей')
    def check_open_men_sale_page(self):
        self.find(loc.MEN_SALE).click()
        men_sale_header = self.find(loc.MEN_SALE_PAGE)
        expect(men_sale_header).to_have_text('Men Sale')

    @allure.label('owner', 'Андрей')
    @allure.story('Страница распродаж')
    @allure.step('Проверка, что заголовок страницы имеет тег h1')
    def header_page_have_tag_h1(self):
        # header = self.find('h1')
        # expect(header).to_have_text('Sale')
        header = self.find(loc.HEADER_PAGE)
        expect(header).to_have_js_property("tagName", "H1")

    @allure.label('owner', 'Андрей')
    @allure.story('Страница распродаж')
    @allure.step('Открытие страница с женской распродажей')
    def check_open_women_sale_page(self):
        self.find(loc.WOMEN_SALE).click()
        women_sale_header = self.find(loc.WOMEN_SALE_PAGE)
        expect(women_sale_header).to_have_text('Women Sale')
