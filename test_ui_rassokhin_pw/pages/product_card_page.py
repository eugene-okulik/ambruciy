from test_ui_rassokhin_pw.pages.base_page import BasePage
from test_ui_rassokhin_pw.pages.locators import card_product_locators as loc
from playwright.sync_api import expect
import allure


class ProductCard(BasePage):
    @allure.label('owner', 'Андрей')
    @allure.story('Страница товаров')
    @allure.step('Получение названия товара в карточке товара')
    def check_product_card(self, name_product):
        product_header = self.find(loc.PRODUCT_HEADER)
        product_name_in_card = self.find(loc.PRODUCT_NAME_IN_CARD)
        expect(product_header).to_have_text(name_product)
        expect(product_name_in_card).to_have_text(name_product)
