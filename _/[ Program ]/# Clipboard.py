import subprocess
import webbrowser

import win32clipboard
import tkinter
import tkinter.messagebox


win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()


#Path
    #flip win32<>unix
#URL


win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(data)
win32clipboard.CloseClipboard()