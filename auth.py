import face_recognition
import cv2
import os
from os import path
import sys
import subprocess
from datetime import datetime
from decouple import config

# opencv camera selector (.env)
cam = config('CAMERA')

# exit if no source file (create source file in add.py)
if path.exists("source/source.jpg") == False:
    sys.exit(3)

cn = int(cam)

video_capture = cv2.VideoCapture(cn)

try:
    baseimg = face_recognition.load_image_file("source/source.jpg")
    encoding = face_recognition.face_encodings(baseimg)[0]

except:
    # exit if no face/unclear face in source.jpg
    sys.exit(5)

fail = 0

def cap():
    # main face authentication function
    global fail

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
            sys.exit(1)
            # successful authorization
        else:
            # comment out next 3 to record non match face to dir fails/
            #now = datetime.now().time()
            #s = "fails/{}.png".format(now)
            #cv2.imwrite(s, frame)
            sys.exit(0)

    except IndexError:
        # indexerror denotes that no faces could be identified
        # not present, etc
        fail = fail + 1
        if fail >= 90:
            #90 fails = ~~5s .No faces found, exiting with status 2
            sys.exit(2)
        else:
            cap()  # start over if <90

    video_capture.release()  # end of function: camera closed/released


cap()

# STATUS 0 = not match
# STATUS 1 = match
# STATUS 2 = timeout
# STATUS 3 = no source file
# STATUS 4 = no camera
# STATUS 5 = base image fail
