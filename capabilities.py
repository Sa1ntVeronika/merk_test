import pathlib

CURRENT_DIR = pathlib.Path().resolve()
def android_reset(version):
    return dict(
        platformName='Android',
        platformVersion=version,
        automationName='uiautomator2',
        appPackage='ru.app.androidmobile',
        appActivity='.ui.activities.utils.ActivitySplash',
        autoGrantPermissions=True,
        newCommandTimeout=540,
        udid='emulator-5554',
    )

def android_no_reset(version):
    return dict(
        platformName='Android',
        platformVersion=version,
        automationName='uiautomator2',
        appPackage='ru.app.androidmobile',
        noReset=True,
        appActivity='.ui.activities.utils.ActivitySplash',
        udid='emulator-5554',
    )
DESIRED_CAPS_ANDROID_SIM_NO_RESET = dict(
    platformName='Android',
    platformVersion='11',
    automationName='uiautomator2',
    appPackage='ru.app.androidmobile',
    noReset=True,
    appActivity='.ui.activities.utils.ActivitySplash',
    udid='emulator-5554',
)
