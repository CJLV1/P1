from email.mime import application
from os import stat
from tkinter.tix import MAIN
import pyttsx3
import time
import math
import pydub
import threading
from AppOpener import run
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)



tz=time.timezone
status = 0 #MODE
greet=0
longtime=time.time()
curr=time.ctime(longtime)
print("\nComputer found: " , longtime)
time.sleep(2)
print("Local time: ", curr + "\n\n")

def start_up():
    print("Good to see you again, sir.\n\n")
    engine.say("Good to see you again, sir.")
    engine.runAndWait()
    time.sleep(3)
    while True:
        print("What should we do from here?\n")
        engine.say("What should we do from here?")
        engine.runAndWait()
        p=input()
        p=p.upper()

        if("WORK" in p) or ("WORKPLACE" in p) or ("CODE" in p):
            print("Yessir.\n")
            engine.say("Yessir.")
            engine.runAndWait()
            status=1
            time.sleep(1)
            print(status)
            break    
        else:
            print("Not sure I understand, sir.\n")


def workplace():
    print("Preparing your in house programming environment for you now, sir.\n")
    time.sleep(1)
    run("Visual Studio Code")
    time.sleep(0.5)
    run("Spotify")
    run("Google Chrome")
    print("I am running core applications for the work environmen now.\n")
    time.sleep(1.5)
    while True:
        print("Is there anything else you might want opened?\n")
        p=input()
        p=p.upper
        print(p)
        
        if("NO" in p ) or ("NOPE" in p):
            print("Goood luck, sir.\n")
            continue
        elif("COMMAND PROMPT" in p) or ("CMD" in p):
            print("Opening...\n")
            run("Command Prompt")
        elif("DISCORD" in p):
            print("Opening...\n")
            run("DISCORD")



start_up()


        
print(status)





    
 






