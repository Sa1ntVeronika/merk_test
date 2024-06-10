from appium import webdriver
from pages.base_page import BasePage
from appium.webdriver.webelement import WebElement
from pages.auth_page import AuthPage
from locators.onboarding_locators import *
from appium.webdriver.common.appiumby import AppiumBy


class OnboardingPage(BasePage):

    def tap_on_continue_button(self):
        self.tap_on_element(CONTINUE_BUTTON)
        return self

    def tap_on_login_button(self):
        self.tap_on_element(LOGIN_BUTTON)
        return self

    def change_lang_button(self):
        locator = {'android': 'ru.start.androidmobile:id/btn_language'}

    def tap_on_skip_button(self):
        self.tap_on_element(SKIP_BUTTON)
        return self

    # """Проверки (Asserts)"""

    def assert_onboarding_page_is_opened(self):
        assert self.is_element_presented(ONBOARDING_PAGE), 'Онбординг не открылся'
        return self

    def run_skip_onboarding(self):
        self.tap_on_continue_button() \
            .tap_on_skip_button()
        AuthPage(self.driver) \
            .assert_registration_page_opened() \
            .tap_on_close_button()
        return self
