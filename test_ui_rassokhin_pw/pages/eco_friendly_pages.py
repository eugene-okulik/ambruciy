from time import sleep

from test_ui_rassokhin_pw.pages.base_page import BasePage
from test_ui_rassokhin_pw.pages.locators import eco_friendly_locators as loc
from playwright.sync_api import expect
import allure


class EcoFriendly(BasePage):
    page_url = 'collections/eco-friendly.html'

    @allure.label('owner', 'Андрей')
    @allure.story('Страница товаров')
    @allure.step('Проверка на количество отображаемых товаров на странице')
    def check_number_of_products_on_a_page(self):
        products_in_the_title = self.find(loc.ELEMENTS_ON_TITLE).first.inner_text()
        counting_products = self.find(loc.ALL_ELEMENTS)
        expect(counting_products).to_have_count(int(products_in_the_title))

    @allure.label('owner', 'Андрей')
    @allure.story('Страница товаров')
    @allure.step('Открытие карточки товара')
    def open_card_product(self):
        product_name = self.find(loc.PRODUCT).inner_text()
        self.find(loc.PRODUCT).click()
        return product_name

    @allure.label('owner', 'Андрей')
    @allure.story('Страница товаров')
    @allure.step('Сортировка товаров по возрастанию цены')
    def check_sort_by_price(self):
        sorter = self.find(loc.SORT_BTN).first
        sorter.select_option('Price')
        self.page.wait_for_selector(loc.PRICE)
        sorted_prices = [
            float(price.inner_text().replace('$', ''))
            for price in self.find(loc.PRICE).all()
            if price.inner_text().strip() and price.inner_text().replace('.', '', 1).isdigit()
        ]
        assert sorted_prices == sorted(sorted_prices)
