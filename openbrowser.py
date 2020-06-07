#opens the desired webpage in the default browser by reading the file and matching the text
#view browsermap.txt
import webbrowser
from speak import speakclass

class browserclass():
    x="google"
    def browsermethod(text):
        x=text.lower()
        handle=open('browsermap.txt',mode='r',encoding="utf-8")
        for line in handle:
           if line.startswith(x):
               l=line.split(':')
               speakclass.speakmethod("OPENING "+l[0])
               webbrowser.open(l[1])

    def browse(text):
        st="https://www.google.com/search?q={}".format(text)
        webbrowser.open(st)
#browserclass.browsermethod("google")
#browserclass.browse("what is android")