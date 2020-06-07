import pyttsx3
from tkinter import *

class speakclass:
 d=0
 def speakmethod(message):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[speakclass.d].id)
    engine.setProperty('rate',150)
    engine.say(message)
    engine.runAndWait()


 def check():
   x=speakclass.d
   if x==0:
      speakclass.d=1
   else:
      speakclass.d=0
   speakclass.speakmethod("hey")


#speakclass.check()

