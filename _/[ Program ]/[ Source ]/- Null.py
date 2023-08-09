import subprocess
import webbrowser
import os

import win32clipboard
import tkinter
import tkinter.messagebox


win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
os.chdir('C:\\Users\\Administrator\\Desktop')

exit()

data=data.replace('sample_','')
data2='https://hypnohub.net/index.php?page=post&s=list&tags=md5%3a'
#data2='https://hypnohub.net/index.php?page=post&s=view&id='


#subprocess.Popen(["C:\Program Files\Links\links-g.exe", data], start_new_session=True)
#webbrowser.open(data, new=2, autoraise=True)
webbrowser.open(data2+data, new=2, autoraise=True)
