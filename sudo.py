from pynput import keyboard
from decouple import config
import subprocess
import time
import sys
import os

# This is a simple example of what can be implemented using faceauth. When you are being prompted to enter your sudo password at a terminal
# L CTRL + TAB and faceauth will authenticate and enter the password for you.

# use at your own risk
pswd = config('PASSWORD')

strg = str(pswd)

# L CTRL + TAB to call faceauth-sudo
COMBINATION = {keyboard.Key.ctrl_l, keyboard.Key.tab}

current = set()


def auth():
    # get face authorization from main
    get = subprocess.call(
        ["/usr/bin/python3", os.path.dirname(os.path.abspath(__file__)) + "/main.py"])

    if get == 1:
        # success: type password in terminal and hit enter
        type()
    else:
        return


def pasw():
    for ch in strg:
        subprocess.call(["xdotool", "type", "--delay", "100", ch])


def type():
    time.sleep(0.2)
    pasw()
    time.sleep(0.1)
    subprocess.call(["xdotool", "key", "Return"])


def on_press(key):
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            auth()


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
