import subprocess
import os
import time

code = subprocess.call(
    ["/usr/bin/python3", os.path.dirname(os.path.abspath(__file__)) + "/auth.py"])

if code == 0:
    print("DENIED")
elif code == 1:
    print("MATCH")
elif code == 2:
    print("TIMEOUT")
elif code == 3:
    print("NO SOURCE FILE")
    print("Calling add.py")
    time.sleep(0.5)
    subprocess.call(
        ["/usr/bin/python3", os.path.dirname(os.path.abspath(__file__)) + "/add.py"])
    exit()
elif code == 4:
    print("NO CAMERA")
elif code == 5:
    print("BASE IMAGE FAIL. PLEASE DELETE SOURCE/SOURCE.JPG AND CREATE A NEW ONE WITH ADD.PY")

# STATUS 0 = not match
# STATUS 1 = match
# STATUS 2 = timeout
# STATUS 3 = no source file
# STATUS 4 = no camera
# STATUS 5 = base image fail
