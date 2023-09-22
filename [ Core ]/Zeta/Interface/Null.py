import Zeta
import Internal
from Zeta.Panel import *
import tkinter.ttk as ttk

import webbrowser
import os

from natsort import os_sorted


ZLCORE = os.environ['ZLCORE']

addicon = False
darkmode = False
tooltip = True
colorbg = "#000000" if darkmode else "#ffffff"
colorbg2 = "#253B34" if darkmode else "#6effbe"
colorfg = "#ffffff" if darkmode else "#000000"

Panel = {'System': {'taskbar': '', 'wallpaper': ''}, 'Monolith': {'root': ''}, 'Command': {'root': ''}, 'Launch': {'root': ''}}
Workspace = Zeta.System.WM.Workspace(Panel)

sidebar = Tk()
sidebar.attributes('-topmost', True)
sidebar.attributes('-alpha', 0.1)
sidebar.title('1px')
sidebar.geometry("1x740-0+0")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)

sidebarext = Toplevel(sidebar)
sidebarext.attributes('-topmost', True)
sidebarext.attributes('-alpha', 0.1)
sidebarext.title('1ext')
sidebarext.geometry("1x740+0+0")
sidebarext.overrideredirect(1)
sidebarext.configure(bg=colorbg)
sidebarext.hide()
Panel['System']['sidebarext'] = sidebarext

# sidebar2 = Toplevel(sidebar)
sidebar2 = Window(color2='black', mode='border')
sidebar2.title('===[ Sidebar: File ]===')
sidebar2.attributes('-topmost', True)
sidebar2.geometry("333x730+5+5")
sidebar2.overrideredirect(1)
sidebar2.hide()
File1 = FileBox(sidebar2.frame, home=Zeta.System.Path.Core().Planner, darkmode=False)

overflow = Toplevel(sidebar)
overflow.title('Icon overflow')
overflow.geometry("+0-25")
overflow.overrideredirect(1)
overflow.configure(bg=colorbg)
#overflow.transient(taskbar)
overflow.attributes('-topmost', True)
imggemini=Zeta.Image.Icon.Load(icon='cpub', icontype='bw').image
Button(overflow, text=' Thaumiel', relief='flat', bg=colorbg, fg=colorfg, image=imggemini, compound='left').grid(column=0, row=0, sticky='NW')
imgeye=Zeta.Image.Icon.Load(icon='cpub', icontype='bw').image
Button(overflow, text=' The eye', relief='flat', bg=colorbg, fg=colorfg, image=imgeye, compound='left').grid(column=0, row=1, sticky='NW')
imgmoon=Zeta.Image.Icon.Load(icon='cpub', icontype='bw').image
Button(overflow, text=' Moon cycle', relief='flat', bg=colorbg, fg=colorfg, image=imgmoon, compound='left').grid(column=0, row=2, sticky='NW')
imgsun=Zeta.Image.Icon.Load(icon='cpub', icontype='bw').image
Button(overflow, text=' Sun cycle', relief='flat', bg=colorbg, fg=colorfg, image=imgsun, compound='left').grid(column=0, row=3, sticky='NW')
imgdice=Zeta.Image.Icon.Load(icon='cpub', icontype='bw').image
Button(overflow, text=' Chaos theory', relief='flat', bg=colorbg, fg=colorfg, image=imgdice, compound='left').grid(column=0, row=4, sticky='NW')
imgcalendar=Zeta.Image.Icon.Load(icon='cpub', icontype='bw').image
Button(overflow, text=' Calendar', relief='flat', bg=colorbg, fg=colorfg, image=imgcalendar, compound='left').grid(column=0, row=5, sticky='NW')
imghorse=Zeta.Image.Icon.Load(icon='cpub', icontype='bw').image
Button(overflow, text=' Strategy', relief='flat', bg=colorbg, fg=colorfg, image=imghorse, compound='left').grid(column=0, row=6, sticky='NW')
imgwave=Zeta.Image.Icon.Load(icon='cpub', icontype='bw').image
Button(overflow, text=' Flunctuation', relief='flat', bg=colorbg, fg=colorfg, image=imgwave, compound='left').grid(column=0, row=7, sticky='NW')
overflow.hide()

taskbar = Toplevel(sidebar)
taskbar.attributes('-topmost', True)
taskbar.title('Taskbar')
taskbar.geometry("1366x30+0-0")
taskbar.overrideredirect(1)
taskbar.grid_rowconfigure(0, weight=1)
taskbar.configure(bg=colorbg)
#Label(taskbar, text=r'[ Workspace ]', bg=colorbg, fg=colorfg).place(relx=0.48, rely=0)
appframe = Frame(taskbar, bg=colorbg)
appframe.grid(sticky='NSW', column=0, row=0)
appframe.grid_rowconfigure(0, weight=1)
imgmenu=Zeta.Image.Icon.Load(icon='menu2b', icontype='bw').image
btnoverflow = Button(appframe, text='', relief='flat', bg=colorbg, fg=colorfg, image=imgmenu, compound='left')
btnoverflow.grid(column=0, row=0, sticky='NSW')
# Zeta.System.WM.toggle_bind(btnoverflow, overflow)
Workspace.toggle_bind(btnoverflow, overflow)
quickframe = Frame(taskbar, bg=colorbg)
quickframe.grid(sticky='NSW', column=1, row=0)
quickframe.grid_rowconfigure(0, weight=1)
imgbrowser=Zeta.Image.Icon.Load(icon='eye2b', icontype='bw').image
Button(quickframe, text='', relief='flat', bg=colorbg, fg=colorfg, image=imgbrowser, compound='left').grid(column=0, row=0, sticky='NSW')
imgproxy=Zeta.Image.Icon.Load(icon='proxyb', icontype='bw').image
Button(quickframe, text='', relief='flat', bg=colorbg, fg=colorfg, image=imgproxy, compound='left').grid(column=1, row=0, sticky='NSW')
programframe = Frame(taskbar, bg=colorbg)
programframe.grid(sticky='NSW', column=2, row=0)
programframe.grid_rowconfigure(0, weight=1)
Button(programframe, text='[ Main ]', relief='flat', bg=colorbg, fg=colorfg).grid(column=0, row=0, sticky='NSW')
Button(programframe, text='Peripheral', relief='flat', bg=colorbg, fg=colorfg).grid(column=1, row=0, sticky='NSW')
Button(programframe, text='Transient', relief='flat', bg=colorbg, fg=colorfg).grid(column=2, row=0, sticky='NSW')
trayframe = Frame(taskbar, bg=colorbg)
trayframe.grid(sticky='NSE', column=3, row=0)
trayframe.grid_rowconfigure(0, weight=1)
taskbar.grid_columnconfigure(3, weight=1)
btnF = Button(trayframe, text=' F ', relief='flat', bg=colorbg, fg=colorfg)
btnF.grid(column=0, row=0, sticky='NSW')
btnF.bind("<Button-3>", lambda e: (os.startfile(ZLCORE+r'\Toolbar\F'), toggle_sidebar()))
btnN = Button(trayframe, text=' N ', relief='flat', bg=colorbg, fg=colorfg)
btnN.grid(column=1, row=0, sticky='NSW')
btnN.bind("<Button-3>", lambda e: (os.startfile(ZLCORE+r'\Toolbar\N'), toggle_sidebar()))
btn_ = Button(trayframe, text=' _ ', relief='flat', bg=colorbg, fg=colorfg)
btn_.grid(column=2, row=0, sticky='NSW')
btn_.bind("<Button-3>", lambda e: (os.startfile(ZLCORE+r'\Toolbar\_'), toggle_sidebar()))
imgrect=Zeta.Image.Icon.Load(icon='cornerb', icontype='bw').image
Button(trayframe, text='', relief='flat', bg=colorbg, fg=colorfg, image=imgrect, compound='left').grid(column=3, row=0, sticky='NSW')
imghardware=Zeta.Image.Icon.Load(icon='cpub', icontype='bw').image
Button(trayframe, text=' System', relief='flat', bg=colorbg, fg=colorfg, image=imghardware, compound='left').grid(column=4, row=0, sticky='NSW')
imgmonitoring=Zeta.Image.Icon.Load(icon='motherboardb', icontype='bw').image
Button(trayframe, text=' Manager', relief='flat', bg=colorbg, fg=colorfg, image=imgmonitoring, compound='left').grid(column=5, row=0, sticky='NSW')
imgcalendar=Zeta.Image.Icon.Load(icon='calendarb', icontype='bw').image
Button(trayframe, text=' Z[1.95996|97.5] 54.7356° π[3.14159] √[1.41421] ϕ[1.61803]', relief='flat', bg=colorbg, fg=colorfg, image=imgcalendar, compound='left').grid(column=6, row=0, sticky='NSW')
Button(trayframe, text=' ', relief='flat', bg=colorbg, fg=colorfg).grid(column=7, row=0, sticky='NSW')
Panel['System']['taskbar'] = taskbar

wallpaper = Toplevel(sidebar)
wallpaper.title('Wallpaper')
wallpaper.geometry("1366x740+0+0")
wallpaper.overrideredirect(1)
wallpaper.configure(bg=colorbg)
wallpaper.lower()
wallpaper.hide()
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

ttk.Style().theme_use('alt')

def toggle_sidebar(*event):
	Workspace.toggle_sidebar(popupmsg.cget('text'))
	
	# if sidebarext.on: Zeta.System.WM.toggle(sidebarext)
	# if btnoverflow.on: Zeta.System.WM.toggle(btnoverflow)

def tooltip_show(x, y):
	#popup.show() if hidden else print(e)
	if Workspace.hidden:
		if (y<=50 and x==0): (popupmsg.configure(text='Monolith'),popup.geometry('-10+10'),popup.show())
		elif x>=1: (popupmsg.configure(text='_'),popup.geometry('-10+10'),popup.show())
		elif y>=468: (popupmsg.configure(text='Launch'),popup.geometry('-10-40'),popup.show())
		else: (popupmsg.configure(text='Command'),popup.hide())

def tooltip_hide():
	popup.hide() if Workspace.hidden else print('hidden')

#-------------------------------------------------------------------------------

def menu_clear():
	#os.execv(sys.argv[0], sys.argv)
	os.execv(sys.executable, ['python'] + sys.argv)

root = Internal.Launch()
Panel['Launch']['root'] = root
Panel['Monolith']['root'] = root
Panel['Command']['root'] = root

#-------------------------------------------------------------------------------

if tooltip:
	sidebar.bind("<Enter>", lambda e: tooltip_show(e.x, e.y))
	sidebar.bind('<Motion>', lambda e: tooltip_show(e.x, e.y))
	sidebar.bind("<Leave>", lambda e: tooltip_hide())
	sidebar.bind("<Button-1>", lambda e: tooltip_hide())

sidebar.bind("<Button-1>", toggle_sidebar, add="+")
Workspace.toggle_bind(sidebarext, sidebar2)
# Zeta.System.WM.toggle_bind(sidebarext, sidebar2)
# Zeta.System.WM.hover_bind(sidebarext, sidebar2, stay=True)

#taskbar.bind("<Enter>", lambda e: root.hide())
#taskbar.bind("<Button-1>", lambda event: (root.hide(), sidebar.geometry("1366x1+0+0"), taskbar.geometry("1366x24+0+1")))
taskbar.bind("<Button-1>", lambda event: Workspace.hide(Workspace.active))

sidebar.mainloop()