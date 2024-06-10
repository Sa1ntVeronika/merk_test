import time

from selenium.webdriver.support import expected_conditions as ec

import utils
from pages.base_page import BasePage
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from locators.settings_page_locators import *
from locators.account_and_subscribers import *
from locators.base_locators import *



class SettingsPage(BasePage):

    def tap_accounts_and_subscriptions(self):
        self.tap_on_element(ACCOUNTS_AND_SUBSCRIPTIONS)
        return self

    def tap_devices_button(self):
        self.scroll_to_element_by_locator(DEVICES)
        self.tap_on_element(DEVICES)
        return self

    def tap_activate_promocode(self):
        self.tap_on_element(ACTIVATE_PROMOCODE, need_to_scroll=True)
        return self

    def tap_on_logout_button(self):
        """Тап на кнопку 'Выйти из аккаунта' """
        self.tap_on_element(LOGOUT_BUTTON)
        return self

    def tap_on_create_profile_button(self):
        """Тап на кнопку создания профиля"""
        self.tap_on_element(CREATE_PROFILE_BUTTON)
        return self

    def enter_profile_name(self, name: str):
        """Ввод имени профиля {name} в инпут"""
        input = self.get_element(EDIT_PROFILE_NAME)
        self.type_text_to_field(input, name)
        return self

    def save_profile_changes(self):
        """Сохранить изменения профиля"""
        self.tap_on_element(SAVE_PROFILE_CHANGES)
        return self

    def tap_on_child_switcher(self):
        """Тап на свичер типа профиля (детский/взрослый)"""
        self.tap_on_element(PROFILE_TYPE_SWITCHER)
        return self

    def select_profile(self, name):
        """Смена профиля на профиль {name}"""
        self.tap_on_element_by_text(name)
        return self

    def tap_on_edit_screen_profiles_button(self):
        """Там по кнопке Редактировать пользователей на экране настроек"""
        self.tap_on_element(EDIT_PROFILES_SCREEN_BUTTON)
        return self

    def tap_on_edit_profile_button(self, name):
        """Тап по кнопке Редактировать"""

        time.sleep(1)
        parent_profile = self.wdwait(
            ec.visibility_of_element_located,
            AppiumBy.XPATH, f"//android.widget.TextView[@text='{name}']//ancestor::android.view.ViewGroup"
        )
        edit_button_profile = parent_profile.find_element(AppiumBy.ID, "ru.start.androidmobile:id/img_edit")
        edit_button_profile.click()
        return self

    def tap_on_delete_profile_button(self):
        self.tap_on_element(DELETE_PROFILE_BUTTON)
        # time.sleep(1) #вынужденная мера, не удалять :)
        return self

    def tap_on_profile_name(self, name: str):
        self.tap_on_element_by_text(name)
        return self

    def tap_on_child_profile(self):
        profile_list_parent = self.get_element(PROFILE_LIST)
        profile_list: [WebElement] = profile_list_parent.find_elements(AppiumBy.XPATH, './/*//*')
        # for el in profile_list:
        #     print((el.get_attribute('class')), 123)
        child_profile = profile_list[0]
        child_profile.click()
        time.sleep(2)
        return self

    def tap_on_adult_profile(self):
        profile_list_parent = self.get_element(PROFILE_LIST)
        profile_list: [WebElement] = profile_list_parent.find_elements(AppiumBy.XPATH, './/*//*')
        child_profile = profile_list[1]
        child_profile.click()
        return self

    def tap_on_cw_in_settings(self):
        self.tap_on_element(CONTINUE_WATCHING)
        return self

    def tap_on_downloads_in_settings(self):
        self.tap_on_element(DOWNLOADS)
        return self

    def tap_on_favourites_in_settings(self):
        self.tap_on_element(FAVORITES)
        return self

    def tap_on_enter_account(self):
        self.tap_on_element(ENTER_ACCOUNT)
        return self

    def tap_on_support(self):
        self.tap_on_element(SUPPORT, need_to_scroll=True)
        return self

    def tap_on_auth_from_support_page(self):
        self.tap_on_element(AUTH_FROM_SUPPORT_PAGE)
        return self

    def tap_on_registration_from_support_page(self):
        self.tap_on_element(REG_FROM_SUPPORT_PAGE)
        return self

    def tap_on_enter_by_code_on_tv(self):
        self.tap_on_element(LOGIN_IN_TV_WITH_CODE_BUTTON)
        return self

    def tap_on_enter_button_in_tv_login_screen(self):
        self.tap_on_element(LOGIN_IN_TV_SCREEN_BUTTON)
        return self

    def enter_code_to_login_in_tv(self, code):
        element = self.get_element(LOGIN_IN_TV_SCREEN_INPUT)
        self.type_text_to_field(element, code)
        self.tap_on_enter_button_in_tv_login_screen()
        return self

    def assert_request_code_proceed_for_login_in_tv_code(self, code):
        expected_request = ["auth", "code", "proceed", code]
        data = self.get_data_from_response('code_proceed')
        assert expected_request == data
        return self

    def change_user_name(self, name):
        """Изменяет имя пользователя в настрйоках аккаунта"""
        self.tap_on_element(EDIT_NAME)
        assert self.is_element_presented(EDIT_NAME_TITLE), "не открылся экран изменения имени"
        input = self.get_element(INPUT_FIELD)
        self.type_text_to_field(input, name)
        self.tap_on_element(SAVE_PROFILE_CHANGES)
        self.assert_toast_displayed_with_text("Мы сохранили ваше имя")
        assert self.is_element_presented_by_text(name)
        return self

    def change_user_gender(self, gender):
        """Изменяет пол пользователя в настройках аккаунта"""
        self.tap_on_element(EDIT_GENDER)
        assert self.is_element_presented_by_text("Выберите пол"), "не открылся поп-ап смены пола"
        if gender == "Мужской":
            self.tap_on_element(MALE_RADIOBUTTON)
        else:
            self.tap_on_element(FEMALE_RADIOBUTTON)
        self.tap_on_element(SAVE_PROFILE_CHANGES)
        self.assert_toast_displayed_with_text('Данные успешно обновлены')
        assert self.is_element_presented_by_text(gender)
        return self

    def delete_device_from_list(self):
        devices = self.get_data_from_response('device_list')
        description = devices[-1]['description']
        device_element = self.wdwait(
            ec.visibility_of_element_located,
            AppiumBy.XPATH, f"//android.widget.TextView[@text='{description}']/../.."
        )
        device_delete = device_element.find_element(AppiumBy.ID, 'ru.start.androidmobile:id/delete_button')
        device_delete.click()
        assert self.is_element_presented_by_text('Удалить устройство'), 'не открылся поп-ап удадления'
        assert self.is_element_presented_by_text(f'Удалив {description}'), 'удаляется неверное устройство'
        self.tap_on_element(ALERT_CANCEL_BUTTON)
        return self

    def send_report_to_support_with_given_text_by_user_with_email(self, text, email):
        self.tap_on_element(SUPPORT, need_to_scroll=True)
        self.tap_on_element(SUPPORT_RESOLVE_PROBLEM_BUTTON)
        self.tap_on_element_by_text('Android')
        self.tap_on_element_by_text('У меня другая проблема')
        field = self.get_element(DESCRIBE_PROBLEM_SUPPORT_FIELD)
        self.type_text_to_field(field, text)
        self.tap_on_element(SEND_REPORT_BUTTON)

        report_response = self.get_data_from_response('create_ticket')
        assert report_response['data']['recipient'] == email, 'email отличается от пользовательского'
        assert report_response['data']['subject'] in text, 'текст проблемы не соответствует набранному.' \
                                                           'ожидали'
        return self


    # """Проверки (Asserts)"""
    def run_assert_screen_opened(self, name):
        match name:
            case 'settings_screen':
                self.assert_settings_screen_is_opened()
            case 'coupon_screen':
                self.assert_coupon_screen_opened()
            case 'language_screen':
                self.assert_language_screen_opened()
            case 'device_screen':
                self.assert_devices_are_displayed()
            case 'accounts_screen':
                self.assert_account_and_subscription_screen_opened()
            case 'support_screen':
                self.assert_support_screen_is_opened()
            case 'policy_screen':
                self.assert_policy_screen_is_opened()
            case 'terms_of_use':
                self.assert_term_of_use_is_opened()
            case 'privacy_policy':
                self.assert_privacy_policy_is_opened()
            case 'terms_of_promocode':
                self.assert_terms_of_promocode_is_opened()
        return self

    def assert_settings_screen_is_opened(self):
        assert self.is_element_presented(SETTINGS_SCREEN), 'Экран Настроек не открыт'
        settings_page_title = self.get_element(SETTINGS_TITLE)
        assert 'Настройки' == settings_page_title.text, 'Заголовок не соответствует ожидаемому "Настройки"'
        return self

    def assert_create_child_profile_screen_opened(self):
        assert self.is_element_presented(EDIT_PROFILE_SCREEN)
        assert self.get_element(PROFILE_TYPE_SWITCHER).get_attribute('checked')
        return self

    def assert_account_and_subscription_screen_opened(self):
        assert self.is_element_presented(ACCOUNTS_AND_SUBSCRIPTIONS_SCREEN, duration=5), 'Экран Аккаунт и подписки не открыт'
        return self

    def assert_device_screen_is_opened(self):
        assert self.is_element_presented(DEVICE_SCREEN)
        return self

    def assert_coupon_screen_opened(self):
        assert self.is_element_presented(COUPON_SCREEN)
        return self

    def assert_language_screen_opened(self):
        assert self.is_element_presented(LANGUAGE_SCREEN)
        return self

    def assert_support_screen_is_opened(self):
        assert self.is_element_presented(SUPPORT_SCREEN)
        return self

    def assert_policy_screen_is_opened(self):
        assert self.is_element_presented(POLICY_SCREEN), 'Экран Правила и Условия не открыт'
        return self

    def assert_term_of_use_is_opened(self):
        assert self.is_element_presented_by_text('Пользовательское соглашение', duration=7), \
            'экран с пользовательским соглашением не открыт'
        return self

    def assert_privacy_policy_is_opened(self):
        assert self.is_element_presented_by_text('Политика приватности', duration=7), 'экран с политиками приватности не открыт'
        return self

    def assert_terms_of_promocode_is_opened(self):
        assert self.is_element_presented_by_text('Правила использования промокодов', duration=7), \
            'экран с правилами промокодов не открыт'
        return self

    def assert_edit_users_button_unavailable(self):
        assert not self.is_element_presented(EDIT_PROFILES_SCREEN_BUTTON)
        return self

    def assert_profile_exist(self, name: str):
        """Проверяем, что профиль с переданным именем существует"""
        profiles = self.get_elements(PROFILE_NAME)
        assert bool([profile for profile in profiles if profile.text == name]), f'Профиль с именем {name} не найден!'

    def assert_child_profile_is_active(self):
        assert not self.is_element_presented(CREATE_PROFILE_BUTTON, 1), 'Присутствует кнопка создания профиля'
        assert not self.is_element_presented(EDIT_PROFILE_BUTTON, 1), 'Присутствует кнопка редактирования профиля'

    def assert_profile_deleted(self, name):
        self.assert_toast_displayed_with_text(name)
        assert not self.is_element_presented_by_text(name)

    def assert_email_presented(self, email: str):
        assert self.is_element_presented_by_text(email.lower(), 5)
        return self

    def assert_subscription_available(self):
        self.scroll_to_element_by_locator(SUBSCRIPTIONS_BLOCK)
        assert self.is_element_presented_by_text('Подписка на Google Play'), 'Элемент не найден'
        return self

    def assert_create_profile_unavailable(self):
        assert not self.is_element_presented(CREATE_PROFILE_BUTTON, 4), 'Присутствует кнопка создания профиля'
        return self

    def assert_user_not_authorized(self):
        """ Проверка, что юзер не авторизован (в Настрйоках есть кнопка 'Войти в аккаунт'"""
        assert self.is_element_presented(ENTER_ACCOUNT), 'Кнопка Войти в аккаунт отсутствует'
        return self

    def assert_menu_items_for_virtual_displayed(self):
        """Проверка отображения пунктов меню настроек для виртуала"""
        for menu_item in self.menu_items_virtual:
            locator = locator_by_name(menu_item)
            assert self.is_element_presented(locator, need_to_scroll=True)
        self.scroll_down()
        for menu_item in self.menu_no_items_virtual:
            locator = locator_by_name(menu_item)
            assert not self.is_element_presented(locator, need_to_scroll=True)

    def assert_menu_items_for_authorized_displayed(self):
        """Проверка отображения пунктов меню настроек для авторизованного"""
        for menu_item in self.menu_items_authorized:
            locator = locator_by_name(menu_item)
            assert self.is_element_presented(locator, need_to_scroll=True)
        self.scroll_down()
        for menu_item in self.menu_no_items_authorized:
            locator = locator_by_name(menu_item)
            assert not self.is_element_presented(locator, need_to_scroll=True)

    def assert_devices_are_displayed(self):
        """Проверка отображения списка девайсов на основе данных от API"""
        devices = self.get_data_from_response('device_list')
        for device in devices:
            while not self.is_element_presented_by_text(device['description'], duration=2):
                self.scroll_down()
            assert self.is_element_presented_by_text(device['description'], duration=5)

    def assert_menu_items_for_virtual_displayed_kids(self):
        '''Проверка отображения пунктов меню для виртуала в детском профиле'''
        for menu_item in self.menu_items_virtual_kids:
            locator = locator_by_name(menu_item)
            assert self.is_element_presented(locator, need_to_scroll=True)
        self.scroll_down()
        '''Проверка отсутствия пунктов меню для виртуала в детском профиле'''
        for no_menu_item in self.menu_no_items_virtual_kids:
            assert not self.is_element_presented_by_text(no_menu_item)

    def assert_menu_items_for_authorized_displayed_kids(self):
        '''Проверка отображения пунктов меню для виртуала в детском профиле'''
        for menu_item in self.menu_items_authorized_kids:
            locator = locator_by_name(menu_item)
            assert self.is_element_presented(locator, need_to_scroll=True)
        self.scroll_down()
        '''Проверка отсутствия пунктов меню для виртуала в детском профиле'''
        for no_menu_item in self.menu_no_items_authorized_kids:
            assert not self.is_element_presented_by_text(no_menu_item, 3)