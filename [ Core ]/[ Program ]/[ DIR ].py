import subprocess
import webbrowser

import win32clipboard
import tkinter
import tkinter.messagebox


win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

subprocess.Popen(['C:\Program Files\Sublime Text 3\sublime_text.exe', data], start_new_session=True)