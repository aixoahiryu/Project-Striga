import Zeta
import External
from Zeta.Panel import *
import tkinter.ttk as ttk

import time
import os
import glob
import subprocess

from natsort import os_sorted
#import codecs


ZLCORE = os.environ['ZLCORE']
#os.chdir(home)
#cwd = os.getcwd()

addicon = False
darkmode = True
tooltip = True
colorbg = "#000000" if darkmode else "#ffffff"
colorbg2 = "#253B34" if darkmode else "#6effbe"
colorfg = "#ffffff" if darkmode else "#000000"

Panel = {'System': {'taskbar': '', 'wallpaper': ''}, 'File': {'root': ''}, 'Network': {'root': ''}, 'Lounge': {'root': ''}}
Workspace = Zeta.System.WM.Workspace(Panel)

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
sidebarext.hide()
Panel['System']['sidebarext'] = sidebarext

# sidebar2 = Toplevel(sidebar)
sidebar2 = Window(color2='white', mode='border')
sidebar2.title('===[ Sidebar: File ]===')
sidebar2.attributes('-topmost', True)
sidebar2.attributes('-alpha', 0.77)
sidebar2.geometry("333x715-1+25")
sidebar2.overrideredirect(1)
sidebar2.hide()
File2 = FileBox(sidebar2.frame, home=Zeta.System.Path.Core().Sidebar, darkmode=True)

overflow = Toplevel(sidebar)
overflow.title('Icon overflow')
overflow.geometry("-0+25")
overflow.overrideredirect(1)
overflow.configure(bg=colorbg)
#overflow.transient(taskbar)
overflow.attributes('-topmost', True)
imggemini=Zeta.Image.Icon.Load(icon='geminiw', icontype='bw').image
Button(overflow, text=' Thaumiel', relief='flat', background=colorbg, foreground='#c9c9c9', image=imggemini, compound='left').grid(column=0, row=0, sticky='NW')
imgeye=Zeta.Image.Icon.Load(icon='eyew', icontype='bw').image
Button(overflow, text=' The eye', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgeye, compound='left').grid(column=0, row=1, sticky='NW')
imgmoon=Zeta.Image.Icon.Load(icon='moonw', icontype='bw').image
Button(overflow, text=' Moon cycle', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgmoon, compound='left').grid(column=0, row=2, sticky='NW')
imgsun=Zeta.Image.Icon.Load(icon='sunw', icontype='bw').image
Button(overflow, text=' Sun cycle', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgsun, compound='left').grid(column=0, row=3, sticky='NW')
imgdice=Zeta.Image.Icon.Load(icon='dicew', icontype='bw').image
Button(overflow, text=' Chaos theory', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgdice, compound='left').grid(column=0, row=4, sticky='NW')
imgcalendar=Zeta.Image.Icon.Load(icon='calendarw', icontype='bw').image
Button(overflow, text=' Calendar', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgcalendar, compound='left').grid(column=0, row=5, sticky='NW')
imghorse=Zeta.Image.Icon.Load(icon='horsew', icontype='bw').image
Button(overflow, text=' Strategy', relief='flat', background=colorbg, foreground='#c9c9c9', image=imghorse, compound='left').grid(column=0, row=6, sticky='NW')
imgwave=Zeta.Image.Icon.Load(icon='wave2w', icontype='bw').image
Button(overflow, text=' Flunctuation', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgwave, compound='left').grid(column=0, row=7, sticky='NW')
overflow.hide()

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
imgcode=Zeta.Image.Icon.Load(icon='code', icontype='neon').image
Button(appframe, text=' Program', relief='flat', background=colorbg, foreground=colorfg, image=imgcode, compound='left').grid(column=5, row=0, sticky='NW')
imgterm=Zeta.Image.Icon.Load(icon='term3', icontype='neon').image
Button(appframe, text=' Hacking', relief='flat', background=colorbg, foreground=colorfg, image=imgterm, compound='left').grid(column=6, row=0, sticky='NW')
imgfile=Zeta.Image.Icon.Load(icon='file', icontype='neon').image
Button(appframe, text=' File', relief='flat', background=colorbg, foreground='#6effbe', image=imgfile, compound='left').grid(column=7, row=0, sticky='NW')
imglink=Zeta.Image.Icon.Load(icon='qr', icontype='neon').image
Button(appframe, text=' Network', relief='flat', background=colorbg, foreground=colorfg, image=imglink, compound='left').grid(column=8, row=0, sticky='NW')
trayframe = Frame(taskbar, bg=colorbg)
trayframe.grid(sticky='NSE', column=1, row=0)
taskbar.grid_columnconfigure(1, weight=1)
imgcpu=Zeta.Image.Icon.Load(icon='cpuw', icontype='bw').image
Button(trayframe, text=' 13%', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgcpu, compound='left').grid(column=0, row=0, sticky='NW')
imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
Button(trayframe, text=' 322G', relief='flat', background=colorbg, foreground='#c9c9c9', image=imghdd, compound='left').grid(column=1, row=0, sticky='NW')
imgnetwork=Zeta.Image.Icon.Load(icon='networkw', icontype='bw').image
Button(trayframe, text=' 0.7 MB/s', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgnetwork, compound='left').grid(column=2, row=0, sticky='NW')
imgram=Zeta.Image.Icon.Load(icon='ramw', icontype='bw').image
Button(trayframe, text=' 2.2 GB', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgram, compound='left').grid(column=3, row=0, sticky='NW')
imgtemp=Zeta.Image.Icon.Load(icon='tempw', icontype='bw').image
Button(trayframe, text=' 33°C', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgtemp, compound='left').grid(column=4, row=0, sticky='NW')
imgvolume=Zeta.Image.Icon.Load(icon='volumew', icontype='bw').image
Button(trayframe, text=' Ballad', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgvolume, compound='left').grid(column=5, row=0, sticky='NW')
imgmenu=Zeta.Image.Icon.Load(icon='menuw', icontype='bw').image
btnoverflow = Button(trayframe, text='', relief='flat', background=colorbg, foreground='#c9c9c9', image=imgmenu, compound='none')
btnoverflow.grid(column=6, row=0, sticky='NW')
Zeta.System.WM.toggle_bind(btnoverflow, overflow)
Panel['System']['taskbar'] = taskbar


wallpaper = Toplevel()
wallpaper.attributes('-alpha', 0.77)
wallpaper.title('ASCII')
wallpaper.geometry("1366x738+0+0")
wallpaper.overrideredirect(1)
wallpaper.configure(bg=colorbg)
Panel['System']['wallpaper'] = wallpaper
msg1=r'''

 __________________________________________________________
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
msg3=r'''

As above, so below. As within, so without.
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
| 
|                                                             |
|                                                             |
|                                                             |
└── ‡ breach --cluster #6effbe                         ───────┘
'''
txt1 = Frame(wallpaper, bg=colorbg)
txt1.grid(row=0, column=0, sticky='NW')
Message(txt1, text=msg1, width=444, bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal")).grid(row=0, column=0, sticky='NW')
txt2 = Message(wallpaper, text=msg2, width=444, bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal"))
txt2.grid(row=0, column=1, sticky='NEW')
txt3 = Message(wallpaper, text=msg3, width=444, bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal"))
txt3.grid(row=0, column=2, sticky='NE')
wallpaper.grid_columnconfigure(0, weight=1)
wallpaper.grid_columnconfigure(1, weight=1)
wallpaper.grid_columnconfigure(2, weight=1)
txt1frame = Frame(txt1, bg=colorbg)
txt1frame.grid(row=1, column=0, sticky='NW')
img1=Zeta.Image.Icon.Load(icon='geminiw', icontype='bw').image
Button(txt1frame, text=' Thaumiel', relief='flat', background=colorbg, foreground='#c9c9c9', image=img1, compound='left').grid(column=0, row=0, sticky='NW')

popup = Toplevel(sidebar)
popup.title('Popup')
popup.geometry("+10+350")
popup.overrideredirect(1)
popup.attributes('-alpha', 0.77)
popup.configure(bg=colorbg)
popup.attributes('-topmost', True)
popupmsg = Message(popup, text='', bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal"), aspect=500)
popupmsg.grid(sticky='NWES')
popup.hide()

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
		temp1 = sidebar.clipboard_get().split('\n')
		for i in temp1[:10]:
			msg2_2 = msg2_2+r'| '+i[:55]+'\n'
		if len(temp1)<10:
			for i in range(0, (10-len(temp1))): msg2_2 = msg2_2+r'| '+'\n'
		msg2_2 = msg2_2+r'└── ‡ limit --head 10'
		txt2.configure(text=msg2_2)
		preview_file(root.File1.fullpath)
	except: #txt2.configure(text=msg2+'Clipboard failure')
		msg2_2 = msg2+r'┌─[ Clipboard:xclip ]─[ /dev/clipboard ]'+'\n'
		msg2_2 = msg2_2+r'| '+'Cliboard failure \n'
		for i in range(1, 10): msg2_2 = msg2_2+r'| '+'\n'
		msg2_2 = msg2_2+r'└── ‡ limit --head 10'
		txt2.configure(text=msg2_2)
		preview_file(root.File1.fullpath)

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
	Workspace.toggle(popupmsg.cget('text'))
	
	if sidebarext.on: Zeta.System.WM.toggle(sidebarext)
	if btnoverflow.on: Zeta.System.WM.toggle(btnoverflow)

	preview_clipboard()

def tooltip_show(x, y):
	#popup.show() if hidden else print(e)
	if Workspace.hidden:
		if (y<=50 and x==0): (popupmsg.configure(text='Network'),popup.geometry('+10+10'),popup.show())
		elif x>=1: (popupmsg.configure(text='F'),popup.geometry('+10+10'),popup.show())
		elif y>=700: (popupmsg.configure(text='Lounge'),popup.geometry('+10-40'),popup.show())
		else: (popupmsg.configure(text='File'),popup.hide())

def tooltip_hide():
	popup.hide() if Workspace.hidden else print('hidden')

#-------------------------------------------------------------------------------

class Controller():
	def toggle_sidebar(child): toggle_sidebar()
	def preview_file(child, path): preview_file(path)

root = External.File(controller=Controller())
#root.option_add("*tearOff", False)
#root.configure(background="#000000")
#root.configure(highlightbackground="#000000")
#root.configure(highlightcolor="white")
Panel['File']['root'] = root

search = External.Search()
Panel['Network']['root'] = search
Panel['Lounge']['root'] = root

#-------------------------------------------------------------------------------

if tooltip:
	sidebar.bind("<Enter>", lambda e: tooltip_show(e.x, e.y))
	sidebar.bind('<Motion>', lambda e: tooltip_show(e.x, e.y))
	sidebar.bind("<Leave>", lambda e: tooltip_hide())
	sidebar.bind("<Button-1>", lambda e: tooltip_hide())

sidebar.bind("<Button-1>", toggle_sidebar, add="+")
Zeta.System.WM.toggle_bind(sidebarext, sidebar2)

#taskbar.bind("<Enter>", lambda e: root.hide())
#taskbar.bind("<Button-1>", lambda event: (root.hide(), sidebar.geometry("1366x1+0+0"), taskbar.geometry("1366x24+0+1")))
taskbar.bind("<Button-1>", lambda event: Workspace.hide(Workspace.active))

File2.controller = Controller()

sidebar.mainloop()