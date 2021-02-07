from pynput import mouse
import time
import sys
import subprocess


def spawn(program, exit_code=2):
    subprocess.Popen(program)
    sys.exit(exit_code)


def on_move(x, y):
    # mouse movement event
    return False


def listen():
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()

    if listener == False:
        pass
    else:
        # if mouse moves, exit and call back login.py (main.py)
        spawn(["/usr/bin/python3", "./login.py"])


listen()
