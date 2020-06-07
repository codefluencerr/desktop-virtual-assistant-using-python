import wikipedia
import wikipediaapi
import webbrowser
import tkinter
from tkinter import  *
import  os
from plyer import  notification
from speak import speakclass
import  time

class searchnet():
    def wikisearch(text):#searchkeylis=[tell, me, something ,about ,india]
        start_time = time.time()
        key=['what','who','is','tell','me','something','describe','give','some','details','about','when','was','wiki','wikipedia','the','according','to']
        searchkeylist=text.split()
        for x in searchkeylist:
            #print(x)
            if x in key:
                continue
            else:
                s=searchkeylist.index(x)
                searchkeylistnew=searchkeylist[s:]
                searchkey = ' '.join([str(elem) for elem in searchkeylistnew])
                break
        print(searchkey)
        #try:
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(searchkey)
        webbrowser.open(page_py.fullurl)
        x = (time.time() - start_time)
        notification.notify(title="Virtual assistant", message=" we found this in " + str(x) + "seconds", timeout=5)
        result = wikipedia.summary(searchkey, sentences=2)
        #print(result)
        #notification.notify(title="Virtual as
        # sistant", message=" we found this", timeout=5)
        writeresults=wikipedia.page(searchkey).content
        handle=open('scratch.txt',mode='w',encoding='utf-8')
        handle.write(writeresults)
        handle.close()
        root=Tk()
        buttoncopy=Button(root,text='copy results',command=lambda :os.startfile('scratch.txt'))
        speakclass.speakmethod(result)
        buttoncopy.pack()
        root.mainloop()

    def googlesearch(text):
            print("HERE ARE RESULTS FOR ", text)
            st = "https://www.google.com/search?q={}".format(text)
            webbrowser.open(st)
            notification.notify(title="Virtual assistant", message=" we found some results", timeout=5)
            speakclass.speakmethod("according to google")

searchnet.wikisearch("according to wikipedia who is india")

