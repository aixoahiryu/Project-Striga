import webbrowser
import os
import subprocess
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted

ZLCORE = os.environ['ZLCORE']
hidden = False

colorbg = "#ffffff"
colorfg = "#000000"

sidebar = Tk()
sidebar.attributes('-topmost', True)
sidebar.attributes('-alpha', 0.1)
sidebar.title('1px')
sidebar.geometry("1x270+1365+468")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)

#root = Tk()
root = Toplevel(sidebar)
root.title('===[ Sidebar: File ]===')
root.attributes('-topmost', True)
root.geometry("443x270+922+468")
root.overrideredirect(1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)
root.configure(background="#ffffff")
root.configure(highlightbackground="#000000")
root.configure(highlightcolor="#000000")

ttk.Style().theme_use('alt')

def toggle_sidebar(*event):
	global hidden
	global root
	global searchbox

	hidden = not hidden
	if (hidden == False): root.withdraw()
	else: root.deiconify()
	root.focus_set()

def menu_clear():
	#os.execv(sys.argv[0], sys.argv)
	os.execv(sys.executable, ['python'] + sys.argv)

sidebar.bind("<Button-1>", toggle_sidebar)
top = ''

frame0 = Frame(root, bg=colorbg)
frame0.grid(sticky='E', column=0, row=0, ipady=0, ipadx=0)
Button(frame0, text='[ Scraps ]', command=lambda: os.startfile(ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\[ Scraps ].txt'), bg=colorbg, fg=colorfg).grid(sticky='W', column=0, row=0)
Button(frame0, text='Active', command=lambda: os.startfile(ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\Active.txt'), bg=colorbg, fg=colorfg).grid(sticky='W', column=1, row=0)

frame1 = Frame(root, bg=colorbg)
frame1.grid(sticky='S', column=0, row=1)
Button(frame1, text='Proxy', command=lambda: os.startfile(ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\Proxy.py'), bg=colorbg, fg=colorfg).grid(sticky='N', row=0)
Button(frame1, text='Sticky', command=exit, bg=colorbg, fg=colorfg).grid(sticky='N', row=1)
#Button(frame1, text='B', command=menu_clear, bg=colorbg, fg=colorfg).grid(sticky='N', row=2)
#ttk.Separator(frame1, orient='horizontal').grid(sticky='EW', row=3)
#Button(frame1, text='yt', command=menu_clear, bg=colorbg, fg=colorfg).grid(sticky='N', row=4)

frame2 = Frame(root, bg=colorbg)
frame2.grid(sticky='NSEW', column=1, row=1)
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_rowconfigure(0, weight=1)
frame2_1 = Frame(frame2, bg=colorbg)
frame2_1.grid(sticky='SW', column=0, row=0)
Button(frame2_1, text='Breach', command=exit, bg='black', fg='white').grid(sticky='SW', row=0)
frame2_2 = Frame(frame2, bg=colorbg)
frame2_2.grid(sticky='SE', column=1, row=0)
Button(frame2_2, text='FastStone', bg=colorbg, fg=colorfg, command=lambda: os.startfile(r'D:\Tools\FSCapture97\FSCapture.exe')).grid(sticky='SE', row=0, column=0)
Button(frame2_2, text='mpv', bg=colorbg, fg=colorfg, command=lambda: os.startfile(r'C:\cygwin64\home\sidebar\mpv.vbs')).grid(sticky='SE', row=1, column=0)
Button(frame2_2, text='links2', bg=colorbg, fg=colorfg, command=lambda: os.startfile(r'D:\MEGA\ZL-Core\Toolbar\F\Utility\Links.lnk')).grid(sticky='SE', row=2, column=0)
nullbtn = Button(frame2_2, text='- Null', bg=colorbg, fg=colorfg, command=lambda: os.startfile(ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\- Null.py'))
nullbtn.grid(sticky='SE', row=3, column=0)
nullbtn.bind("<Button-3>", lambda e: subprocess.Popen(["C:\\Program Files\\Notepad++\\notepad++.exe", "-ro", ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\- Null.py'], start_new_session=True))

frame3 = Frame(root, bg=colorbg)
frame3.grid(sticky='E', column=1, row=0, ipady=0, ipadx=0)
Button(frame3, text='Experiment', bg=colorbg, fg=colorfg, command=lambda: os.startfile(ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\Experiment.txt')).grid(sticky='W', row=0, column=0)
Button(frame3, text='File', bg=colorbg, fg=colorfg, command=lambda: os.startfile(ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\File.txt')).grid(sticky='W', row=0, column=1)
Label(frame3, text='|', bg=colorbg, fg=colorfg).grid(sticky='W', row=0, column=2)
#Button(frame3, text='_', bg=colorbg, fg=colorfg, command=lambda: goPath('D:\\_')).grid(sticky='W', row=0, column=3)
#Button(frame3, text='Data', bg=colorbg, fg=colorfg, command=lambda: goPath('D:\\Data')).grid(sticky='W', row=0, column=4)
#Button(frame3, text='Core', bg=colorbg, fg=colorfg, command=lambda: goPath('D:\\ZL-Core')).grid(sticky='W', row=0, column=5)

linkbtn = Button(root, text='[ Link ]', command=lambda: os.startfile(ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\Link.py'), bg=colorbg, fg=colorfg)
linkbtn.configure(font="-family {Courier New} -size 20")
linkbtn.place(relx=0.284, rely=0.369, height=74, width=167)
linkbtn.bind("<Button-3>", lambda e: subprocess.Popen(["C:\\Program Files\\Notepad++\\notepad++.exe", "-ro", ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\Link.py'], start_new_session=True))


sidebar.mainloop()