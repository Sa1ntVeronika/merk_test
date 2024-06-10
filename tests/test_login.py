import time

from pages.auth_page import AuthPage
from pages.settings_page import SettingsPage
from pages.onboarding_page import OnboardingPage
from pages.main_page import MainPage
from preconditions import deeplinks as dl

adult_vyzhivshaya_18 = dl.adult_product['vyzhivshaya_18']
adult_goliaf_16 = dl.adult_product['goliaf_16']

tv_autoplay_five_channel = dl.tv_channel_autoplay['5y_vitrina']

adult_tv_kinokomediya_24 = dl.adult_tv['24tv']['kinokomediya']

settings_screen = dl.system_link['settings']


def test_auth_from_onboarding_page(driver_reset):
    """Авторизация с экрана онбординга"""
    email = 'maqa@qa.qa'
    password = 'qqqqqq'

    OnboardingPage(driver_reset)\
        .tap_on_login_button()
    AuthPage(driver_reset)\
        .enter_email(email)\
        .enter_password(password)\
        .tap_enter_button() \
        .tap_back_button()
    MainPage(driver_reset)\
        .tap_on_tabbar_settings()
    SettingsPage(driver_reset)\
        .tap_accounts_and_subscriptions()\
        .assert_email_presented(email)


def test_reg_with_existing_user(driver_reset):
    """Попытка регистрации ранее созданным пользователем"""
    email = 'maqa@qa.qa'
    password = 'qqqqqq'

    OnboardingPage(driver_reset)\
        .tap_on_login_button()
    AuthPage(driver_reset)\
        .tap_switch_to_reg_button()\
        .enter_email(email)\
        .enter_password(password)\
        .tap_license_agreement_checkbox()\
        .tap_enter_button()\
        .assert_error_message_is_valid('Этот e-mail уже зарегистрирован')

