
from turtle import delay
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


status_list=[None,None]
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


# capturing video



song = AudioSegment.from_wav(r"C:\Users\Stanley\Desktop\alarm.wav")
def alarmSound():
    engine.say("Warning") 
    engine.runAndWait(0)

capture = cv2.VideoCapture(0)

while capture.isOpened():
    # to read frame by frame
    _, img_1 = capture.read()
    _, img_2 = capture.read()
    status = 0
    # find difference between two frames
    diff = cv2.absdiff(img_1, img_2)

    # to convert the frame to grayscale
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # apply some blur to smoothen the frame
    diff_blur = cv2.GaussianBlur(diff_gray, (5, 5), 0)

    # to get the binary image
    _, thresh_bin = cv2.threshold(diff_blur, 20, 255, cv2.THRESH_BINARY)

    # to find contours
    contours, hierarchy = cv2.findContours(thresh_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # to draw the bounding box when the motion is detected
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 300:
            status = 1
            cv2.rectangle(img_1, (x, y), (x+w, y+h), (0, 255, 0), 2)
    status_list.append(status)
        
            
          
    if status_list[-1]==1 and status_list[-2]==0:
        t = threading.Thread(target=alarmSound, args=(engine,))
        t.start()
               
     
    
    # cv2.drawContours(img_1, contours, -1, (0, 255, 0), 2)

    # display the output
    cv2.imshow("Front Door", img_1)
    if cv2.waitKey(100) == 13:
        exit()


    
engine.stop()
capture.release()
cv2.destroyAllWindows