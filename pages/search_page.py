import time
from pages.base_page import BasePage
from locators.search_page_locators import *
from locators.base_locators import *


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def tap_on_input_search(self):
        self.tap_on_element(SEARCH_INPUT)
        return self

    def tap_on_search_cancel_button(self):
        self.tap_on_element(SEARCH_INPUT_CANCEL_BUTTON)
        return self

    def enter_search_input(self, text):
        element = self.get_element(SEARCH_INPUT)
        self.type_text_to_field(element, text)
        self.hide_keyboard()
        return self

    def tap_on_result_by_alias(self, alias):
        """Тап по результату поиска по переданному алиасу"""
        locator = locator_by_name(alias)
        self.tap_on_element(locator)
        return self

    ###############
    ### Asserts ###
    ###############


    def assert_search_page_opened(self):
        assert self.is_element_presented(SEARCH_PAGE), f'экран поиска не открыт'
        return self

    def assert_search_page_title(self):
        assert self.get_element(SEARCH_TITLE).text == self.search_title, f'Название заголовка не соостветствует ({self.search_title})'
        return self

    def assert_search_input_hint(self):
        assert self.get_element(SEARCH_INPUT_HINT).text == self.search_input_hint, f'Подсказка в инпуте не соответствует ({self.search_input_hint})'
        return self
