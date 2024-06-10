from appium.webdriver.common.appiumby import AppiumBy

MAIN_PAGE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'main'
    }
}

MAIN_PAGE_LOADING = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'main_loading'
    }
}

CONTENT_CARD = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/main_view'
    }
}


FEATURE_BLOCK = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/main_view_scrollable_container'
    }
}

FEATURE_DESCRIPTION = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/description_textview'
    }
}

CW_CARD = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/cw_framelayout_image'
    }
}

CW_DURATION_TEXT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/duration_textview'
    }
}

CW_PROGRESS = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/watched_progress'
    }
}

CW_TITLE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/title_textview'
    }
}

CW_SUBTITLE = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/subtitle_textview'
    }
}

RECOMMENDATION_SELECTION = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'segmentation'
    }
}

SELECTION_BLOCK = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/main_block_view'
    }
}

BANNER = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/banner'
    }
}

CREATE_CHILD_PROFILE_TEXT = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/text_create_cp'
    }
}

COLLECTION_SELECTION = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'collections'
    }
}

COLLECTION_SCREEN = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ACCESSIBILITY_ID,
        'selector': 'collection'
    }
}

CHANNEL_IN_TV_SELECTION = {
    'ios': {
        'method': '',
        'selector': ''
    },
    'android': {
        'method': AppiumBy.ID,
        'selector': 'ru.app.androidmobile:id/thumbnail_imageview_channel'
    }
}
