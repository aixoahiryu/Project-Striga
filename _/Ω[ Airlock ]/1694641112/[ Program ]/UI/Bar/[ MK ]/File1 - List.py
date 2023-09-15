import os
import subprocess
import pathlib
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted

home = r'D:\_'
picked = ''
path = home
hidden = False

colorbg = "#000000"
colorfg = "#ffffff"

sidebar = Tk()
sidebar.attributes('-topmost', True)
sidebar.attributes('-alpha', 0.1)
sidebar.title('1px')
sidebar.geometry("1x740+0+150")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)

#root = Tk()
root = Toplevel(sidebar)
root.title('===[ Sidebar: File ]===')
root.attributes('-topmost', True)
root.geometry("444x740+1+0")
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
	hidden = not hidden
	if (hidden == False): root.withdraw()
	else: root.deiconify()
	list.focus_set()

def pathChange(*event):
	global path
	path = currentPath.get()
	dirlist = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
	filelist = [x for x in os.listdir(path) if not os.path.isdir(os.path.join(path, x))]
	dirlist = os_sorted(dirlist)
	filelist = os_sorted(filelist)
	#directory = os.listdir(currentPath.get())
	#directory = os.scandir(currentPath.get())
	#directory.sort(reverse = True)
	#sorted(lis, key=abs, reverse=True)

	list.delete(0, END)
	#for file in directory:
	#for i,item in enumerate(dirlist + filelist):
	#	list.insert(END, item)
	for item in dirlist:
		list.insert(END, item)
	list.insert(END, "-----------------------------------------------------------------------------------")
	for item in filelist:
		list.insert(END, item)
	list.insert(0, "..")

def goBack(event=None):
	newPath = pathlib.Path(currentPath.get()).parent
	currentPath.set(newPath)
	print('Going Back')

def goHome(event=None):
	currentPath.set(home)
	# simple message
	print('Going home')

def changePathByClick(event=None):
	global picked
	picked = list.get(list.curselection()[0])
	if (picked == '..'):
		goBack()
		return
	global path
	path = os.path.join(currentPath.get(), picked)
	if os.path.isfile(path):
		print('Opening: '+path)
		os.startfile(path)
	else:
		currentPath.set(path)

def open_popup():
	global top
	top = Toplevel(root)
	top.geometry("250x150+444+0")
	top.resizable(False, False)
	top.title("Child Window")
	top.columnconfigure(0, weight=1)
	Label(top, text='Enter File or Folder name').grid()
	Entry(top, textvariable=newFileName).grid(column=0, pady=10, sticky='NSEW')
	Button(top, text="Create", command=newFileOrFolder).grid(pady=10, sticky='NSEW')

def newFileOrFolder():
	if len(newFileName.get().split('.')) != 1:
		open(os.path.join(currentPath.get(), newFileName.get()), 'w').close()
	else:
		os.mkdir(os.path.join(currentPath.get(), newFileName.get()))
	top.destroy()
	pathChange()

def menu_open():
	toggle_sidebar()
	#subprocess.Popen(r'explorer /select,"C:\xampp"')
	subprocess.Popen(r'explorer '+path)

def menu_edit():
	toggle_sidebar()
	#if os.path.isfile(path):
	subprocess.Popen(['C:\Program Files\Sublime Text 3\sublime_text.exe', path], start_new_session=True)

def menu_clear():
	#os.execv(sys.argv[0], sys.argv)
	os.execv(sys.executable, ['python'] + sys.argv)

sidebar.bind("<Button-1>", toggle_sidebar)
top = ''

newFileName = StringVar(root, "", 'new_name')
currentPath = StringVar(
	root,
	name='currentPath',
	value=pathlib.Path.cwd()
)
currentPath.trace('w', pathChange)

Button(root, text='≡', command=goHome).grid(sticky='NSEW', column=0, row=0)

frame1 = Frame(root, bg=colorbg)
frame1.grid(sticky='NSEW', column=0, row=1)
button1 = Button(frame1, text='∆', command=goBack)
button2 = Button(frame1, text='X', command=goBack)
button1.grid(sticky='N', row=0)
button2.grid(sticky='N', row=1)
#button1.place(relx=0, rely=0, relwidth=0.1, relheight=0.1)

root.bind("<Alt-Up>", goBack)
#root.bind("<FocusOut>", exit)

Entry(root, textvariable=currentPath, bg=colorbg, fg=colorfg).grid(sticky='NSEW', column=1, row=0, ipady=0, ipadx=0)

list = Listbox(root, bg=colorbg, fg=colorfg)
list.grid(sticky='NSEW', column=1, row=1, ipady=10, ipadx=10)

list.bind('<Double-1>', changePathByClick)
list.bind('<Return>', changePathByClick)


menubar = Menu(root)
menubar.add_command(label="New", command=open_popup)
menubar.add_command(label="Open", command=menu_open)
menubar.add_command(label="Edit", command=menu_edit)
menubar.add_command(label="Select", command=menu_edit)
menubar.add_command(label="Exit", command=menu_clear)
menubar.add_command(label="[Exit]", command=root.quit)
root.config(menu=menubar)

currentPath.set(home)
pathChange('')

sidebar.mainloop()