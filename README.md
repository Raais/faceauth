# faceauth

faceauth uses [dlib](http://dlib.net)'s face recognition model which claims an [accuracy of 99.38%](https://github.com/davisking/dlib/blob/9f6aefc0db01e1d2edca666bb4d9dc76240b9074/python_examples/face_recognition.py#L16).

## Usage

When called, **[auth.py](https://github.com/Raais/faceauth/blob/main/auth.py)** will capture from the default camera (set in [.env](https://github.com/Raais/faceauth/blob/main/.env) as 0), validate and return a status code 0-5:

STATUS 0 = no match  
STATUS 1 = match  
STATUS 2 = timeout  
STATUS 3 = no source image  
STATUS 4 = no camera  
STATUS 5 = unclear source image [[r]](https://github.com/Raais/faceauth/blob/e46dd0458639ffc02bcc85b82ac0f038bc8384d0/auth.py#L26)

## Installation

### Requirements

  * Python 3.x
  * Linux
  
### Software Prerequisites

  * [face_recognition](https://github.com/ageitgey/face_recognition)
  
#### Clone this repo

```bash
git clone https://github.com/Raais/faceauth.git
```
  
#### Finally, install cv2, decouple:

```bash
pip3 install opencv-python python-decouple
```

### Create a face model first:

```bash
python3 test.py
```

Try **test.py** again to see if it matches.
