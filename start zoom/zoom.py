import json
import os
import sys
import time
import webbrowser

import pyautogui

config_file = "config.json"
# windows...............
__location__ = os.path.join(sys.path[0], config_file)
args = sys.argv


def add_link():
    if args[2] is None or args[3] is None:
        raise ValueError("You need to define key and value to add a link")
    data[args[2]] = args[3]
    with open(__location__, 'w') as f:
        json.dump(data, f)


def remove_link():
    if args[2] is None:
        raise ValueError("You need to define key and value to add a link")
    del data[args[2]]
    with open(__location__, 'w') as f:
        json.dump(data, f)


def load_json_config():
    try:
        with open(__location__, 'r') as f:
            return json.load(f)
    except EnvironmentError:
        raise FileNotFoundError("Please add config.json in this path: " + __location__)


def start_zoom():
    try:
        webbrowser.open(data[args[2]], new=0, autoraise=True)
    except Exception:
        raise ValueError("You have not definied that link !!! " +
                         "\n Link name: " + args[2] +
                         "\n Check your config.json or use -a function")


def start_and_write():
    start_zoom()
    if args[3] is None:
        raise ValueError("Please enter your name")
    time.sleep(10)
    if os.name == "nt":
        import pygetwindow as gw
        handle = gw.getWindowsWithTitle('Zoom Meeting')[0]
        handle.activate()
        handle.maximize()
    pyautogui.hotkey('alt', 'h')
    for char in args[3]:
        pyautogui.press(char)
    pyautogui.press("enter")


def print_help():
    return None


def print_config():
    if len(args) >= 3:
        try:
            return print(data[args[2]])
        except Exception:
            raise ValueError("Config file does not contains that key")
    return print(data)


def handle_input():
    definer = args[1]
    if definer == "-s" or definer == "--start":
        start_zoom()
    elif definer == "-a" or definer == "--add":
        add_link()
    elif definer == "-d" or definer == "--delete":
        remove_link()
    elif definer == "-r" or definer == "--read":
        print_config()
    elif definer == "-h" or definer == "--help":
        raise ValueError("Not implemented")
    elif definer == "-sw" or definer == "--startwrite":
        start_and_write()


data = load_json_config()

handle_input()
