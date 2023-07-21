import webbrowser
import os
import subprocess
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted

ZLCORE = os.environ['ZLCORE']
hidden = False

darkmode = False
colorbg = "#000000" if darkmode else "#ffffff"
colorbg2 = "#253B34" if darkmode else "#6effbe"
colorfg = "#ffffff" if darkmode else "#000000"

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

overflow = Toplevel(sidebar)
overflow.title('Icon overflow')
overflow.geometry("+0-25")
overflow.overrideredirect(1)
overflow.configure(bg=colorbg)
#overflow.transient(taskbar)
overflow.attributes('-topmost', True)
imggemini=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\cpub.png')
Button(overflow, text=' Thaumiel', relief='flat', background=colorbg, foreground=colorfg, image=imggemini, compound='left').grid(column=0, row=0, sticky='NW')
imgeye=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\cpub.png')
Button(overflow, text=' The eye', relief='flat', background=colorbg, foreground=colorfg, image=imgeye, compound='left').grid(column=0, row=1, sticky='NW')
imgmoon=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\cpub.png')
Button(overflow, text=' Moon cycle', relief='flat', background=colorbg, foreground=colorfg, image=imgmoon, compound='left').grid(column=0, row=2, sticky='NW')
imgsun=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\cpub.png')
Button(overflow, text=' Sun cycle', relief='flat', background=colorbg, foreground=colorfg, image=imgsun, compound='left').grid(column=0, row=3, sticky='NW')
imgdice=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\cpub.png')
Button(overflow, text=' Chaos theory', relief='flat', background=colorbg, foreground=colorfg, image=imgdice, compound='left').grid(column=0, row=4, sticky='NW')
imgcalendar=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\cpub.png')
Button(overflow, text=' Calendar', relief='flat', background=colorbg, foreground=colorfg, image=imgcalendar, compound='left').grid(column=0, row=5, sticky='NW')
imghorse=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\cpub.png')
Button(overflow, text=' Strategy', relief='flat', background=colorbg, foreground=colorfg, image=imghorse, compound='left').grid(column=0, row=6, sticky='NW')
imgwave=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\cpub.png')
Button(overflow, text=' Flunctuation', relief='flat', background=colorbg, foreground=colorfg, image=imgwave, compound='left').grid(column=0, row=7, sticky='NW')
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
taskbar.geometry("1366x30+0-0")
taskbar.overrideredirect(1)
taskbar.grid_rowconfigure(0, weight=1)
taskbar.configure(bg=colorbg)
#Label(taskbar, text=r'[ Workspace ]', background=colorbg, foreground=colorfg).place(relx=0.48, rely=0)
appframe = Frame(taskbar, bg=colorbg)
appframe.grid(sticky='NSW', column=0, row=0)
appframe.grid_rowconfigure(0, weight=1)
imgmenu=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\menu2b.png')
btnoverflow = Button(appframe, text='', relief='flat', background=colorbg, foreground=colorfg, image=imgmenu, compound='left')
btnoverflow.grid(column=0, row=0, sticky='NSW')
btnoverflow.bind("<Button-1>", lambda event: toggle_overflow())
quickframe = Frame(taskbar, bg=colorbg)
quickframe.grid(sticky='NSW', column=1, row=0)
quickframe.grid_rowconfigure(0, weight=1)
imgbrowser=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\eye2b.png')
Button(quickframe, text='', relief='flat', background=colorbg, foreground=colorfg, image=imgbrowser, compound='left').grid(column=0, row=0, sticky='NSW')
imgproxy=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\proxyb.png')
Button(quickframe, text='', relief='flat', background=colorbg, foreground=colorfg, image=imgproxy, compound='left').grid(column=1, row=0, sticky='NSW')
programframe = Frame(taskbar, bg=colorbg)
programframe.grid(sticky='NSW', column=2, row=0)
programframe.grid_rowconfigure(0, weight=1)
Button(programframe, text='[ Main ]', relief='flat', background=colorbg, foreground=colorfg).grid(column=0, row=0, sticky='NSW')
Button(programframe, text='Peripheral', relief='flat', background=colorbg, foreground=colorfg).grid(column=1, row=0, sticky='NSW')
Button(programframe, text='Transient', relief='flat', background=colorbg, foreground=colorfg).grid(column=2, row=0, sticky='NSW')
trayframe = Frame(taskbar, bg=colorbg)
trayframe.grid(sticky='NSE', column=3, row=0)
trayframe.grid_rowconfigure(0, weight=1)
taskbar.grid_columnconfigure(3, weight=1)
Button(trayframe, text=' F ', relief='flat', background=colorbg, foreground=colorfg).grid(column=0, row=0, sticky='NSW')
Button(trayframe, text=' N ', relief='flat', background=colorbg, foreground=colorfg).grid(column=1, row=0, sticky='NSW')
Button(trayframe, text=' _ ', relief='flat', background=colorbg, foreground=colorfg).grid(column=2, row=0, sticky='NSW')
imgrect=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\cornerb.png')
Button(trayframe, text='', relief='flat', background=colorbg, foreground=colorfg, image=imgrect, compound='left').grid(column=3, row=0, sticky='NSW')
imghardware=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\cpub.png')
Button(trayframe, text=' System', relief='flat', background=colorbg, foreground=colorfg, image=imghardware, compound='left').grid(column=4, row=0, sticky='NSW')
imgmonitoring=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\motherboardb.png')
Button(trayframe, text=' Manager', relief='flat', background=colorbg, foreground=colorfg, image=imgmonitoring, compound='left').grid(column=5, row=0, sticky='NSW')
imgcalendar=PhotoImage(file=ZLCORE+r'\Toolbar\_\[ Program ]\[ Source ]\gif\bw\calendarb.png')
Button(trayframe, text=' Z[1.95996|97.5] 54.7356° π[3.14159] √[1.41421] ϕ[1.61803]', relief='flat', background=colorbg, foreground=colorfg, image=imgcalendar, compound='left').grid(column=6, row=0, sticky='NSW')
Button(trayframe, text=' ', relief='flat', background=colorbg, foreground=colorfg).grid(column=7, row=0, sticky='NSW')
#taskbar.bind("<Button-1>", lambda event: (root.withdraw(), sidebar.geometry("1366x1+0+0"), taskbar.geometry("1366x24+0+1")))
taskbar.bind("<Button-1>", lambda event: root.withdraw())

ttk.Style().theme_use('alt')

def toggle_sidebar(*event):
	global hidden, root, searchbox, overflow_on
	
	if (hidden == False):
		root.withdraw()
		taskbar.withdraw()
	else:
		root.deiconify()
		taskbar.deiconify()
	hidden = not hidden
	if overflow_on:
		overflow.withdraw()
		overflow_on = False

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


taskbar.bind("<Enter>", lambda e: root.withdraw())
sidebar.mainloop()