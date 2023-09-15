import webbrowser
import os
import pathlib
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted

hidden = False

colorbg = "#ffffff"
colorfg = "#000000"

sidebar = Tk()
sidebar.attributes('-topmost', True)
sidebar.attributes('-alpha', 0.1)
sidebar.title('1px')
sidebar.geometry("1x50+1365+0")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)

#root = Tk()
root = Toplevel(sidebar)
root.title('===[ Sidebar: File ]===')
root.attributes('-topmost', True)
root.geometry("443x740+922+0")
root.overrideredirect(1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)
#root.configure(background="#000000")
#root.configure(highlightbackground="#000000")
#root.configure(highlightcolor="white")

ttk.Style().theme_use('alt')

def toggle_sidebar(*event):
	global hidden
	global root
	global searchbox

	hidden = not hidden
	if (hidden == False): root.withdraw()
	else: root.deiconify()
	searchbox.focus_set()
	searchbox.selection_range(0, END)

def menu_clear():
	#os.execv(sys.argv[0], sys.argv)
	os.execv(sys.executable, ['python'] + sys.argv)

sidebar.bind("<Button-1>", toggle_sidebar)
top = ''

Button(root, text='≡', command=menu_clear, bg=colorbg, fg=colorfg).grid(sticky='NSEW', column=0, row=0)

frame1 = Frame(root, bg=colorbg)
frame1.grid(sticky='NSEW', column=0, row=1)
Button(frame1, text='G', command=menu_clear, bg=colorbg, fg=colorfg).grid(sticky='N', row=0)
Button(frame1, text='Y', command=menu_clear, bg=colorbg, fg=colorfg).grid(sticky='N', row=1)
Button(frame1, text='B', command=menu_clear, bg=colorbg, fg=colorfg).grid(sticky='N', row=2)
ttk.Separator(frame1, orient='horizontal').grid(sticky='EW', row=3)
Button(frame1, text='yt', command=menu_clear, bg=colorbg, fg=colorfg).grid(sticky='N', row=4)

frame2 = Frame(root, bg=colorbg)
frame2.grid(sticky='NSEW', column=1, row=1, ipady=10, ipadx=10)

searchbox = Entry(root, bg=colorbg, fg=colorfg)
searchbox.grid(sticky='NSEW', column=1, row=0, ipady=0, ipadx=0)


menubar = Menu(root)
#menubar.add_command(label="Exit", command=menu_clear)
menubar.add_command(label="Exit", command=root.quit)
root.config(menu=menubar)

sidebar.mainloop()