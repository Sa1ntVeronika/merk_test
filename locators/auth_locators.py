from appium.webdriver.common.appiumby import AppiumBy


LOGIN_INPUT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': ''
    }
}

ENTER_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/main_button'
    }
}

SWITCH_TO_REG_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/btn_reg'
    }
}

LICENSE_AGREEMENT_CHECKBOX = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/license_agreement_checkbox'
    }
}

NOTIFY_AGREEMENT_CHECKBOX = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/mailing_agreement_checkbox'
    }
}

AUTH_PAGE_TITLE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/txtTitle'
    }
}

ERROR_MESSAGE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/til_error_text'
    }
}

YANDEX_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/sign_in_yandex_button'
    }
}

GOOGLE_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/sign_in_google_button'
    }
}

MF_PLUS_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/sign_in_megafon_button'
    }
}


MF_POPUP_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/sign_in_megafon_popup'
    }
}


MF_PHONE_LOGIN_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector':'ru.app.androidmobile:id/mf_phone_login_button'
    }
}

VK_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/sign_in_vkontakte_button'
    }
}

FACEBOOK_SIGN_IN = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/sign_in_facebook_button'
    }
}

RESTORE_PASSWORD_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/restore_pass_button'
    }
}

CONFIRM_RESTORE_WITH_SMS_TITLE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/title'
    }
}

RESTORE_PASSWORD_INPUT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '//android.widget.TextView[@text="Придумайте новый пароль"]//'
                    'following-sibling::android.widget.EditText'
    }
}

RESTORE_CODE_INPUT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '//android.widget.TextView[@text="Введите код из смс"]//'
                    'following-sibling::android.widget.EditText'
    }
}

REFRESH_SMS_CODE_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/refresh_code_button'
    }
}

REFRESH_SMS_CODE_TIMER_TEXT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/refresh_code_text'
    }
}

CONFIRM_CODE_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/confirm_code_button'
    }
}

MF_PHONE_LOGIN_INPUT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '//android.widget.TextView[@text="Введите номер телефона"]//'
                    'following-sibling::android.widget.EditText'
    }
}

MF_SMS_CODE_INPUT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '//android.widget.TextView[@text="Введите код из SMS"]//'
                    'following-sibling::android.widget.EditText'
    }
}

SUBSCRIBER_MF_LOGIN_SCREEN = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '//android.widget.TextView[@text="Вход для абонентов МегаФона"]'
    }
}

MF_ACCEPT_SMS_CODE_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '//android.widget.TextView[@text="Подтвердить"]'
    }
}
