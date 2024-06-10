import pytest
from pytest import fixture
from appium import webdriver
from datetime import datetime
from os import path, makedirs
import os
from capabilities import *
import utils
import glob
from selenium.common.exceptions import ScreenshotException


ROOT_DIR = path.dirname(path.abspath(__file__))


@pytest.hookimpl(hookwrapper=True, )
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    test_fn = item.obj
    test = report.head_line
    test_name = test.partition('[')[0]
    extra = getattr(report, "extra", [])
    if report.when == "teardown":
        screen_files = glob.glob(f'screenshots/{test_name}*.png')
        if screen_files != []:
            extra.append(pytest_html.extras.image(screen_files[0]))
            report.extra = extra


def pytest_addoption(parser):
    parser.addoption('--device', action='store', default='phone',
                     help="phone or tablet")
    parser.addoption('--os', action='store', default='11')


@fixture()
def driver_no_reset(request):
    test_name = request.node.originalname
    device = request.config.getoption('device')
    version = request.config.getoption('os')
    if device == 'tablet':
        print(device)
        driver = webdriver.Remote('http://localhost:4723', android_no_reset(version))
    elif device == 'phone':
        print(device)
        driver = webdriver.Remote('http://localhost:4723',  android_no_reset(version))
    else:
        raise pytest.UsageError("phone or tablet")

    def kill_driver():
        scr_dir = path.join(ROOT_DIR, 'screenshots')
        if not path.exists(scr_dir):
            makedirs(scr_dir)
        file_name = f'{test_name}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
        try:
            driver.save_screenshot(path.join(scr_dir, file_name))
        except ScreenshotException:
            print('Не удалось сохранить скриншот')
        finally:
            driver.quit()

    request.addfinalizer(kill_driver)
    return driver


@fixture()
def driver_reset(request):
    test_name = request.node.originalname
    device = request.config.getoption('device')
    version = request.config.getoption('os')
    if device == 'tablet':
        print(device)
        driver = webdriver.Remote('http://localhost:4723', android_reset(version))
    elif device == 'phone':
        print(device)
        driver = webdriver.Remote('http://localhost:4723', android_reset(version))
    else:
        raise pytest.UsageError("phone or tablet")
    def kill_driver():
        scr_dir = path.join(ROOT_DIR, 'screenshots')
        if not path.exists(scr_dir):
            makedirs(scr_dir)
        file_name = f'{test_name}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::",
                                                                                                               "__")
        try:
            driver.save_screenshot(path.join(scr_dir, file_name))
        except ScreenshotException:
            print('Не удалось сохранить скриншот')
        finally:
            driver.quit()
    request.addfinalizer(kill_driver)
    return driver


def pytest_configure():
    screenshots = glob.glob(f'{ROOT_DIR}/screenshots/*')
    for f in screenshots:
        os.remove(f)
    reports = glob.glob(f'{ROOT_DIR}/*.zip')
    for r in reports:
        os.remove(r)
    files = glob.glob(f'{ROOT_DIR}/mitmproxy_data/*')
    for f in files:
        os.remove(f)


def pytest_sessionfinish(session, exitstatus):
    terminalreporter = session.config.pluginmanager.get_plugin('terminalreporter')
    report = {
        'tests_count': session.testscollected,
        'passed_tests': terminalreporter.stats.get('passed', []),
        'failed_tests': terminalreporter.stats.get('failed', []),
        'skipped_tests': terminalreporter.stats.get('skipped', []),
        'error_tests': terminalreporter.stats.get('error', []),
        'html_report': utils.get_zipfile_assets()
    }


def pytest_runtest_teardown(item, nextitem):
    files = glob.glob(f'{ROOT_DIR}/mitmproxy_data/*')
    for f in files:
        os.remove(f)