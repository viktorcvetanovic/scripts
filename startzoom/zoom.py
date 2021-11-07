import json
import os
import sys
import time
import webbrowser
from abc import abstractmethod, ABC

import pyautogui


class Argument(ABC):
    def __init__(self, flag, value) -> None:
        super().__init__()
        self.flag = flag
        self.value = value

    def __repr__(self) -> str:
        return "Flag:" + self.flag + " " + "Value: " + self.value

    def __str__(self) -> str:
        return "Flag:" + self.flag + " " + "Value: " + self.value

    @abstractmethod
    def handle(self):
        pass


class StartZoom(Argument):

    def handle(self):
        pass


config_file = "config.json"
# windows...............
__location__ = os.path.join(sys.path[0], config_file)
args = sys.argv

mapped_arguments = []
declared_flags = {}


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


# windows only
def create_task():
    import datetime
    import win32com.client

    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')
    task_def = scheduler.NewTask(0)

    # Create trigger
    start_time = datetime.datetime.now() + datetime.timedelta(minutes=float(args[3]))
    TASK_TRIGGER_TIME = 1
    trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)
    trigger.StartBoundary = start_time.isoformat()

    # Create action
    TASK_ACTION_EXEC = 0
    action = task_def.Actions.Create(TASK_ACTION_EXEC)
    action.ID = 'zoom'
    action.Path = args[0]
    action.Arguments = "-s " + args[2]

    # Set parameters
    task_def.RegistrationInfo.Description = 'Task for starting zoom meetings'
    task_def.Settings.Enabled = True
    task_def.Settings.StopIfGoingOnBatteries = False

    # Register task
    # If task already exists, it will be updated
    TASK_CREATE_OR_UPDATE = 6
    TASK_LOGON_NONE = 0
    root_folder.RegisterTaskDefinition(
        'zoom starter',  # Task name
        task_def,
        TASK_CREATE_OR_UPDATE,
        '',  # No user
        '',  # No password
        TASK_LOGON_NONE)


def read_flags():
    for i in range(len(args)):
        if isFlag(args[i]):
            next = i + 1
            if next < len(args) and not isFlag(args[next]):
                mapped_arguments.append(Argument(args[i], args[next]))
            else:
                mapped_arguments.append(Argument(args[i], ""))


def isFlag(string: str):
    return string.startswith("-")


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
    elif definer == "-c" or definer == "--cron":
        create_task()
    elif definer == "-sw" or definer == "--startwrite":
        start_and_write()


data = load_json_config()
read_flags()
print(mapped_arguments)
# handle_input()
