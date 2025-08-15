from test_ui_rassokhin_pw.pages.base_page import BasePage
from test_ui_rassokhin_pw.pages.locators import create_account_locators as loc
from playwright.sync_api import expect
from faker import Faker
import allure


class CreateAccount(BasePage):
    page_url = 'customer/account/create/'

    @allure.label('owner', 'Андрей')
    @allure.story('Страница регистрации пользователя')
    @allure.step('Регистрация нового пользователя')
    def user_registration(self, first_name, last_name, email, password, confirm_password):
        first_name_field = self.find(loc.FIRST_NAME)
        last_name_field = self.find(loc.LAST_NAME)
        email_field = self.find(loc.EMAIL)
        password_field = self.find(loc.PASSWORD)
        confirm_password_field = self.find(loc.CONFIRM_PASSWORD)
        create_account_btn = self.find(loc.CREATE_ACCOUNT_BTN)
        first_name_field.fill(first_name)
        last_name_field.fill(last_name)
        email_field.fill(email)
        password_field.fill(password)
        confirm_password_field.fill(confirm_password)
        create_account_btn.click()

    @allure.label('owner', 'Андрей')
    @allure.story('Страница регистрации пользователя')
    @allure.step('Проверка регистрации')
    def check_registration(self, text):
        msg = self.find(loc.MSG)
        expect(msg).to_have_text(text)

    def create_fake_email(self):
        fake = Faker()
        return fake.email()

    @allure.label('owner', 'Андрей')
    @allure.story('Страница регистрации пользователя')
    @allure.step('Проверка зарегистрированного пользователя')
    def check_account_information(self, create_name, create_email):
        account_info = self.find(loc.ACCOUNT_INFORMATION).first.inner_text()
        lines = account_info.strip().split('\n')
        name = lines[0].strip()
        email = lines[1].strip()
        assert name == create_name
        assert email == create_email

    @allure.story('Страница регистрации пользователя')
    @allure.step('Проверка на то, что пароли разные')
    def check_error_with_different_passwords(self, text):
        error = self.find(loc.ERROR_PASSWORD)
        expect(error).to_have_text(text)
