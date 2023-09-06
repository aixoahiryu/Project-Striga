import Zeta
from Zeta.Image import Icon
from Zeta.Panel import *

import time
import os
import glob
import subprocess
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted
#import codecs


ZLCORE = os.environ['ZLCORE']
home = r'D:\MEGA\ZL-Core\Commit\╬'
#os.chdir(home)

cwd = os.getcwd()
fullpath = home
hidden = False

addicon = False
darkmode = True
tooltip = True
colorbg = "#000000" if darkmode else "#ffffff"
colorbg2 = "#253B34" if darkmode else "#6effbe"
colorfg = "#ffffff" if darkmode else "#000000"

sidebar = Tk()
sidebar.attributes('-topmost', True)
sidebar.attributes('-alpha', 0.1)
sidebar.title('1px')
sidebar.geometry("1x740+0+0")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)

sidebarext = Toplevel(sidebar)
sidebarext.attributes('-topmost', True)
sidebarext.attributes('-alpha', 0.1)
sidebarext.title('1ext')
sidebarext.geometry("1x710-0+30")
sidebarext.overrideredirect(1)
sidebarext.configure(bg=colorbg)
sidebarext.withdraw()

#root = Tk()
root = Toplevel(sidebar)
# root = Window(color2='white', mode='basic')
root.title('===[ Sidebar: File ]===')
root.attributes('-topmost', True)
root.attributes('-alpha', 0.77)
root.geometry("333x715+1+25")
root.overrideredirect(1)
#root.option_add("*tearOff", False)
#root.configure(background="#000000")
#root.configure(highlightbackground="#000000")
#root.configure(highlightcolor="white")

overflow = Toplevel(sidebar)
overflow.title('Icon overflow')
overflow.geometry("-0+25")
overflow.overrideredirect(1)
overflow.configure(bg=colorbg)
#overflow.transient(taskbar)
overflow.attributes('-topmost', True)
imggemini=Icon.Load(icon='geminiw', icontype='bw').image
Button(overflow, text=' Thaumiel', relief='flat', background=colorbg, foreground='#c9c9c9', image=imggemini, compound='left').grid(column=0, row=0, sticky='NW')
imgeye=Icon.Load(icon='eyew', icontype='bw').image
Button(overflow, text=' The eye', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgeye, compound='left').grid(column=0, row=1, sticky='NW')
imgmoon=Icon.Load(icon='moonw', icontype='bw').image
Button(overflow, text=' Moon cycle', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgmoon, compound='left').grid(column=0, row=2, sticky='NW')
imgsun=Icon.Load(icon='sunw', icontype='bw').image
Button(overflow, text=' Sun cycle', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgsun, compound='left').grid(column=0, row=3, sticky='NW')
imgdice=Icon.Load(icon='dicew', icontype='bw').image
Button(overflow, text=' Chaos theory', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgdice, compound='left').grid(column=0, row=4, sticky='NW')
imgcalendar=Icon.Load(icon='calendarw', icontype='bw').image
Button(overflow, text=' Calendar', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgcalendar, compound='left').grid(column=0, row=5, sticky='NW')
imghorse=Icon.Load(icon='horsew', icontype='bw').image
Button(overflow, text=' Strategy', relief='flat', background=colorbg, foreground='#c9c9c9', image=imghorse, compound='left').grid(column=0, row=6, sticky='NW')
imgwave=Icon.Load(icon='wave2w', icontype='bw').image
Button(overflow, text=' Flunctuation', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgwave, compound='left').grid(column=0, row=7, sticky='NW')
overflow.withdraw()
overflow_on = False

def toggle_overflow():
	global overflow_on
	if overflow_on: overflow.withdraw()
	else: overflow.deiconify()
	overflow_on = not overflow_on
taskbar = Toplevel(sidebar)
taskbar.attributes('-topmost', True)
taskbar.attributes('-alpha', 0.77)
taskbar.title('Taskbar')
taskbar.geometry("1366x25+1+0")
taskbar.overrideredirect(1)
#taskbar.configure(bg=colorbg, bd=1, relief='groove')
taskbar.configure(bg=colorbg)
Label(taskbar, text=r'[ Workspace ]', background=colorbg, foreground=colorfg).place(relx=0.48, rely=0)
appframe = Frame(taskbar, bg=colorbg)
appframe.grid(sticky='NSW', column=0, row=0)
#Button(appframe, text='1', relief='flat', background='#3c3c3c', foreground=colorfg).grid(column=0, row=0, sticky='NW')
Button(appframe, text='1', relief='flat', background=colorbg2, foreground='#6effbe').grid(column=0, row=0, sticky='NW')
Button(appframe, text='2', relief='flat', background=colorbg, foreground=colorfg).grid(column=1, row=0, sticky='NW')
Button(appframe, text='3', relief='flat', background=colorbg, foreground=colorfg).grid(column=2, row=0, sticky='NW')
Button(appframe, text='4', relief='flat', background=colorbg, foreground=colorfg).grid(column=3, row=0, sticky='NW')
Button(appframe, text='#', relief='flat', background=colorbg, foreground=colorfg).grid(column=4, row=0, sticky='NW')
imgcode=Icon.Load(icon='code', icontype='neon').image
Button(appframe, text=' Program', relief='flat', background=colorbg, foreground=colorfg, image=imgcode, compound='left').grid(column=5, row=0, sticky='NW')
imgterm=Icon.Load(icon='term3', icontype='neon').image
Button(appframe, text=' Hacking', relief='flat', background=colorbg, foreground=colorfg, image=imgterm, compound='left').grid(column=6, row=0, sticky='NW')
imgfile=Icon.Load(icon='file', icontype='neon').image
Button(appframe, text=' File', relief='flat', background=colorbg, foreground='#6effbe', image=imgfile, compound='left').grid(column=7, row=0, sticky='NW')
imglink=Icon.Load(icon='qr', icontype='neon').image
Button(appframe, text=' Network', relief='flat', background=colorbg, foreground=colorfg, image=imglink, compound='left').grid(column=8, row=0, sticky='NW')
trayframe = Frame(taskbar, bg=colorbg)
trayframe.grid(sticky='NSE', column=1, row=0)
taskbar.grid_columnconfigure(1, weight=1)
imgcpu=Icon.Load(icon='cpuw', icontype='bw').image
Button(trayframe, text=' 13%', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgcpu, compound='left').grid(column=0, row=0, sticky='NW')
imghdd=Icon.Load(icon='hddw', icontype='bw').image
Button(trayframe, text=' 322G', relief='flat', background=colorbg, foreground='#c9c9c9', image=imghdd, compound='left').grid(column=1, row=0, sticky='NW')
imgnetwork=Icon.Load(icon='networkw', icontype='bw').image
Button(trayframe, text=' 0.7 MB/s', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgnetwork, compound='left').grid(column=2, row=0, sticky='NW')
imgram=Icon.Load(icon='ramw', icontype='bw').image
Button(trayframe, text=' 2.2 GB', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgram, compound='left').grid(column=3, row=0, sticky='NW')
imgtemp=Icon.Load(icon='tempw', icontype='bw').image
Button(trayframe, text=' 33°C', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgtemp, compound='left').grid(column=4, row=0, sticky='NW')
imgvolume=Icon.Load(icon='volumew', icontype='bw').image
Button(trayframe, text=' Ballad', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgvolume, compound='left').grid(column=5, row=0, sticky='NW')
imgmenu=Icon.Load(icon='menuw', icontype='bw').image
btnoverflow = Button(trayframe, text='', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgmenu, compound='none')
btnoverflow.grid(column=6, row=0, sticky='NW')
btnoverflow.bind("<Button-1>", lambda event: toggle_overflow())
#taskbar.bind("<Button-1>", lambda event: (root.withdraw(), sidebar.geometry("1366x1+0+0"), taskbar.geometry("1366x24+0+1")))
taskbar.bind("<Button-1>", lambda event: root.withdraw())


titlepanel = Toplevel(sidebar)
titlepanel.attributes('-topmost', True)
titlepanel.attributes('-alpha', 0.77)
titlepanel.title('ASCII')
titlepanel.geometry("1366x740+1+25")
titlepanel.overrideredirect(1)
titlepanel.configure(bg=colorbg)
titlepanel.lower()
msg1=r''' __________________________________________________________
|[] Module                                           |F]|!"|
|""""""""""""""""""""""""""""""""""""""""""""""""""""""""|"|
| Left: file, search                                     | |
| Top: file, note, null                                  | |
| Right: dial, command, launch                           | |
|                                                        |_|
|________________________________________________________|/|


'''
msg2=r'''
|     .-.
|    /   \         .-.
|   /     \       /   \       .-.     .-.     _   _
+--/-------\-----/-----\-----/---\---/---\---/-\-/-\/\/---
| /         \   /       \   /     '-'     '-'
|/           '-'         '-'

'''
msg2_2=r''
msg3=r'''As above, so below. As within, so without.
Null and void, endless and finite, two become one.
If my delusion is so strong it can bend reality, is it really a delusion? I can die to set me free. Ego Sum Aeternae

		===[ Mercy - Justice - Vigilance ]===
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠄⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣤⡀⡄⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⣿⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢠⣱⢿⣿⡇⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣠⣿⣿⠁⢿⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠐⣼⣿⣿⣿⡀⡀⢿⣣⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠰⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢠⣴⣿⣿⣿⣿⠈⣼⣀⣾⣿⡆⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣠⣿⣿⣿⣿⠄⡀⡀⠁⠃⡀⠻⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⢣⣄⡀⢀⢀⡀⡀⡀⡀⡀⡀⡀⣷⣿⣿⣿⡿⠁⡀⡀⡀⡀⡀⡀⡀⢻⣰⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⣿⣿⠟⣿⣍⠿⣭⣴⣶⠇⣶⢄⡀⡀⡀⢀⣿⣿⣿⡟⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣷⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⠘⠂⡀⠈⠛⡀⠬⣄⠻⢶⣤⠁⠉⣩⢇⡀⡀⠈⣿⣿⣿⡿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡜⣝⣷⡀⢀⣀⡀⡀⡀⣀⣰⣶⠛⡀⡀⢀⠴⣷⡆⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⠺⢿⣿⠿⡐⠤⣀⠉⡛⣷⣾⣿⣿⠇⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢹⡌⣷⡙⣼⣿⣶⣿⡷⠃⢀⡤⣰⢿⡿⠋⡛⡀⡀⡀
⡀⡀⡀⡀⡀⡀⠐⣿⢀⠈⡀⠉⢿⣶⠒⡦⡀⣼⣿⣿⠟⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠈⡀⢹⣿⣿⣿⡾⠁⣤⠞⣥⣿⠛⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡟⢿⣷⠦⣀⡹⣿⣛⣲⠏⣿⠏⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠻⣿⣿⣾⣩⣶⠟⠁⡀⣀⣧⡟⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠛⣶⣿⣿⡀⣯⣾⠋⡀⡀⡀⡀⡀⡀⡀⡀⡀⠂⡀⡀⡀⡀⡀⡀⡀⡀⡀⠐⢻⣿⣿⣿⡀⢀⣴⣫⠖⠉⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢻⡿⠏⣾⠇⡀⡀⡀⡀⡀⡀⢀⡀⡀⡀⣀⣀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣼⣿⢿⣿⣛⠿⠋⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡞⣾⠃⡀⡀⡀⡀⡀⣠⣶⣶⣶⣶⡀⠉⢿⣧⠃⢙⡟⠳⠶⠘⡀⡀⠻⣿⠡⢿⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡞⣾⠃⡀⡀⢀⣠⣴⣿⣿⠿⠿⠌⡀⠒⢂⣶⡀⡀⡀⡇⣯⠙⠛⠶⣬⣟⡀⡀⡀⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡘⣾⠃⡀⣀⢀⣶⣿⣿⣿⡆⡄⡀⠜⣿⣿⣿⡿⡀⡀⢀⡏⣼⡀⡀⡀⢠⣉⠛⡀⡀⠈⡄⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢰⣿⠏⡀⢀⣰⣿⠟⣤⡀⡀⣾⡞⡀⠃⢉⣛⠿⡄⠈⢀⡞⠊⡞⡀⡀⡀⡾⠁⢰⡀⡀⡀⠹⡀⢀⡀⡀⠚⠋⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣠⣿⡟⡀⡀⡀⢭⡀⠘⣿⣇⣀⠈⢿⡷⣄⣀⠓⠐⣀⠶⠁⢞⠏⠁⡀⡀⠞⡁⡀⡀⡀⡀⡀⠈⠳⣀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⢠⣿⠏⡀⡀⡀⡀⡀⣤⡀⡀⠻⣿⣿⣤⠙⠿⠿⢿⣭⣯⡓⠋⣁⣠⢾⠟⠁⡀⠛⡀⡀⡀⡀⡀⠐⡀⢻⡗⡀⢰⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⢆⣿⡟⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠡⠉⠛⢀⣿⣿⡄⣰⣌⣍⣬⣉⠘⠁⡀⡀⡀⡀⡀⠆⡀⡀⡀⡀⠘⣿⣷⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⣿⡟⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⡀⡀⠈⢀⡀⠆⡀⡁⡀⠉⡀⡀⡀⡀⣤⡀⡀⡀⡀⣴⠟⠃⡀⡀⡀⡀⡀⡏⣿⣇⡆⡀⡀⡀⡀
⡀⡀⡀⡀⡀⣄⠘⣾⡿⡀⢀⠔⠉⡀⡀⡀⡀⡀⡀⡀⡀⡀⠄⡀⡀⡀⣆⢀⡀⠘⠁⡀⡀⡀⣁⡀⡀⣤⡾⠁⡀⡀⡀⡀⡀⣾⡏⢦⡀⣿⢸⡀⡀⡀⡀
⡀⡀⡀⢀⡀⡄⣿⣿⣤⠶⠂⠐⢶⣠⣤⣥⣴⣤⣶⣶⣿⣿⣿⣿⣄⣀⣤⡀⡀⢉⠂⣛⣾⣿⣡⣶⣦⣴⣶⣿⣦⡤⠁⣀⡀⢸⣿⢀⣦⢹⣿⢆⡀⡀⡀
⡀⡀⡀⡀⡀⢿⣿⣿⠿⠿⠿⠿⠛⠉⣉⠉⠈⠉⠈⠉⢹⢿⣿⠟⡉⠙⢹⡝⣯⠉⡀⠈⠉⡀⠐⣁⠟⠛⡿⠷⢼⣭⣿⢿⣧⣼⣇⣈⣿⣿⣿⣿⣦⡀⡀
⡀⡀⡀⡀⡀⠃⡀⡀⡀⡀⡀⡀⡀⠍⡀⡀⢡⡀⡀⡀⠈⣷⣿⡾⣸⡀⡞⠇⡀⡆⣠⣠⡀⡀⠆⡀⡀⡀⠈⡀⡀⡀⡀⠁⡀⡀⡀⡀⡀⣿⠈⣿⣿⡆⡀
⡀⡀⡀⡀⡀⡀⣀⠠⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⢠⢹⠃⡼⢷⠄⠃⣿⣇⣧⡀⠐⠆⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⡀⠟⣿⢇⡀
⡀⡀⡀⠚⠂⡀⡀⡀⡀⡀⡀⡀⡀⡀⠁⡀⡀⡀⠈⡀⡀⡀⣿⢀⡟⡄⣿⡄⡄⡀⣏⣾⣿⢷⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⠁⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢠⠉⠻⡟⡀⣿⣿⡀⡀⡷⣿⠙⠳⠁⡀⠸⡀⡀⠆⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠰⡀⡀⠠⠛⡷⠸⡛⡇⡀⡏⣿⡀⡀⡀⡀⣤⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡾⡀⡀⠋⢘⡄⡀⣇⠃⡀⣿⠋⡀⡀⣷⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠁⡀⡀⡀⡀⠰⠇⡀⣟⡀⡀⡿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀

┌─[ Monolith:13 ]─[ /dev/void ]                        ───────┐
|                                                             |
|                                                             |
|                                                             |
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
|                                                             |
|                                                             |
|                                                             |
└── ‡ breach --cluster #6effbe                         ───────┘
'''
txt1 = Frame(titlepanel, bg=colorbg)
txt1.grid(row=0, column=0, sticky='NW')
Message(txt1, text=msg1, width=444, bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal")).grid(row=0, column=0, sticky='NW')
txt2 = Message(titlepanel, text=msg2, width=444, bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal"))
txt2.grid(row=0, column=1, sticky='NEW')
txt3 = Message(titlepanel, text=msg3, width=444, bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal"))
txt3.grid(row=0, column=2, sticky='NE')
titlepanel.grid_columnconfigure(0, weight=1)
titlepanel.grid_columnconfigure(1, weight=1)
titlepanel.grid_columnconfigure(2, weight=1)
txt1frame = Frame(txt1, bg=colorbg)
txt1frame.grid(row=1, column=0, sticky='NW')
img1=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\geminiw.png')
Button(txt1frame, text=' Thaumiel', relief='flat', background=colorbg, foreground='#c9c9c9', image=img1, compound='left').grid(column=0, row=0, sticky='NW')

popup = Toplevel(sidebar)
popup.title('Popup')
popup.geometry("+10+350")
popup.overrideredirect(1)
popup.attributes('-alpha', 0.77)
popup.configure(bg=colorbg)
popup.attributes('-topmost', True)
popupmsg = Message(popup, text='[File] Workspace', bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal"), aspect=500)
popupmsg.grid(sticky='NWES')
popup.withdraw()

#root.tk.call("source", r"C:\Users\Administrator\Desktop\tcl\theme\Forest\void.tcl")
style = ttk.Style()
style.theme_use('alt')
style.configure("Treeview", background=colorbg, foreground=colorfg, fieldbackground=colorbg)
style.map('Treeview', background=[('selected', colorbg2)], foreground=[('selected', '#6effbe')])
style.configure("TCombobox", background=colorbg, foreground=colorfg, fieldbackground=colorbg, highlightcolor=colorfg, arrowcolor=colorfg)
style.map('TCombobox', background=[('readonly', colorbg)], foreground=[('readonly', colorfg)], fieldbackground=[('readonly', colorbg)], highlightcolor=[('readonly', colorfg)], arrowcolor=[('readonly', colorfg)] )
style.configure("TScrollbar", background=colorbg, foreground=colorfg, fieldbackground=colorbg, highlightcolor=colorfg, troughcolor=colorbg, arrowcolor=colorfg)
style.configure("Menu", background=colorbg, foreground=colorfg, fieldbackground=colorbg, highlightcolor=colorfg)


def preview_clipboard():
	try:
		global msg2_2
		#msg2_2 = msg2_2+root.clipboard_get()
		msg2_2 = msg2+r'┌─[ Clipboard:xclip ]─[ /dev/clipboard ]'+'\n'
		temp1 = root.clipboard_get().split('\n')
		for i in temp1[:10]:
			msg2_2 = msg2_2+r'| '+i[:55]+'\n'
		if len(temp1)<10:
			for i in range(0, (10-len(temp1))): msg2_2 = msg2_2+r'| '+'\n'
		msg2_2 = msg2_2+r'└── ‡ limit --head 10'
		txt2.configure(text=msg2_2)
		preview_file(File1.fullpath)
	except: #txt2.configure(text=msg2+'Clipboard failure')
		msg2_2 = msg2+r'┌─[ Clipboard:xclip ]─[ /dev/clipboard ]'+'\n'
		msg2_2 = msg2_2+r'| '+'Cliboard failure \n'
		for i in range(1, 10): msg2_2 = msg2_2+r'| '+'\n'
		msg2_2 = msg2_2+r'└── ‡ limit --head 10'
		txt2.configure(text=msg2_2)
		preview_file(File1.fullpath)

def preview_file(path):
	try:
		if os.path.isfile(path):
			msg2_3 = msg2_2+'\n\n'+r'┌─[File]─[ %s ]' % path[-44:] +'\n'
			file = open(path, mode='r', encoding='utf-8')
			filecontent = file.read(666)
			file.close()
			filecontent = filecontent.split("\n")
			for i in filecontent[:30]:
				i = i.replace("\t", "  ")
				msg2_3 = msg2_3+r'| '+i[:55]+'\n'
			if len(filecontent)<30:
				for i in range(0, (30-len(filecontent))): msg2_3 = msg2_3+r'| '+'\n'
			msg2_3 = msg2_3+r'└── ‡ limit --head 30'
			txt2.configure(text=msg2_3)
	except: txt2.configure(text=msg2_2+'Preview failure')

def toggle_sidebar(*event):
	global hidden, overflow_on
	
	if (hidden == False):
		root.withdraw()
		taskbar.withdraw()
		titlepanel.withdraw()
		sidebar.attributes('-alpha', 0.1)
		sidebarext.withdraw()
		#sidebar.geometry("1x690+0+50")
	else:
		root.deiconify()
		taskbar.deiconify()
		titlepanel.deiconify()
		sidebar.attributes('-alpha', 1.0)
		sidebarext.deiconify()
		#sidebar.geometry("1x740+0+0")
		popup.withdraw()
		preview_clipboard()
	
	if overflow_on:
		overflow.withdraw()
		overflow_on = False

	hidden = not hidden

def tooltip_show(x, y):
	#popup.deiconify() if hidden else print(e)
	if hidden:
		if (y<=50 and x==0): (popupmsg.configure(text='Network'),popup.geometry('+10+10'),popup.deiconify())
		elif x>=1: (popupmsg.configure(text='F'),popup.geometry('+10+10'),popup.deiconify())
		elif y>=700: (popupmsg.configure(text='Lounge'),popup.geometry('+10-40'),popup.deiconify())
		else: (popupmsg.configure(text='File'),popup.withdraw())

def tooltip_hide():
	popup.withdraw() if hidden else print('hidden')

#-------------------------------------------------------------------------------

class Controller():
	def toggle_sidebar(child): toggle_sidebar()
	def preview_file(child, path): preview_file(path)

File1 = FileBox(root, home=home, darkmode=True, controller=Controller())

#-------------------------------------------------------------------------------

sidebar.bind("<Button-1>", toggle_sidebar)
sidebarext.bind("<Button-1>", toggle_sidebar)

if tooltip:
	sidebar.bind("<Enter>", lambda e: tooltip_show(e.x, e.y))
	sidebar.bind("<Leave>", lambda e: tooltip_hide())
	sidebar.bind('<Motion>', lambda e: tooltip_show(e.x, e.y))
sidebar.mainloop()
