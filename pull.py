from os import times
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
from time import sleep
import cv2
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import threading
import pyttsx3


def thread_voice_alert(engine):
    engine.say("Motion")
    engine.runAndWait()

baseline_image=None
status_list=[None,None]
video=cv2.VideoCapture(0)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

while True:
    check, frame =  video.read()
    frame = cv2.resize(frame, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)
    status=0
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame=cv2.GaussianBlur(gray_frame,(25,25),0)

    if baseline_image is None:
        baseline_image=gray_frame
        continue

    delta=cv2.absdiff(baseline_image,gray_frame)
    threshold=cv2.threshold(delta,30,255,cv2.THRESH_BINARY)[1]
    (contours,_)=cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 800:
            continue
        status = 1
        
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
    status_list.append(status)

    if status_list[-1]==1 and status_list[-2]==0:
        t = threading.Thread(target=thread_voice_alert, args=(engine,))
        t.start()


    #cv2.imshow("gray_frame Frame",gray_frame)
    #cv2.imshow("Delta Frame",delta)
    #cv2.imshow("Threshold Frame",threshold)
    cv2.imshow("Color Frame",frame)

    key=cv2.waitKey(1)

    if key==ord('z'):
        if status==1:
            times.append(datetime.now())
        break




engine.stop()
video.release()
cv2.destroyAllWindows
