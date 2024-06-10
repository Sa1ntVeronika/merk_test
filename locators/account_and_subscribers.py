from appium.webdriver.common.appiumby import AppiumBy

ACCOUNTS_AND_SUBSCRIPTIONS_SCREEN = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'account_settings'
    }
}

CHANGE_PASSWORD_BTN = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/btn_change_pass'
    }
}
