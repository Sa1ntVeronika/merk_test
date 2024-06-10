import utils
from pages.search_page import SearchPage
from pages.main_page import MainPage
from pages.onboarding_page import OnboardingPage
from pages.auth_page import AuthPage
from preconditions import deeplinks as dl

search_scr = dl.system_link['search']
settings_screen = dl.system_link['settings']
skip_onboarding = dl.system_link['skip_onboarding']


def test_hint_input(driver_reset):
    """Проверяет открытие экрана Поиск + корректность отображаемого текста в хинте"""
    OnboardingPage(driver_reset)\
        .assert_onboarding_page_is_opened()\
        .go_to_deeplink(skip_onboarding)
    AuthPage(driver_reset)\
        .assert_registration_page_opened()\
        .tap_on_close_button()
    MainPage(driver_reset)\
        .assert_main_page_is_opened()\
        .tap_on_tabbar_search()
    SearchPage(driver_reset)\
        .assert_search_page_opened()\
        .assert_search_page_title()\
        .assert_search_input_hint()

