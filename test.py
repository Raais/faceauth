import subprocess
import os

code = subprocess.call(
    ["/usr/bin/python3", os.path.dirname(os.path.abspath(__file__)) + "/main.py"])

if code == 0:
    print("DENIED")
elif code == 1:
    print("MATCH")
elif code == 2:
    print("TIMEOUT")
elif code == 3:
    print("NO SOURCE FILE")
elif code == 4:
    print("NO CAMERA")
elif code == 12:
    print("ABORTED")

# STATUS 0 = not match
# STATUS 1 = match
# STATUS 2 = timeout
# STATUS 3 = no source file
# STATUS 4 = no camera
# STATUS 12 = abort
