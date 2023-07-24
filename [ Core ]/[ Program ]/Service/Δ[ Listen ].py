import subprocess
import webbrowser
import os
from timeit import Timer

import win32clipboard
import tkinter
import tkinter.messagebox


win32clipboard.OpenClipboard()
data1 = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
os.chdir('C:\\Users\\Administrator\\Desktop')


#def trigger():
#Clipboard
    #Link
        # image: open
        # archive
        # youtube|twitch: metadata
        # bookmark > Text: URL

def clipboard():
    win32clipboard.OpenClipboard()
    data2 = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    if data2!=data1:
        data1 = data2
        #trigger()
        webbrowser.open(data2, new=2, autoraise=True)

while True:
    t = Timer('1', clipboard)
    t.start()
    t.join()
