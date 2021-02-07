import face_recognition
import cv2
import os
from os import path
import sys
import subprocess
from datetime import datetime
from decouple import config

# opencv camera selector (.env)
CAM = config('CAMERA')

# checking if base model exists
if path.exists("source/source.jpg") == False:
    if input("No face model exists. Create one now? (y/n)") != "y":
        exit()
    subprocess.call(
        ["/usr/bin/python3", os.path.dirname(os.path.abspath(__file__)) + "/add.py"])
    print("Success. Face model saved as ./source/source.jpg")
    exit()

cn = int(CAM)

video_capture = cv2.VideoCapture(cn)

baseimg = face_recognition.load_image_file("source/source.jpg")
encoding = face_recognition.face_encodings(baseimg)[0]

fail = 0
status = 0


def spawn(program, exit_code=2):
    subprocess.Popen(program)
    sys.exit(exit_code)


def cap():
    # main face authentication function
    global fail
    global status

    # exit if no camera exists
    if video_capture.read()[0] == False:
        sys.exit(4)
    else:
        # capture 1 frame from the camera
        ret, frame = video_capture.read()
    # downscaling for performance
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    try:
        face_encodings = face_recognition.face_encodings(rgb_small_frame)[0]

        results = face_recognition.compare_faces(
            [encoding], face_encodings)

        if results[0] == True:
            status = 1
            # successful authorization
        else:
            # if not match, take photo of intruder :D
            now = datetime.now().time()
            s = "fails/{}.png".format(now)
            cv2.imwrite(s, frame)
            #os.system("xdotool key Up")
            status = 0

    except IndexError:
        # indexerror denotes that no faces could be identified
        # not present, etc
        fail = fail + 1
        if fail >= 90:
            # if more than 90 fails / ~~5 seconds, exit main.py (close camera) and call mouse movement listener (for awaiting user interaction)
            spawn(["/usr/bin/python3", "./listener.py"])
        else:
            cap()  # start over if <90

    video_capture.release()  # end of function: camera closed/released


cap()
# Status code returns useful if you want to implement your own authentication system using faceauth
if status == 0:
    sys.exit(0)
elif status == 1:
    sys.exit(1)
elif status == 2:
    sys.exit(2)

# STATUS 0 = not match
# STATUS 1 = match
# STATUS 2 = timeout
# STATUS 3 = no source file
# STATUS 4 = no camera
# STATUS 12 = abort
