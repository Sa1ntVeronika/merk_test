from appium.webdriver.common.appiumby import AppiumBy


SETTINGS_SCREEN = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'main_settings'
    }
}

SETTINGS_TITLE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/title_text_view'
    }
}

CREATE_PROFILE_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '//android.widget.ImageView[@content-desc="Добавить"]'
    }
}

PROFILE_LIST = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/list_profiles'
    }
}

PROFILE_NAME = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/name_profile'
    }
}

EDIT_PROFILE_NAME = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/til_edit_text'
    }
}

SAVE_PROFILE_CHANGES = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/btn_save'
    }
}

PROFILE_TYPE_SWITCHER = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/switch_is_child'
    }
}

EDIT_PROFILES_SCREEN_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/btn_edit_profile'
    }
}

EDIT_PROFILE_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/img_edit'
    }
}

DELETE_PROFILE_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/btn_delete_profile'
    }
}

OK_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/ok_button'
    }
}

BACK_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/ok_button'
    }
}

ACCOUNTS_AND_SUBSCRIPTIONS = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Аккаунт и подписки'
    }
}

CONTINUE_WATCHING = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Продолжить просмотр'
    }
}


FAVORITES = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Избранное'
    }
}

DOWNLOADS = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Загрузки'
    }
}


APPLICATION_SETTINGS = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Настройки приложения'
    }
}

SUBSCRIPTIONS_BLOCK = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/ll_main_open_di'
    }
}

LOGOUT_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/btn_log_out'
    }
}

ENTER_ACCOUNT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Войти в аккаунт'
    }
}

DEVICES = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Устройства'
    }
}

CHANGE_LANGUAGE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Изменить язык'
    }
}

ACTIVATE_PROMOCODE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Активировать промокод'
    }
}

SUPPORT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Служба поддержки'
    }
}

AGREEMENTS = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Правила и условия'
    }
}

DEBUG_MENU = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Дебаг меню'
    }
}

DELETE_ALL_DEVICES = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/ll_delete_all_device'
    }
}

EDIT_PROFILE_SCREEN = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/container_edit_users'
    }
}

EDIT_NAME_TITLE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '//android.widget.TextView[@text="Редактировать имя"]'
    }
}


EDIT_NAME = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '//android.widget.TextView[@text="Имя"]'
    }
}

EDIT_GENDER = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '//android.widget.TextView[@text="Пол"]'
    }
}


AUTH_FROM_SUPPORT_PAGE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/btn_sign_support'
    }
}

REG_FROM_SUPPORT_PAGE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/btn_reg_support'
    }
}

MALE_RADIOBUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/male'
    }
}


FEMALE_RADIOBUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/female'
    }
}

SUPPORT_RESOLVE_PROBLEM_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/btn_resolve_problem'
    }
}

EDIT_EMAIL = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/edit_email'
    }
}

DESCRIBE_PROBLEM_SUPPORT_FIELD = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/edit_another'
    }
}

SEND_REPORT_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/btn_send_form'
    }
}

TITLE_CHAT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/title_chat'
    }
}

COUPON_SCREEN = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'promocode'
    }
}

LANGUAGE_SCREEN = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'select_language'
    }
}

DEVICE_SCREEN = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'devices'
    }
}

SUPPORT_SCREEN = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'support'
    }
}

POLICY_SCREEN = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'terms_and_conditions'
    }
}

LOGIN_IN_TV_WITH_CODE_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Войти по коду на ТВ'
    }
}

LOGIN_IN_TV_SCREEN = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/tv_code_login_container'
    }
}

LOGIN_IN_TV_SCREEN_TITLE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/tv_title'
    }
}

LOGIN_IN_TV_SCREEN_SUBTITLE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/tv_subtitle'
    }
}

LOGIN_IN_TV_SCREEN_DESCRIPTION = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/tv_description'
    }
}

LOGIN_IN_TV_SCREEN_INPUT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/til_edit_text'
    }
}

LOGIN_IN_TV_SCREEN_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/btn_login'
    }
}

TEXT_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '//android.widget.TextView'
    }
}
