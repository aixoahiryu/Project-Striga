import time
import os
import glob
import subprocess
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted
#import codecs


ZLCORE = os.environ['ZLCORE']
home = r'D:\Scraps\╬'
os.chdir(home)

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
sidebarext.geometry("250x1+1+0")
sidebarext.overrideredirect(1)
sidebarext.configure(bg=colorbg)

#root = Tk()
root = Toplevel(sidebar)
root.title('===[ Sidebar: File ]===')
root.attributes('-topmost', True)
root.geometry("333x715+1+25")
root.overrideredirect(1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)
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
imggemini=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\geminiw.png')
Button(overflow, text=' Thaumiel', relief='flat', background=colorbg, foreground='#c9c9c9', image=imggemini, compound='left').grid(column=0, row=0, sticky='NW')
imgeye=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\eyew.png')
Button(overflow, text=' The eye', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgeye, compound='left').grid(column=0, row=1, sticky='NW')
imgmoon=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\moonw.png')
Button(overflow, text=' Moon cycle', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgmoon, compound='left').grid(column=0, row=2, sticky='NW')
imgsun=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\sunw.png')
Button(overflow, text=' Sun cycle', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgsun, compound='left').grid(column=0, row=3, sticky='NW')
imgdice=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\dicew.png')
Button(overflow, text=' Chaos theory', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgdice, compound='left').grid(column=0, row=4, sticky='NW')
imgcalendar=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\calendarw.png')
Button(overflow, text=' Calendar', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgcalendar, compound='left').grid(column=0, row=5, sticky='NW')
imghorse=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\horsew.png')
Button(overflow, text=' Strategy', relief='flat', background=colorbg, foreground='#c9c9c9', image=imghorse, compound='left').grid(column=0, row=6, sticky='NW')
imgwave=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\wave2w.png')
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
imgcode=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\neon\code.gif')
Button(appframe, text=' Program', relief='flat', background=colorbg, foreground=colorfg, image=imgcode, compound='left').grid(column=5, row=0, sticky='NW')
imgterm=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\neon\term3.gif')
Button(appframe, text=' Hacking', relief='flat', background=colorbg, foreground=colorfg, image=imgterm, compound='left').grid(column=6, row=0, sticky='NW')
imgfile=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\neon\file.gif')
Button(appframe, text=' File', relief='flat', background=colorbg, foreground='#6effbe', image=imgfile, compound='left').grid(column=7, row=0, sticky='NW')
imglink=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\neon\qr.gif')
Button(appframe, text=' Network', relief='flat', background=colorbg, foreground=colorfg, image=imglink, compound='left').grid(column=8, row=0, sticky='NW')
trayframe = Frame(taskbar, bg=colorbg)
trayframe.grid(sticky='NSE', column=1, row=0)
taskbar.grid_columnconfigure(1, weight=1)
imgcpu=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\cpuw.png')
Button(trayframe, text=' 13%', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgcpu, compound='left').grid(column=0, row=0, sticky='NW')
imghdd=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\hddw.png')
Button(trayframe, text=' 322G', relief='flat', background=colorbg, foreground='#c9c9c9', image=imghdd, compound='left').grid(column=1, row=0, sticky='NW')
imgnetwork=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\networkw.png')
Button(trayframe, text=' 0.7 MB/s', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgnetwork, compound='left').grid(column=2, row=0, sticky='NW')
imgram=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\ramw.png')
Button(trayframe, text=' 2.2 GB', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgram, compound='left').grid(column=3, row=0, sticky='NW')
imgtemp=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\tempw.png')
Button(trayframe, text=' 33°C', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgtemp, compound='left').grid(column=4, row=0, sticky='NW')
imgvolume=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\volumew.png')
Button(trayframe, text=' Ballad', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgvolume, compound='left').grid(column=5, row=0, sticky='NW')
imgmenu=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\menuw.png')
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
		preview_file()
	except: #txt2.configure(text=msg2+'Clipboard failure')
		msg2_2 = msg2+r'┌─[ Clipboard:xclip ]─[ /dev/clipboard ]'+'\n'
		msg2_2 = msg2_2+r'| '+'Cliboard failure \n'
		for i in range(1, 10): msg2_2 = msg2_2+r'| '+'\n'
		msg2_2 = msg2_2+r'└── ‡ limit --head 10'
		txt2.configure(text=msg2_2)
		preview_file()

def preview_file():
	try:
		if os.path.isfile(fullpath):
			msg2_3 = msg2_2+'\n\n'+r'┌─[File]─[ %s ]' % fullpath[-44:] +'\n'
			file = open(fullpath, mode='r', encoding='utf-8')
			filecontent = file.read()
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
	global hidden, root, overflow_on
	
	if (hidden == False):
		root.withdraw()
		taskbar.withdraw()
		titlepanel.withdraw()
		sidebar.attributes('-alpha', 0.1)
		#sidebar.geometry("1x690+0+50")
	else:
		root.deiconify()
		taskbar.deiconify()
		titlepanel.deiconify()
		sidebar.attributes('-alpha', 1.0)
		#sidebar.geometry("1x740+0+0")
		popup.withdraw()
		preview_clipboard()
	hidden = not hidden
	if overflow_on:
		overflow.withdraw()
		overflow_on = False

	root.focus_set()

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

def menu_open():
	toggle_sidebar()
	if os.path.isfile(fullpath): path = os.path.split(fullpath)[0]
	else: path = fullpath
	os.startfile(path)
	#subprocess.Popen(r'explorer /select,"C:\xampp"')
	#subprocess.Popen(r'explorer '+fullpath)

def menu_edit():
	toggle_sidebar()
	subprocess.Popen(['C:\Program Files\Sublime Text 3\sublime_text.exe', fullpath], start_new_session=True)
	#os.startfile(r'C:\Program Files\Sublime Text 3\sublime_text.exe '+fullpath)

def menu_select(path=''):
	node = tree.focus()
	if tree.parent(node):
		global fullpath
		print(path)
		if path!='': fullpath = path
		if os.path.isfile(fullpath): fullpath = os.path.split(fullpath)[0]
		os.chdir(fullpath)
		tree.delete(tree.get_children(''))
		populate_roots(tree)

def menu_terminal():
	if os.path.isfile(fullpath): path = os.path.split(fullpath)[0]
	else: path = fullpath
	subprocess.Popen(r'cmd /k cd /d '+path)

def menu_clear():
	#os.execv(sys.argv[0], sys.argv)
	os.execv(sys.executable, ['python'] + sys.argv)

def selectItem(a):
	selectedfocus = tree.focus()
	selecteditem = tree.item(selectedfocus)
	global fullpath
	fullpath = selecteditem.get('values')[0]
	preview_file()

def populate_tree(tree, node):
	if tree.set(node, "type") != 'directory':
		return

	path = tree.set(node, "fullpath")
	tree.delete(*tree.get_children(node))

	parent = tree.parent(node)
	#special_dirs = [] if parent else glob.glob('.') + glob.glob('..')
	special_dirs = []

	dirlist = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
	filelist = [x for x in os.listdir(path) if not os.path.isdir(os.path.join(path, x))]
	dirlist = os_sorted(dirlist)
	filelist = os_sorted(filelist)

	for i in dirlist:
		fname = os.path.split(i)[1]
		i = os.path.join(path, i)
		#folderimg = PhotoImage(file=ZLCORE+r"/Toolbar/_/[ Program ]/[ Source ]/gif/neon/folder.gif")
		#id = tree.insert(node, "end", text=fname, values=[i, "directory"], image=folderimg)
		id = tree.insert(node, "end", text=fname, values=[i, "directory"])
		tree.insert(id, 0, text="dummy")
		tree.item(id, text=fname)

	for i in filelist:
		fname = os.path.split(i)[1]
		i = os.path.join(path, i)
		id = tree.insert(node, "end", text=fname, values=[i, "file"])
		size = os.stat(i).st_size
		tree.set(id, "size", "%d bytes" % size)

	# for p in special_dirs + os.listdir(path):
	#	 ptype = None
	#	 p = os.path.join(path, p).replace('\\', '/')
	#	 if os.path.isdir(p): ptype = "directory"
	#	 elif os.path.isfile(p): ptype = "file"

	#	 fname = os.path.split(p)[1]
	#	 id = tree.insert(node, "end", text=fname, values=[p, ptype])

	#	 if ptype == 'directory':
	#		 if fname not in ('.', '..'):
	#			 tree.insert(id, 0, text="dummy")
	#			 tree.item(id, text=fname)
	#	 elif ptype == 'file':
	#		 size = os.stat(p).st_size
	#		 tree.set(id, "size", "%d bytes" % size)

def populate_roots(tree):
	#dir = os.path.abspath('.').replace('\\', '/')
	dir = fullpath
	node = tree.insert('', 'end', text=dir, values=[dir, "directory"], open=True)
	populate_tree(tree, node)

def update_tree(event):
	tree = event.widget
	populate_tree(tree, tree.focus())

def change_dir(event):
	tree = event.widget
	node = tree.focus()
	if tree.parent(node):
		path = os.path.abspath(tree.set(node, "fullpath"))
		if os.path.isfile(path): os.startfile(path)
		# if os.path.isdir(path):
		# 	os.chdir(path)
		# 	tree.delete(tree.get_children(''))
		# 	populate_roots(tree)

def autoscroll(sbar, first, last):
	first, last = float(first), float(last)
	if first <= 0 and last >= 1:
		sbar.grid_remove()
	else:
		sbar.grid()
	sbar.set(first, last)

def goBack(event=None):
	goPath(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

def goHome(event=None):
	goPath(home)

def goPath(path):
	global fullpath
	fullpath = path
	os.chdir(fullpath)
	tree.delete(tree.get_children(''))
	populate_roots(tree)

dialog = ''
def open_popup():
	global dialog
	newFileName.set('')
	
	dialog = Toplevel(root)
	dialog.geometry("+333+25")
	dialog.resizable(False, False)
	dialog.title("New")
	dialog.transient(root)
	dialog.columnconfigure(0, weight=1)
	Label(dialog, text='Enter File or Folder name').grid()
	Entry(dialog, textvariable=newFileName).grid(column=0, sticky='NSEW')
	btnframe = Frame(dialog)
	btnframe.grid(column=0, sticky='NSEW')
	Button(btnframe, text="Time", command=lambda: newFileName.set( str(round(time.time())) )).pack(side=LEFT)
	Button(btnframe, text="TXT", command=lambda: newFileName.set(newFileName.get()+'.txt')).pack(side=LEFT)
	Button(btnframe, text="[  ]", command=lambda: newFileName.set(r'[ '+newFileName.get()+r' ]')).pack(side=LEFT)
	Button(btnframe, text=" ¦ ", command=lambda: newFileName.set(newFileName.get()+r' ¦ ')).pack(side=LEFT)
	Button(btnframe, text=" √ ", command=lambda: newFileName.set(r'√ ')).pack(side=LEFT)
	Button(btnframe, text=" ≡ ", command=lambda: newFileName.set(r'≡ ')).pack(side=LEFT)
	Button(btnframe, text=" ▷ ", command=lambda: newFileName.set(r'▷ ')).pack(side=LEFT)
	Button(btnframe, text=" Δ ", command=lambda: newFileName.set(r'Δ[ '+newFileName.get()+r' ]')).pack(side=LEFT)
	Button(btnframe, text=" Σ ", command=lambda: newFileName.set(r'Σ[ '+newFileName.get()+r' ]')).pack(side=LEFT)
	Button(btnframe, text=" Ω ", command=lambda: newFileName.set(r'Ω[ '+newFileName.get()+r' ]')).pack(side=LEFT)
	Button(btnframe, text="Create", command=newFileOrFolder).pack(side=LEFT)

def newFileOrFolder():
	if os.path.isdir(fullpath): fullpath2 = fullpath
	if os.path.isfile(fullpath): fullpath2 = os.path.split(fullpath)[0]
	if len(newFileName.get().split('.')) != 1:
		open(os.path.join(fullpath2, newFileName.get()), 'w').close()
	else:
		os.mkdir(os.path.join(fullpath2, newFileName.get()))
	dialog.destroy()
	if os.path.isdir(fullpath): populate_tree(tree, tree.focus())
	else: populate_tree(tree, tree.parent(tree.focus()))

newFileName = StringVar(root, "", 'new_name')
#currentPath = StringVar(root, name='currentPath', value=pathlib.Path.cwd())
#currentPath.trace('w', pathChange)

def workspace_select():
	global fullpath
	combo1.configure(state="readonly")
	file = open(ZLCORE+r'\Toolbar\F\[ Workspace ]\[ Sidebar ]\Internal.txt', mode='r')
	filecontent = file.read()
	file.close()
	filecontent = filecontent.split("\n")
	combo1['values'] = filecontent

	combo1.configure(width=len(combo1.get())+1)
	fullpath = ZLCORE+'\\Toolbar\\F\\[ Workspace ]\\[ Sidebar ]\\'+combo1.get()
	if os.path.isdir(fullpath):
		os.chdir(fullpath)
		tree.delete(tree.get_children(''))
		populate_roots(tree)


Button(root, text='≡', command=goHome, bg=colorbg, fg=colorfg).grid(sticky='NSEW', column=0, row=0)

frame1 = Frame(root, bg=colorbg)
frame1.grid(sticky='NSEW', column=0, row=1)
button1 = Button(frame1, text='∆', command=goBack, bg=colorbg, fg=colorfg)
button2 = Button(frame1, text='X', command=goBack, bg=colorbg, fg=colorfg)
button1.grid(sticky='N', row=0)
button2.grid(sticky='N', row=1)
#button1.place(relx=0, rely=0, relwidth=0.1, relheight=0.1)
frame2 = Frame(root, bg=colorbg)
frame2.grid(sticky='NSEW', column=1, row=1)

#Entry(root, textvariable=currentPath, bg=colorbg, fg=colorfg)
frame3 = Frame(root, bg=colorbg)
frame3.grid(sticky='NSEW', column=1, row=0)
frame3_1 = Frame(frame3, bg=colorbg)
frame3_1.grid(sticky='W', row=0, column=0)
Button(frame3_1, text='C', bg=colorbg, fg=colorfg, command=lambda: goPath('C:\\')).grid(sticky='W', row=0, column=0)
Button(frame3_1, text='D', bg=colorbg, fg=colorfg, command=lambda: goPath('D:\\')).grid(sticky='W', row=0, column=1)
Label(frame3_1, text='|', bg=colorbg, fg=colorfg).grid(sticky='W', row=0, column=2)
Button(frame3_1, text='╬', bg=colorbg, fg=colorfg, command=lambda: goPath(r'D:\Scraps\╬')).grid(sticky='W', row=0, column=3)
Button(frame3_1, text='_', bg=colorbg, fg=colorfg, command=lambda: goPath('D:\\_')).grid(sticky='W', row=0, column=4)
Button(frame3_1, text='Data', bg=colorbg, fg=colorfg, command=lambda: goPath('D:\\Data')).grid(sticky='W', row=0, column=5)
Button(frame3_1, text='Core', bg=colorbg, fg=colorfg, command=lambda: goPath('D:\\ZL-Core')).grid(sticky='W', row=0, column=6)
Button(frame3_1, text='Scraps', bg=colorbg, fg=colorfg, command=lambda: goPath('D:\\Scraps')).grid(sticky='W', row=0, column=7)
frame3_2 = Frame(frame3, bg=colorbg)
frame3_2.grid(sticky='E', row=0, column=1)
frame3.grid_columnconfigure(1, weight=1)
combo1 = ttk.Combobox(frame3_2, state="readonly", values=['--------------'], width=10)
combo1.grid(sticky='E', row=0, column=0)
combo1.bind('<Button-3>', lambda e: combo1.configure(state="normal"))
combo1.bind('<Button-1>', lambda e: workspace_select())
combo1.bind('<<ComboboxSelected>>', lambda e: workspace_select())

vsb = ttk.Scrollbar(frame2, orient="vertical")
hsb = ttk.Scrollbar(frame2, orient="horizontal")
tree = ttk.Treeview(frame2, columns=("fullpath", "type", "size"), show="tree",
	displaycolumns="size", yscrollcommand=lambda f, l: autoscroll(vsb, f, l),
	xscrollcommand=lambda f, l:autoscroll(hsb, f, l))
vsb['command'] = tree.yview
hsb['command'] = tree.xview
tree.grid(column=0, row=0, sticky='NSEW')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_rowconfigure(0, weight=1)

tree.heading("#0", text="Directory Structure", anchor='w')
tree.heading("size", text="File Size", anchor='w')
tree.column("size", stretch=0, width=0)
#tree['show'] = ('headings', 'tree')

populate_roots(tree)
tree.bind('<<TreeviewOpen>>', update_tree)
tree.bind('<Double-Button-1>', change_dir)
tree.bind('<ButtonRelease-1>', selectItem)


#menubar = Menu(root, tearoff=0, background='#ffffff', foreground='#000000', activebackground='#000000', activeforeground='#ffffff')
menubar = Menu(root, tearoff=0)
menubar.add_command(label="New", command=open_popup)
menubar.add_separator()
menubar.add_command(label="Open", command=menu_open)
#subedit = Menu(menubar, tearoff=0)
#menubar.add_cascade(label="Edit", menu=subedit, command=menu_edit)
menubar.add_command(label="Edit", command=menu_edit)
menubar.add_command(label="Select", command=menu_select)
menubar.add_separator()
menubar.add_command(label="Copy path", command=lambda: (root.clipboard_clear(),root.clipboard_append(fullpath),root.update()))
menubar.add_command(label="Go to path", command=lambda: menu_select(root.clipboard_get()))
menubar.add_command(label="Terminal", command=menu_terminal)
menubar.add_command(label="Detach", command=menu_select)
#menubar.add_command(label="Exit", command=menu_clear)
#menubar.add_command(label="Exit", command=root.quit)
#root.config(menu=menubar)
tree.bind("<Button-3>", lambda event: menubar.post(event.x_root, event.y_root))

#-------------------------------------------------------------------------------

sidebar.bind("<Button-1>", toggle_sidebar)
sidebarext.bind("<Button-1>", toggle_sidebar)
root.bind("<Alt-Up>", goBack)
#root.bind("<FocusOut>", exit)

if tooltip:
	sidebar.bind("<Enter>", lambda e: tooltip_show(e.x, e.y))
	sidebar.bind("<Leave>", lambda e: tooltip_hide())
	sidebar.bind('<Motion>', lambda e: tooltip_show(e.x, e.y))
	sidebarext.bind("<Enter>", lambda e: tooltip_show(e.x, e.y))
	sidebarext.bind("<Leave>", lambda e: tooltip_hide())
	sidebarext.bind('<Motion>', lambda e: tooltip_show(e.x, e.y))
sidebar.mainloop()
