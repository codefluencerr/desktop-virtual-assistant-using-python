#to find and open the desired file or folder
#for better perfomances we ignore the cases of the strings during comparison
import  os
from speak import speakclass
dirr="D:"
x="dummy"
smallfile=[]#list for files
smalldirs=[]#list for directories/parent folders
def searchfiles(file):
    x= file.lower()#we convert the filename passed in this function to lower case
    for root,dirs,files in os.walk(dirr):
        #print(root)-->the current folder
        #print(files)-->the list of files in the folder
        #print(dirs)--->the directories in the folder

        #to convert the name of directories to lower case and append them in  the new list smalldirs
        for y in dirs:
            small=y.lower()
            smalldirs.append(small)
        #check for the desired directory and open it
        if x in smalldirs:
            path = os.path.join(root, file)
            print(path)
            os.startfile(path)
            return path

        # to convert the name of file to lower case and append them in  the new list smallfile
        for y in files:
            small=y.lower()
            smallfile.append(small)

        # check for the desired file and open it
        if x in smallfile:
            path=os.path.join(root, file)
            print(path)
            os.startfile(path)
            return path

#while True:
#    d=input("enter filename:")
#    s=searchfiles(d)
#    #print(s)













