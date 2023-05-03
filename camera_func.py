import cv2
import datetime, time
import os, sys
from threading import Thread

class variables:
    capture = 0

global rec_frame

rec_frame = 0
camera = cv2.VideoCapture(0)

#Defines a path to storage taken photos
def generate_path():
    FOLD_NAME = "cam_captures"
    prog_path = os.getcwd()
    try:
        os.mkdir(os.path.join(prog_path, FOLD_NAME))
    
    except OSError as error:
       pass


def gen_frames():
    global out, rec_frame

    while True:
        success, frame = camera.read()
        if success:
            if (variables.capture):
                variables.capture = 0
                now = datetime.datetime.now()
                photo = os.path.sep.join(['instance/photos', "NewFace.jpg"])
                cv2.imwrite(photo, frame)
                photo = os.path.sep.join(['static/img', "NewFace.jpg"])
                cv2.imwrite(photo, frame)
            
            try:
                ret, buffer = cv2.imencode(".jpg", cv2.flip(frame, 1))
                frame = buffer.tobytes()
                yield(b'--frame\r\n'
                      b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass
        
        else:
            pass
