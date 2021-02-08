import face_recognition
import cv2
import sys
import time
from os import path
import os

video_capture = cv2.VideoCapture(0)

print("[add.py]")

if path.exists("source/source.jpg") == False:
    if input("No face model exists. Create one now? (y/n) ") != "y":
        exit()
else:
    print("source.jpg already exists. Exiting...")
    exit()

face_locations = []
face_encodings = []


def cap():
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    try:

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame)[0]
        #Searching for faces in frame

        #save if no exceptions
        print("Capturing image. Please stay still.")
        time.sleep(1.5)
        cv2.imwrite('source/source.jpg', frame)

    except IndexError:
        cap()

    video_capture.release()


cap()
exit()
