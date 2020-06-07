'''
import subprocess,os

def opencam():
 subprocess.run('start microsoft.windows.camera:', shell=True)
def closecam():
 subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)
'''