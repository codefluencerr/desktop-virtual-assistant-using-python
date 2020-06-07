
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk ,Image
import psycopg2
from speak import  speakclass
from demo import mscreenclass
import tkinter.font as font
import time
from plyer import notification
import os


class access:
    def checktime():#to greet the user.examlple->good morning,etc
        timestamp = time.strftime('%H')
        if int(timestamp) <12:
            return ("goood morning")
        elif int(timestamp) >= 12 and int(timestamp) < 16:
            return("good afternoon")
        elif int(timestamp) > 16 and int(timestamp) < 20:
            return("good evening")
        else:
            return("goog night")

    def login(us1):
        us = us1.get()
        #us='Testing'
        root.destroy()
        print("SUCCESFULLY LOGGED IN")
        welcome = "hey " + us + " I'm Your assistant , how can I help you?"
        notification.notify(title="Virtual assistant", message=access.checktime()+" "+us+" ,how can i help you",
                                        timeout=5)
        os.startfile('guide.png')
        mscreenclass.mscreenmethod(welcome)

#GUI
root = Tk()
root.title('VIRTUAL ASSISTANT')
root.geometry('250x390')
img=ImageTk.PhotoImage(Image.open ("1.png"))
lab=Label(image=img)
lab.grid(row=0,column=2,columnspan=3)
img1=ImageTk.PhotoImage(Image.open ("u2.png"))
lab=Label(image=img1)
lab.grid(row=2,column=2)
space0=Label(root,text=" ")
space0.grid(row=1,column=1)
loginentryuser=Entry(root)
space=Label(root,text="")
loginentryuser.grid(row=2,column=3)
space.grid(row=2,column=0,columnspan=2)
space1=Label(root,text=" ")
myFont = font.Font(family='Courier', size=10, weight='bold')
#on clicking on button login and signup methods login and signup will be called from loginscreen module
lbutton=Button(root,text='LOGIN',bg='#A9CCE3',padx=10,pady=10,command=lambda :access.login(loginentryuser))
lbutton['font'] = myFont
lbutton['font'] = myFont
space1.grid(row=5,column=1)
lbutton.grid(row=6,column=2)
root.mainloop()









