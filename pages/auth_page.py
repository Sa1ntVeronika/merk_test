import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from appium.webdriver.webelement import WebElement
from locators.base_locators import *
from locators.auth_locators import *
import utils

class AuthPage(BasePage):

    def registration_with_email(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.tap_license_agreement_checkbox()
        self.tap_notify_agreement_checkbox()
        self.tap_enter_button()
        return self

    def registration_with_email_without_notify(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.tap_license_agreement_checkbox()
        self.tap_enter_button()
        return self

    def authentication_with_email_or_phone(self, login, password):
        self.enter_email(login)
        self.enter_password(password)
        self.tap_enter_button()
        return self

    def tap_license_agreement_checkbox(self):
        self.tap_on_element(LICENSE_AGREEMENT_CHECKBOX)
        return self

    def tap_notify_agreement_checkbox(self):
        self.tap_on_element(NOTIFY_AGREEMENT_CHECKBOX)
        return self

    def enter_email(self, email):
        self.type_text_to_field(self.email_input(), email)
        return self

    def enter_password(self, password):
        self.type_text_to_field(self.password_input(), password)
        return self

    def tap_enter_button(self):
        self.tap_on_element(ENTER_BUTTON)
        return self

    def tap_switch_to_reg_button(self):
        self.tap_on_element(SWITCH_TO_REG_BUTTON)
        return self


    def assert_auth_page_opened(self):
        assert self.is_element_presented_by_text('Вход в аккаунт')
        return self

    def assert_registration_page_opened(self):
        assert self.is_element_presented_by_text('Зарегистрируйтесь для просмотра', duration=7)
        return self

    def assert_error_message_is_valid(self, text):
        message = self.get_element(ERROR_MESSAGE)
        print(message.text)
        assert message.text == text, f'Текст ошибки неверный, должен быть {text}'
        return self


