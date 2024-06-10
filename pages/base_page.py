from selenium.webdriver.support.ui import WebDriverWait as WDWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from locators.base_locators import *
from locators.settings_page_locators import DEBUG_MENU, DELETE_ALL_DEVICES
import time
import utils
from typing import List
from preconditions import deeplinks as dl


android_app_name = 'ru.app.androidmobile'

class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.platform = self.driver.session['platformName'].lower()

    def wdwait(self, condition, method, locator, duration=20, parent=None):
        """Ожидает, что элемент будет доступен для лоцирования"""
        # self.driver.implicitly_wait(duration)
        if parent is not None:
            wait = WDWait(parent, duration)
        else:
            wait = WDWait(self.driver, duration)
        return wait.until(condition((method, locator)))

    def get_data_from_response(self, url):
        data = utils.get_response_value_from_mitm(url)
        return data

    def switch_to_webview(self):
        """Переключает драйвер для работы с вебвью"""
        context = "WEBVIEW_ru.app.androidmobile"
        print(self.driver.contexts)
        self.driver.switch_to.context("WEBVIEW_ru.app.androidmobile")
        return self

    def switch_to_native_app(self):
        """Переключает драйвер для работы с нативным приложением"""
        self.driver.switch_to.context("NATIVE_APP")
        return self

    def close_app(self):
        """Закрывает приложение"""
        self.driver.terminate_app(android_app_name)
        return self

    def start_app(self):
        """Запускает приложение"""
        self.driver.activate_app(android_app_name)
        return self

    def go_to_deeplink(self, link):
        """Переход по диплинку"""
        time.sleep(5)
        self.driver.get(link)
        return self

    def tap_on_element(self, locator, need_to_scroll=False):
        """Тап по элементу, найденного по переданному локатору"""
        platform = self.platform.lower()
        if need_to_scroll:
            if not self.is_element_presented(locator, 4):
                self.scroll_to_element_by_locator(locator, tries=10)
        print(f"Тап по элементу {locator[platform]['selector']}")
        self.get_element(locator).click()

    def tap_on_element_by_text(self, text):
        """Тап по элементу, найденного по переданному локатору"""
        print(self.get_element_by_text(text))
        self.get_element_by_text(text).click()

    def get_element(self, locator, parent=None) -> WebElement:
        """Получение элемента по переданному локатору"""
        platform = self.platform.lower()
        return self.wdwait(ec.visibility_of_element_located, locator[platform]['method'], locator[platform]['selector'],
                           parent=parent)

    def get_elements(self, locator, parent=None) -> List[WebElement]:
        """Получение элемента по переданному локатору"""
        platform = self.platform.lower()
        return self.wdwait(ec.presence_of_all_elements_located, locator[platform]['method'],
                           locator[platform]['selector'], parent=parent)

    def get_element_by_text(self, text, parent=None) -> WebElement:
        """Получение элемента по переданному локатору"""
        return self.wdwait(ec.visibility_of_element_located,
                           AppiumBy.XPATH,
                           f"//android.widget.TextView[contains(@text, '{text}')]", parent=parent)

    def is_activity_presented(self, activity):
        """Проверяет показ нужного Activity"""
        if self.driver.wait_activity(activity, 5):
            print(f'Активити "{activity}" найден')
            return True
        else:
            print(f'Активити "{activity}" не найден, показан {self.driver.current_activity}')
            return False

    def is_element_presented(self, locator, duration=20, need_to_scroll=False, tries=5, parent=None):
        """Проверяет наличие элемента на экране с переданным временем ожидания"""
        # if self.platform == 'iOs':
        #     print(f'Элемент {locator["ios"]} найден!')
        #     return self.wdwait(AppiumBy.IOS_CLASS_CHAIN, locator['ios'], duration).is_displayed()
        # else:
        platform = self.platform.lower()
        try:
            if need_to_scroll:
                self.scroll_to_element_by_locator(locator, tries=tries)
            self.wdwait(ec.visibility_of_element_located, locator[platform]['method'],
                        locator[platform]['selector'], duration=duration, parent=parent)
            print(f'Элемент {locator[platform]["selector"]} найден!')
            return True
        except (TimeoutException, NoSuchElementException):
            print(f'Элемент {locator[platform]["selector"]} не найден!')
            return False

    def is_element_hidden(self, locator, duration=15, need_to_scroll=False):
        """Проверяет, скрылся ли элемент на экране с переданным временем ожидания"""
        count = 0
        while count < duration:
            count = count + 1
            time.sleep(1)
            if self.is_element_presented(locator, duration=1, need_to_scroll=need_to_scroll):
                continue
            else:
                print(f"Элемент {locator} скрыт")
                return True
        return False

    def is_element_presented_by_text(self, name, duration=3, parent=None):
        """Проверяет отсутствие элемента на экране с переданным временем ожидания"""
        if self.platform == 'ios':
            pass
            # print(f'Элемент {"locator"["ios"]} отсутствует')
            # return self.wdwait(AppiumBy.IOS_CLASS_CHAIN, locator['ios'], duration = 2).is_displayed()
        else:
            try:
                locator = (AppiumBy.XPATH, f"//android.widget.TextView[contains(@text, '{name}')]")
                self.wdwait(ec.visibility_of_element_located, *locator, duration=duration, parent=parent)
                print(f'Элемент {name} найден')
                return True
            except TimeoutException:
                print(f'Элемент {name} отсутствует')
                return False

    def get_webview_element(self, locator):
        """Получение элемента по переданному локатору"""
        platform = self.platform.lower()
        return self.wdwait(ec.presence_of_element_located, AppiumBy.XPATH, locator)

    def type_text_to_webview_field(self, locator, text):
        """Вводит текст {text} в переданное поле {field}"""
        self.get_webview_element(locator).send_keys(text)

    def tap_on_webview_element(self, locator):
        self.get_webview_element(locator).click()

    def scroll_down(self):
        """ Скролл экрана вниз"""
        self.driver.swipe(1045, 1450, 1045, 850, duration=350)

    def scroll_up(self):
        """ Скролл экрана вверх"""
        self.driver.swipe(1045, 850, 1045, 1550, duration=350)

    def scroll_mini(self, x_start=1045, y_start=1100, x_stop=1045, y_stop=900):
        """Скрол на одну линейку вниз"""
        self.driver.swipe(x_start, y_start, x_stop, y_stop, duration=350)
        print()

    def scroll_to_element_by_locator(self, locator, direction='down', tries=None):
        """ Скролл экрана вниз, пока на экране не будет доступен элемент по переданному локатору"""
        self.driver.implicitly_wait(1)
        scroll_count = 0
        while not self.is_element_presented(locator, 1):
            print('scrolling')
            if direction == 'down':
                self.scroll_down()
            else:
                self.scroll_up()
            scroll_count = scroll_count + 1
            if tries and scroll_count > tries:
                raise NoSuchElementException(f'Элемент {locator} не найден спустя {tries} попыток')
        element = self.get_element(locator)
        self.scroll_element_to_center(element)
        print('found!')

    def scroll_to_element_by_text(self, text,  direction='down', tries=None, scroll_to_center=True):
        """ Скролл экрана вниз, пока на экране не будет доступен элемент по переданному тексту"""
        self.driver.implicitly_wait(1)
        scroll_count = 0
        if text:
            while not self.is_element_presented_by_text(text, 1):
                if direction == 'down':
                    self.scroll_down()
                else:
                    self.scroll_up()
                if tries and scroll_count > tries:
                    raise NoSuchElementException(f'Элемент {text} не найден спустя {tries} попыток')
            element = self.get_element_by_text(text)
            if scroll_to_center:
                self.scroll_element_to_center(element)
            else:
                self.scroll_mini()

    def swipe_element_to_direction_until_text_is_visible(self, element: WebElement, text, parent=None):
        center = utils.get_center_of_element(element)
        x = utils.get_x_coordinate_to_swipe_up(self.driver)
        print(center)
        counter = 0
        while not self.is_element_presented_by_text(text, parent=parent):
            self.driver.swipe(x['start_x'], center['y'], x['stop_x'], center['y'], duration=800)
            counter += 1
            if counter >= 10:
                raise NoSuchElementException(f'не нашли элемент с текстом {text}')
            print('swiping')
        print('found!')

    def max_scroll_to_down(self):
        screen_size = self.driver.get_window_size()
        center_x = int(screen_size['width'] / 2)
        start_y = int(screen_size['height'] - 250)
        to_up = 250
        self.driver.swipe(center_x, start_y, center_x, to_up, duration=300)

    def max_scroll_to_up(self):
        screen_size = self.driver.get_window_size()
        center_x = int(screen_size['width'] / 2)
        to_down = int(screen_size['height'] - 250)
        start_y = 250
        self.driver.swipe(center_x, start_y, center_x, to_down, duration=300)

    def scroll_element_to_center(self, element):
        screen_size = self.driver.get_window_size()
        center_x = int(screen_size['width'] / 2)
        center_y = int(screen_size['height'] / 2)
        to_up = int(center_y + (center_y * 0.3))
        to_down = int(center_y - (center_y * 0.3))
        element_y = utils.get_start_coordinats_of_element(element)['y']
        match element_y:
            case element_y if center_y-130 < element_y < center_y+130:
                print('Элемент виден полностью')
            case element_y if element_y > center_y and (element_y - to_up) > 30:
                self.driver.swipe(center_x, element_y, center_x, to_up, duration=350)
            case element_y if element_y < center_y and (to_down - element_y) > 30:
                self.driver.swipe(center_x, element_y, center_x, to_down, duration=350)

    def swipe_element_until_element_with_locator_is_visible(self, element: WebElement, locator, parent=None):
        center = utils.get_center_of_element(element)
        x = utils.get_x_coordinate_to_swipe_up(self.driver)
        counter = 0
        while not self.is_element_presented(locator, duration=1, parent=parent):
            self.driver.swipe(x['start_x'], center['y'], x['stop_x'], center['y'], duration=800)
            counter += 1
            if counter >= 10:
                raise NoSuchElementException(f'не нашли элемент с текстом {locator}')
            print('swiping')
        print('found!')

    def swipe_element_to_direction(self, element: WebElement, direction='right', count=1):
        center = utils.get_center_of_element(element)
        x = utils.get_x_coordinate_to_swipe_up(self.driver)
        i = 1
        while i <= count:
            if direction == 'right':
                self.driver.swipe(x['start_x'], center['y'], x['stop_x'], center['y'], duration=800)
                i = i+1
        return self

    def swipe_until_element_is_visible(self, element: WebElement, locator, count=3, parent=None):
        center = utils.get_center_of_element(element)
        x = utils.get_x_coordinate_to_swipe_up(self.driver)
        k = 0
        while not self.is_element_presented(locator, duration=1, parent=parent) and k <= count:
            self.driver.swipe(x['start_x'], center['y'], x['stop_x'], center['y'], duration=800)
            k += 1

    def assert_webview_is_opened(self):
        """ Проверяет, открыт ли вебвью"""
        assert self.is_element_presented(WEBVIEW), 'Webview не открылось'
        return self

    def hide_keyboard(self):
        self.driver.hide_keyboard()
        return self

    def type_text_to_field(self, field: WebElement, text: str):
        """Вводит текст {text} в переданное поле {field}"""
        field.clear()
        field.send_keys(text)

    def tap_on_close_button(self):
        self.tap_on_element(CLOSE_BUTTON)
        return self

    def tap_back_button(self):
        self.tap_on_element(BACK_BUTTON)
        return self

    def tap_on_tabbar_settings(self):
        self.tap_on_element(TABBAR_SETTINGS_BUTTON)
        return self

