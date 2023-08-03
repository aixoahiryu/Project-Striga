import subprocess
import webbrowser

import win32clipboard
import tkinter
import tkinter.messagebox


win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

subprocess.Popen('C:\\Users\\Administrator\\AppData\\Local\\Chromium\\Application\\chrome.exe --disk-cache-size=0 --force-dark-mode --media-cache-size=0 --app="'+data+'"', start_new_session=True)