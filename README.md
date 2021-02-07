# faceauth

Unlock sessions and authenticate sudo prompts using face recognition.

faceauth was made as an alternative to [howdy](https://github.com/boltgolt/howdy) for those who don't have a [camera with an IR emitter](https://github.com/boltgolt/howdy/wiki/Cameras-that-have-been-verified-to-work-with-Howdy). It is therefore likely to be less secure. In fact it is advised to only use faceauth for purposes of convenience (for personal use) and never for security. As a simple picture of yourself could be used to gain access to your system.

However, faceauth uses ageitgey's [face_recognition](https://github.com/ageitgey/face_recognition) API which claims a [99.38% accuracy model](https://github.com/ageitgey/face_recognition#face-recognition) and I personally haven't seen a noticeable performance difference between Howdy and faceauth.

## Features

#### Session Unlocking

A monitoring process launches the program when the system goes into a locked state. If your camera/webcam has an LED, it will turn active indicating that the program is searching for faces. If the program cannot find a face within 5 seconds, it will go idle and await user interaction (through the mouse). When a mouse movement event is triggered, the camera will become active again.

The [monitoring pipeline](https://github.com/Raais/faceauth/blob/main/faceauth.sh) and the session unlock command is configured for Manjaro KDE; and should work for Gnome and other DEs with minimal tinkering.

#### PAM

The [PAM module](https://github.com/Raais/faceauth/blob/main/PAM-example/base_dir/pam.py) is not functional and is included as an example. ( i couldnt get it to work :D )

#### Sudo Authentication without PAM (Not Recommended)

This module is extremely unsecure as you have to locally save your password in an env. Which is why it is seperated from the main faceauth script. After launching the sudoer script, you can press L_Ctrl + Tab by default to launch a faceauth authentication. If successful, it will send the keystrokes to the terminal and hit enter. Automating the authentication for you.



## Installation

### Requirements

  * Python 3x
  * Linux
  
### Software Prerequisites

  * [face_recognition](https://github.com/ageitgey/face_recognition)
  * xdotool (optional, for sudo module)
  
Finally, install cv2, numpy, pynput, python-decouple:

```bash
pip3 install cv2 numpy pynput python-decouple
```

## Running

**[faceauth.sh](https://github.com/Raais/faceauth/blob/main/faceauth.sh)** is the main process that handles monitoring and launching.

Make sure [faceauth.sh](https://github.com/Raais/faceauth/blob/main/faceauth.sh) and [unlock.sh](https://github.com/Raais/faceauth/blob/main/unlock.sh) are properly configured for your desktop environment. Ignore this step if you use KDE Plasma.


If you just want to test out faceauth,

```bash
python3 test.py
```
and you will be prompted to create a face model the first time. If not the program will attempt to verify your face.
