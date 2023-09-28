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
height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar
sidebar.geometry(f"1x{height}-0+0")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)

sidebarext = Toplevel(sidebar)
sidebarext.attributes('-topmost', True)
sidebarext.attributes('-alpha', 0.1)
sidebarext.title('1ext')
height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar
sidebarext.geometry(f"1x{height}+0+0")
sidebarext.overrideredirect(1)
sidebarext.configure(bg=colorbg)
sidebarext.hide()
Panel['System']['sidebarext'] = sidebarext

# sidebar2 = Toplevel(sidebar)
sidebar2 = Window(color2='black', mode='border')
sidebar2.title('===[ Sidebar: File ]===')
sidebar2.attributes('-topmost', True)
height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar - 5 - 5
sidebar2.geometry(f"333x{height}+5+5")
sidebar2.overrideredirect(1)
sidebar2.hide()
File1 = FileBox(sidebar2.frame, home=Zeta.System.Path.Core().Planner, darkmode=False)
sidebar2.theme(sidebar2.frame, bg='#ffffff', fg='#000000')

taskbar = Internal.Taskbar(Workspace)
Panel['System']['taskbar'] = taskbar

wallpaper = Toplevel(sidebar)
wallpaper.title('Wallpaper')
width = Zeta.System.Size.Screen.width
height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar
wallpaper.geometry(f"{width}x{height}+0+0")
wallpaper.overrideredirect(1)
wallpaper.configure(bg=colorbg)
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