import random
import string
import math
from selenium.webdriver.remote.webelement import WebElement
import datetime
import json
import requests
import time
import os
import zipfile
import glob
from appium.webdriver.webdriver import WebDriver

ROOTDIR = os.path.dirname(os.path.abspath(__file__))



def random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))


def random_numbers(length):
    return ''.join(random.choices(string.digits, k=length))


def get_html_file():
    html = [f for f in os.listdir(ROOTDIR) if f.endswith('.html')][0]
    return html

def get_screenshots():
    screens = [f for f in os.listdir(f'{ROOTDIR}/screenshots') if f.endswith('.png')]
    return screens

def get_zipfile_assets():
    # screens = get_screenshots()
    zip_name = f'report_{datetime.datetime.today().strftime("%Y-%m-%d_%H:%M")}.zip'
    zf = zipfile.ZipFile(zip_name, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9)

    for dirname, subdirs, files in os.walk(f"{ROOTDIR}/screenshots"):
        # zf.write(dirname)
        for filename in files:
            zf.write(os.path.relpath(os.path.join(dirname, filename)))

    zf.write(get_html_file())
    zf_path = f'{ROOTDIR}/{zip_name}'
    return zf_path


def get_start_coordinats_of_element(element: WebElement):
    start = element.location
    start_x = start['x']
    start_y = start['y']
    return {'x': start_x, 'y': start_y}


def get_center_of_element(element: WebElement):
    start = element.location
    size = element.size
    center_x = start['x'] + (size['width'] - start['x']) / 2
    center_y = start['y'] + (size['height'] / 2)
    print(start, size)
    return {'x': center_x, 'y': center_y}


def get_x_coordinate_to_swipe_up(driver: WebDriver):
    screen_size = driver.get_window_size()
    stop_x = int(screen_size['width'] * 0.21)
    start_x = int(screen_size['width'] - stop_x)
    return {'start_x': start_x, 'stop_x': stop_x}


def get_response_value_from_mitm(url):
    counter = 0
    file_path = f'{ROOTDIR}/mitmproxy_data/{url}.json'
    while not glob.glob(file_path):
        time.sleep(1)
        counter += 1
        if counter > 10:
            break
    try:
        response_file = glob.glob(file_path)[0]
        with open(response_file) as f:
            jsonObject = json.load(f)
            f.close()
        return jsonObject
    except BaseException:

        print('не нашел файл')
        return []


def get_image_from_url(url):
    img_data = requests.get(url).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)


def convert_ms_to_min(ms: int):
    duration_min = math.floor(ms / 60000)
    if duration_min > 59:
        return f'{duration_min//60} ч {duration_min%60} мин'
    else:
        return duration_min


def convert_ms_to_min_sec(ms: float):
    seconds = (ms / 1000) % 60
    seconds = round(int(seconds), 2)
    minutes = (ms / (1000 * 60)) % 60
    minutes = round(int(minutes), 2)
    hours = round(((ms / (1000 * 60 * 60)) % 24))
    min_str = f'{minutes}' if minutes >= 10 else f'0{minutes}'
    sec_str = f'{seconds}' if seconds >= 10 else f'0{seconds}'
    return f'{min_str}:{sec_str}' if hours > 0 else f'{hours}:{min_str}:{sec_str}'


def get_current_date():
    return datetime.datetime.today()


def convert_string_to_time(time_str: str):
    time_ = datetime.datetime.strptime(time_str, '%H:%M:%S')
    return time_


def get_new_time(current_time, secs_to_add):
    new_time = current_time + datetime.timedelta(seconds=secs_to_add)
    return new_time.strftime('%M:%S')


def get_new_date(days):
    delta = datetime.timedelta(days=days)
    new_date = get_current_date() + delta
    return new_date.strftime('%d.%m.%Y')

