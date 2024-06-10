from appium.webdriver.common.appiumby import AppiumBy


def locator_by_name(name):
    return {
        'ios': {
            'method': '',
            'selector': name
        },
        'android': {
            'method': AppiumBy.ACCESSIBILITY_ID,
            'selector': name
        }
    }


def locator_by_xpath(name):
    return{
        'ios': {
            'method': '',
            'selector': name
        },
        'android': {
            'method': AppiumBy.XPATH,
            'selector': name
        }
    }


INPUT_FIELD = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/til_edit_text'
    }
}

HINT_INPUT_FIELD = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/til_hint_text_fake'
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
        'selector': 'ru.app.androidmobile:id/back_button'
    }
}

TABBAR_MAIN_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/navigation_home'
    }
}
TABBAR_SEARCH_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/navigation_search'
    }
}
TABBAR_MY_START_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/navigation_my'
    }
}
TABBAR_TV_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/navigation_channels'
    }
}

TABBAR_SETTINGS_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/navigation_settings'
    }
}

CLOSE_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/close_button'
    }
}

TOAST = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '/hierarchy/android.widget.Toast'
    }
}

WEBVIEW = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '//android.webkit.WebView'
    }
}

EXPAND_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/expand_button'
    }
}

ALERT_OK_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'android:id/button1'
    }
}

ALERT_CANCEL_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'android:id/button2'
    }
}

BOTTOM_SHEET = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/standard_bottom_sheet'
    }
}

BOTTOM_SHEET_BUTTON_OK = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/bottomsheet_button_ok'
    }
}

BOTTOM_SHEET_BUTTON_CANCEL = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/bottomsheet_button_cancel'
    }
}

DESCRIPTION_VIEW = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/description_view'
    }
}

HEADER_TITLE_VIEW = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/header_title_view'
    }
}

TITLE_VIEW = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/title_view'
    }
}

BUTTON_DISAGREE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/button_cancel'
    }
}

BUTTON_AGREE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/button_ok'
    }
}

TITLE_TEXT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/txtTitle'
    }
}

BUTTON_BUY = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/btnBuy'
    }
}

ALERT_TITLE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/titleAlert'
    }
}

DESCRIPTION_TEXT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/description_textview'
    }
}

DELETE_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/delete_button'
    }
}

WIDGET_TEXTVIEW = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.XPATH,
        'selector': '//android.widget.TextView'
    }
}