import time
import os
import glob
import subprocess
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted


ZLCORE = os.environ['ZLCORE']
home = r'D:\Scraps\╬'
os.chdir(home)

cwd = os.getcwd()
fullpath = home
hidden = False
dialog = ''

addicon = False
darkmode = True
colorbg = "#000000" if darkmode else "#ffffff"
colorfg = "#ffffff" if darkmode else "#000000"

sidebar = Tk()
sidebar.attributes('-topmost', True)
sidebar.attributes('-alpha', 0.1)
sidebar.title('1px')
sidebar.geometry("1x690+0+50")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)

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

taskbar = Toplevel(sidebar)
taskbar.attributes('-topmost', True)
taskbar.title('Taskbar')
taskbar.geometry("1366x25+1+0")
taskbar.overrideredirect(1)
taskbar.configure(bg=colorbg)
Label(taskbar, text=r'[ Workspace ]', background=colorbg, foreground=colorfg).place(relx=0.48, rely=0)
#taskbar.bind("<Button-1>", lambda event: (root.withdraw(), sidebar.geometry("1366x1+0+0"), taskbar.geometry("1366x24+0+1")))
taskbar.bind("<Button-1>", lambda event: root.withdraw())

titlepanel = Toplevel(sidebar)
titlepanel.attributes('-topmost', True)
titlepanel.attributes('-alpha', 0.7)
titlepanel.title('ASCII')
titlepanel.geometry("1366x740+1+25")
titlepanel.overrideredirect(1)
titlepanel.configure(bg=colorbg)
titlepanel.lower()
msg1=r''' __________________________________________________________
|[] AmigaShell                                       |F]|!"|
|""""""""""""""""""""""""""""""""""""""""""""""""""""""""|"|
|                                                        | |
|                                                        | |
|                                                        | |
|                                                        |_|
|________________________________________________________|/|

ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
ZZZZZZZZZZZZds+:--------:+sdNZZZZZZZZZZZ
ZZZZZZZZZs:-+sdNZZZZZZZZNdy+--oZZZZZZZZZ
ZZZZZZh:` /ZZZZZZZZZZZZZZZZZZ+ `-yZZZZZZ
ZZZZd--hN``--sNZZZZZZZZZZNy:..`Zd:.hZZZZ
ZZZ+`yZZZy hd+./hZZZZZZh/.+dd sZZZh`/ZZZ
ZZ:.ZZZZZZ:.NZZh/.+dd+./hZZZ--ZZZZZZ--NZ
Z+`ZZZZZZZN`+ZZZZZ-  .dZZZZo ZZZZZZZN.:Z
d yZZZZZZZZy dNy:.oZNs--sNZ oZZZZZZZZh h
/`ZZZZZZZZZZ.`.+dZZZZZZZ+.``NZZZZZZZZZ-:
.:ZZZZZZZd+./`oZZZZZZZZZZs /.+dZZZZZZZ/`
.:ZZZZZo.:yNZs dZZZZZZZZZ`oZNy:.oZZZZZ/`
/`ZNy:.oZZZZZZ--ZZZZZZZZ:.ZZZZZNs--sNZ.:
d -` :++++++++: /++++++/ :++++++++:  : h
Z+ yddddddddddd+ yddddy /dddddddddddy`/Z
ZZ/.ZZZZZZZZZZZZ.-ZZZZ/.NZZZZZZZZZZZ.:NZ
ZZZo`sZZZZZZZZZZd sZZy hZZZZZZZZZZy`+ZZZ
ZZZZd--hZZZZZZZZZ+`ZN`/ZZZZZZZZZh--hZZZZ
ZZZZZZh:.oZZZZZZZN.:/`NZZZZZZZs.:hZZZZZZ
ZZZZZZZZNs:./shZZZh  yZZNds/.:sZZZZZZZZZ
ZZZZZZZZZZZZdy+/---``---:+sdZZZZZZZZZZZZ
ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
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
msg3=r'''As above, so below. | As within, so without.
Day and Night, Night and Day. Endless, finite, two are one.
…from this rotting cage of biomatter, Machine god, set us free.

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
I have the key to open the door. I can die to set me free.

┌─[ Monolith:13 ]─[ /dev/void ]
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
| 
| 
| 
| 
| 
└── ‡ breach --cluster #6effbe
'''
txt1 = Message(titlepanel, text=msg1, width=444, bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal"))
txt1.grid(row=0, column=0, sticky='NW')
txt2 = Message(titlepanel, text=msg2, width=444, bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal"))
txt2.grid(row=0, column=1, sticky='NEW')
txt3 = Message(titlepanel, text=msg3, width=444, bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal"))
txt3.grid(row=0, column=2, sticky='NE')
titlepanel.grid_columnconfigure(0, weight=1)
titlepanel.grid_columnconfigure(1, weight=1)
titlepanel.grid_columnconfigure(2, weight=1)

#root.tk.call("source", r"C:\Users\Administrator\Desktop\tcl\theme\Forest\void.tcl")
style = ttk.Style()
#style.theme_use('void')
style.configure("Treeview", background=colorbg, foreground=colorfg, fieldbackground=colorbg)
style.map('Treeview', background=[ ('selected', '#6effbe') ], foreground=[ ('selected', '#000000') ])

def preview_clipboard():
	try:
		global msg2_2
		#msg2_2 = msg2_2+root.clipboard_get()
		msg2_2 = msg2+r'┌─[ Clipboard:Text ]─[ /dev/void ]'+'\n'
		temp1 = root.clipboard_get().split('\n')
		for i in temp1[:10]:
			msg2_2 = msg2_2+r'| '+i[:55]+'\n'
		msg2_2 = msg2_2+r'└── ‡ limit --head 10'
		txt2.configure(text=msg2_2)
		preview_file()
	except: txt2.configure(text=msg2+'Clipboard failure')

def preview_file():
	try:
		if os.path.isfile(fullpath):
			msg2_3 = msg2_2+'\n\n'+r'┌─[File]─[ %s ]' % fullpath[-44:] +'\n'
			file = open(fullpath, mode='r')
			filecontent = file.read()
			file.close()
			filecontent = filecontent.split("\n")
			for i in filecontent[:33]:
				msg2_3 = msg2_3+r'| '+i[:55]+'\n'
			msg2_3 = msg2_3+r'└── ‡ limit --head 33'
			txt2.configure(text=msg2_3)
	except: txt2.configure(text=msg2_2+'Preview failure')

def toggle_sidebar(*event):
	global hidden
	global root
	
	if (hidden == False):
		root.withdraw()
		taskbar.withdraw()
		titlepanel.withdraw()
		sidebar.attributes('-alpha', 0.1)
		sidebar.geometry("1x690+0+50")
	else:
		root.deiconify()
		taskbar.deiconify()
		titlepanel.deiconify()
		sidebar.attributes('-alpha', 1.0)
		sidebar.geometry("1x740+0+0")
		preview_clipboard()
	hidden = not hidden

	root.focus_set()

def menu_open():
	toggle_sidebar()
	#subprocess.Popen(r'explorer /select,"C:\xampp"')
	subprocess.Popen(r'explorer '+fullpath)

def menu_edit():
	toggle_sidebar()
	#if os.path.isfile(path):
	subprocess.Popen(['C:\Program Files\Sublime Text 3\sublime_text.exe', fullpath], start_new_session=True)

def menu_select():
	node = tree.focus()
	if tree.parent(node):
		if os.path.isdir(fullpath):
			os.chdir(fullpath)
			tree.delete(tree.get_children(''))
			populate_roots(tree)

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

def open_popup():
	global dialog
	newFileName.set(str(round(time.time()))+r' ¦ ')

	dialog = Toplevel(root)
	dialog.geometry("250x100+333+25")
	dialog.resizable(False, False)
	dialog.title("Child Window")
	dialog.columnconfigure(0, weight=1)
	Label(dialog, text='Enter File or Folder name').grid()
	Entry(dialog, textvariable=newFileName).grid(column=0, pady=10, sticky='NSEW')
	Button(dialog, text="Create", command=newFileOrFolder).grid(pady=10, sticky='NSEW')

def newFileOrFolder():
	if os.path.isdir(fullpath): fullpath2 = fullpath
	if os.path.isfile(fullpath): fullpath2 = os.path.split(fullpath)[0]
	if len(newFileName.get().split('.')) != 1:
		open(os.path.join(fullpath2, newFileName.get()), 'w').close()
	else:
		os.mkdir(os.path.join(fullpath2, newFileName.get()))
	dialog.destroy()
	populate_tree(tree, tree.focus())

newFileName = StringVar(root, "", 'new_name')
#currentPath = StringVar(root, name='currentPath', value=pathlib.Path.cwd())
#currentPath.trace('w', pathChange)

def workspace_click():
	combo1.configure(state="readonly")
	file = open(ZLCORE+r'\Toolbar\F\[ Workspace ]\[ Sidebar ]\Internal.txt', mode='r')
	filecontent = file.read()
	file.close()
	filecontent = filecontent.split("\n")
	combo1['values'] = filecontent

def workspace_select():
	global fullpath
	combo1.configure(width=len(combo1.get())+1)
	fullpath = ZLCORE+'\\Toolbar\\F\\[ Workspace ]\\[ Sidebar ]\\'+combo1.get()
	if os.path.isdir(fullpath):
		os.chdir(fullpath)
		tree.delete(tree.get_children(''))
		populate_roots(tree)

sidebar.bind("<Button-1>", toggle_sidebar)
root.bind("<Alt-Up>", goBack)
#root.bind("<FocusOut>", exit)

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
combo1 = ttk.Combobox(frame3_2, state="readonly", values=['--------------'], width=1)
combo1.grid(sticky='E', row=0, column=0)
combo1.bind('<Button-3>', lambda e: combo1.configure(state="normal"))
combo1.bind('<Button-1>', lambda e: workspace_click())
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


menubar = Menu(root, tearoff=0)
menubar.add_command(label="New", command=open_popup)
menubar.add_separator()
menubar.add_command(label="Open", command=menu_open)
menubar.add_command(label="Edit", command=menu_edit)
menubar.add_command(label="Select", command=menu_select)
menubar.add_separator()
menubar.add_command(label="Copy path", command=lambda: (root.clipboard_clear(),root.clipboard_append(fullpath),root.update()))
#menubar.add_command(label="Exit", command=menu_clear)
#menubar.add_command(label="Exit", command=root.quit)
#root.config(menu=menubar)
tree.bind("<Button-3>", lambda event: menubar.post(event.x_root, event.y_root))

sidebar.mainloop()
