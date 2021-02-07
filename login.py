import subprocess
import os

auth = subprocess.call(
    ["/usr/bin/python3", os.path.dirname(os.path.abspath(__file__)) + "/main.py"])

if auth == 1:
    # command to unlock session
    os.system("loginctl unlock-session")
    subprocess.call(["/usr/bin/bash", os.path.dirname(
        os.path.abspath(__file__)) + "/notify.sh"])
    exit()
else:
    exit()
