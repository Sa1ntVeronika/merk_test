

from pages.base_page import BasePage
from locators.main_page_locators import *
from locators.base_locators import *


class MainPage(BasePage):


    def assert_main_page_is_opened(self):
        """Проверям, что открыт главный экран"""
        assert self.is_element_presented(MAIN_PAGE), "Главная страница не открыта"
        return self
