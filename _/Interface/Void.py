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
height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar
sidebar.geometry(f"1x{height}+0+0")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)

sidebarext = Toplevel(sidebar)
sidebarext.attributes('-topmost', True)
sidebarext.attributes('-alpha', 0.1)
sidebarext.title('1ext')
height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar - 25
bottom = Zeta.System.Size.taskbar
sidebarext.geometry(f"1x{height}-0-{bottom}")
sidebarext.overrideredirect(1)
sidebarext.configure(bg=colorbg)
sidebarext.hide()
Panel['System']['sidebarext'] = sidebarext

# sidebar2 = Toplevel(sidebar)
sidebar2 = Window(color2='white', mode='border')
sidebar2.title('===[ Sidebar: File ]===')
sidebar2.attributes('-topmost', True)
sidebar2.attributes('-alpha', 0.77)
height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar - 25
sidebar2.geometry(f"333x{height}-1+25")
sidebar2.overrideredirect(1)
sidebar2.hide()
File2 = FileBox(sidebar2.frame, home=Zeta.System.Path.Core().Sidebar, darkmode=True)

taskbar = External.Taskbar(Workspace)
Panel['System']['taskbar'] = taskbar

wallpaper = External.Wallpaper()
Panel['System']['wallpaper'] = wallpaper

popup = Toplevel()
popup.title('Popup')
popup.geometry("+10+350")
popup.overrideredirect(1)
popup.attributes('-alpha', 0.77)
popup.configure(bg=colorbg)
popup.attributes('-topmost', True)
popupmsg = Label(popup, text='', bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal"))
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

def toggle_sidebar(*event):
	Workspace.toggle_sidebar(popupmsg.cget('text'))
	wallpaper.preview_clipboard()

def tooltip_show(x, y):
	#popup.show() if hidden else print(e)
	if Workspace.hidden:
		if (y<=50 and x==0): (popupmsg.configure(text='Network'),popup.geometry('+10+10'),popup.show())
		elif (y>50 and y<100): (popupmsg.configure(text='File'),popup.geometry('+10+50'),popup.show())
		elif x>=1: (popupmsg.configure(text='F'),popup.geometry('+10+10'),popup.show())
		elif y>=700: (popupmsg.configure(text='Lounge'),popup.geometry('+10-40'),popup.show())
		else: (popupmsg.configure(text='File'),popup.hide())
		# else: (popupmsg.configure(text=Workspace.active),popup.hide())

def tooltip_hide():
	popup.hide() if Workspace.hidden else print('hidden')

#-------------------------------------------------------------------------------

class Controller():
	def toggle_sidebar(child): toggle_sidebar()
	def preview_file(child, path): wallpaper.preview_file(path)
Workspace.controller = Controller()

root = External.File(controller=Workspace.controller)
wallpaper.watch = root.File1
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
Workspace.toggle_bind(sidebarext, sidebar2)

#taskbar.bind("<Enter>", lambda e: root.hide())
#taskbar.bind("<Button-1>", lambda event: (root.hide(), sidebar.geometry("1366x1+0+0"), taskbar.geometry("1366x24+0+1")))
taskbar.bind("<Button-1>", lambda event: Workspace.hide(Workspace.active))

File2.controller = Workspace.controller

sidebar.mainloop()