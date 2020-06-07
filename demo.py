#after login this window appears
from tkinter import  *
from PIL import ImageTk ,Image
from speak import speakclass
import tkinter.font as font
import subprocess,os
import wikipedia
import speech_recognition as sr
from weather_info import weatherinfoclass
from loghistory import inserthistory
from openfile import searchfiles
import webbrowser
import  sys
from openbrowser import browserclass
import time
from plyer import notification
import wikipediaapi
from searchfile import searchnet
import  psycopg2
from tkinter import ttk
import sqlite3



class mscreenclass():
    #load the history in the drop down list
    def loadhistory(a):
        conn = sqlite3.connect('historydb.sqlite')
        cur = conn.cursor()
        if a == 0:
            speakclass.speakmethod("deleting history")
            cur.execute("delete from history")
            notification.notify(title="Virtual assistant", message="history cleared", timeout=5)
            cur.close()
            conn.commit()
        else:

            cur.execute("SELECT d from history")
            row = cur.fetchall()
            cur.close()
            conn.commit()
            new_lst = row[::-1]
            return new_lst


    #gui designing for mainscreen
    def mscreenmethod(welcome):
        global img
        print(welcome)
        #speakclass.speakmethod(welcome)
        root=Tk()
        root.title('Your assistant')
        root.configure(bg='#BCD5E5')
        root.geometry('350x490')
        #img=ImageTk.PhotoImage(Image.open ("initial.jpg"))
        #lab=Label(image=img)

        photo0 = ImageTk.PhotoImage(Image.open ("initial.jpg"))
        buttona = Button(root, image=photo0,command=lambda :speakclass.check())

        lspace3=Label(text="              ",bg='#BCD5E5')
        lspace4 = Label(text="              ",bg='#BCD5E5')
        lspace5 = Label(text="              ",bg='#BCD5E5')
        lspace6 = Label(text="              ",bg='#BCD5E5')
        text1=Label(root,text="What's in your mind",bg='#BCD5E5')
        ###searchentry=Entry(root,width=35)
        searchentry = ttk.Combobox(root,postcommand=lambda: searchentry.configure(values=mscreenclass.loadhistory(1)))
        searchentry.current()
        myFont = font.Font(family='Courier', size=10, weight='bold')

        cbutton = Button(root, text="CLEAR",bg='#BCC6CE',padx=10,pady=10, command=lambda: mscreenclass.loadhistory(0))
        cbutton['font']=myFont

        searchbutton=Button(root,text="GO",bg='#BCC6CE',padx=10,pady=10,command=lambda :searchclass.searhfromtext(searchentry))
        searchbutton['font'] = myFont

        photo = PhotoImage(file=r"voice1.png")

        playbutton=Button(root,image=photo,command=lambda:searchclass.audiototext(searchentry) )
        buttonguide=Button(root,text="GUIDE",bg='#BCC6CE',padx=10,pady=10,command=lambda :os.startfile('guide.png'))
        buttonguide['font']=myFont

        photo1 = PhotoImage(file=r"scratch.png")
        buttonscratch = Button(root, image=photo1, command=lambda: os.startfile('scratch.txt'))

        #arranging  the components in the window using grid
        buttona.grid(row=0,column=1)
        lspace3.grid(row=1,column=1)
        text1.grid(row=2,column=1)
        lspace4.grid(row=3,column=0)
        #searchentry.grid(row=4,column=1)
        searchentry.grid(row=4, column=1)
        lspace5.grid(row=5,column=0)
        searchbutton.grid(row=6,column=1)
        cbutton.grid(column=2, row=6)
        lspace6.grid(row=7,column=0)
        playbutton.grid(row=4,column=2)
        buttonguide.grid(row=9,column=1)
        buttonscratch.grid(row=9,column=2)
        root.mainloop()



class searchclass:
  #called when user commands from by writing the command
  def searhfromtext(searchentry):
      search_text=searchentry.get()
      print(search_text)
      speakclass.speakmethod("hold on I'm getting the results")
      searchclass.searchmethod(search_text)
  #called when user commands by speech
  def audiototext(searchentry):
        searchentry.delete(0,END)
        speakclass.speakmethod("What can i do for you ")
        print("LISTENING :")
        r=sr.Recognizer()
        mic=sr.Microphone(device_index=1)
        with mic as source:
            #store audio from mic in var audio
            audio=r.listen(source)
        try:
         #call method for text recogniton in  speech
         search_text=r.recognize_google(audio)
         searchentry.insert(0,search_text)
         print(search_text)
        except:
          speakclass.speakmethod("sorry i didnt get you")
          print("error")
        speakclass.speakmethod("hold on I'm getting the results")
        searchclass.searchmethod(search_text)
  
  #perform the action associated with the command
  def searchmethod(search_text):
        inserthistory(search_text)#log the commands to store history
        if('weather' in search_text):
            l=search_text.split()
            city=l[-1]
            result=weatherinfoclass.weathermethod(city)#weather API
            st = "https://www.google.com/search?q={}".format(search_text)
            webbrowser.open(st)
            notification.notify(title="Virtual assistant", message=" we found some results", timeout=5)
            speakclass.speakmethod(result)

            #searchclass.displayres(result)
        elif('camera'  in search_text):
            speakclass.speakmethod('opening camera')
            subprocess.run('start microsoft.windows.camera:', shell=True)
            notification.notify(title="Virtual assistant", message="Camera opened", timeout=5)
        elif('file' in search_text):
           l = search_text.split()
           file_name = l[-1]
           print(file_name)
           s="searching for the file"+file_name
           speakclass.speakmethod(s)
           print(file_name)
           try:
            result="path is "+ searchfiles(file_name)
           except:
            notification.notify(title="Virtual assistant", message="SORRY FILE NOT FOUND ", timeout=5)
            speakclass.speakmethod('file not found')
           notification.notify(title="Virtual assistant", message="file opened succesfully "  +result, timeout=5)
           speakclass.speakmethod(file_name+"opened successfully")

        elif("bye" in search_text):
            speakclass.speakmethod(" Bye take care")
            sys.exit()

        elif ('open' in search_text):
            l=search_text.split()
            p=l[1].lower()
            browserclass.browsermethod(p)
            notification.notify(title="Virtual assistant", message=p+" opened succesfully",timeout=5)

        elif("entertain" in search_text):
            webbrowser.open('www.youtube.com/feed/trending')

        #for google search results
        elif ('google'in search_text or 'Google' in search_text):
            res = search_text.split(' ', 1)[1]
            searchnet.googlesearch(res)

        else:#uses wikipedia
            searchnet.wikisearch(search_text)


