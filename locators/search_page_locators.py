from appium.webdriver.common.appiumby import AppiumBy

SEARCH_PAGE = {
    'ios': {
        'method': '',
        'selector:': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/general_search'
    }
}

SEARCH_TITLE = {
    'ios': {
        'method': '',
        'selector:': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/title_text_view'
    }
}

SEARCH_INPUT = {
    'ios': {
        'method': '',
        'selector:': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/til_edit_text'
    }
}

SEARCH_INPUT_HINT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/til_hint_text_fake'
    }
}

SEARCH_INPUT_CANCEL_BUTTON = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/input_cancel'
    }
}

SEARCH_POPULAR_QUERIES_TITLE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/rv_popular_search_title'
    }
}

SEARCH_POPULAR_QUERIES = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/ll_search_text'
    }
}

SEARCH_RESULT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/rv_search_result'
    }
}

SEARCH_RESULT_TITLE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/itemTitle'
    }
}

SEARCH_RESULT_CONTENT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Фильмы и сериалы'
    }
}

SEARCH_RESULT_CATCHUPS = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'В эфире на телеканалах'
    }
}

SEARCH_RESULT_CHANNELS = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Телеканалы'
    }
}

SEARCH_RESULT_PERSONS = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'Персоны'
    }
}

SEARCH_EMPTY_RESULT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/empty_view'
    }
}

SEARCH_CATEGORIES_FILTERS = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/ll_categories_filters'
    }
}


