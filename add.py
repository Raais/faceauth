import face_recognition
import cv2
import numpy as np
import sys

video_capture = cv2.VideoCapture(0)

face_locations = []
face_encodings = []


def cap():
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    try:

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame)[0]

        cv2.imwrite('source/source.jpg', frame)

    except IndexError:
        cap()

    video_capture.release()


cap()
sys.exit(0)
