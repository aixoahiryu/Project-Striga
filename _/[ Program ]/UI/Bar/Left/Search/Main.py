import webbrowser
import os
import pathlib
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted

hidden = False
os.chdir('Search')
cwd = os.getcwd()

colorbg = "#000000"
colorfg = "#ffffff"

sidebar = Tk()
sidebar.attributes('-topmost', True)
sidebar.attributes('-alpha', 0.1)
sidebar.title('1px')
sidebar.geometry("1x150+0+0")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)

#root = Tk()
root = Toplevel(sidebar)
root.title('===[ Sidebar: File ]===')
root.attributes('-topmost', True)
root.geometry("333x740+1+25")
root.overrideredirect(1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)
#root.configure(background="#000000")
#root.configure(highlightbackground="#000000")
#root.configure(highlightcolor="white")

taskbar = Toplevel(sidebar)
taskbar.attributes('-topmost', True)
taskbar.title('1px')
taskbar.geometry("1366x25+1+0")
taskbar.overrideredirect(1)
taskbar.configure(bg=colorbg)
Label(taskbar, text=r'[ Network ]', background=colorbg, foreground=colorfg).place(relx=0.444, rely=0)
taskbar.bind("<Button-1>", lambda event: root.withdraw())

#ttk.Style().theme_use('alt')

def toggle_sidebar(*event):
	global hidden
	global root
	global searchbox

	if (hidden == False):
		root.withdraw()
		taskbar.withdraw()
		sidebar.attributes('-alpha', 0.1)
		sidebar.geometry("1x150+0+0")
	else:
		root.deiconify()
		taskbar.deiconify()
		sidebar.attributes('-alpha', 1.0)
		sidebar.geometry("1x740+0+0")
	hidden = not hidden

	searchbox.focus_set()
	searchbox.selection_range(0, END)

def menu_clear():
	#os.execv(sys.argv[0], sys.argv)
	os.execv(sys.executable, ['python'] + sys.argv)

def engine(id):
	print(id)
	search()

def search(*event):
	engine = {'Google': 'https://www.google.com/search?q=%s&num=100&nfpr=1',\
	'Yandex': 'https://yandex.com/search/?text=%s',\
	'Bing': 'https://www.bing.com/search?q=%s',\
	}
	searchstr = searchbox2.get()+' '+searchbox.get()+' '+searchbox3.get()
	webbrowser.open(engine[enginebox.get()] % searchstr, new=2, autoraise=True)
	#webbrowser.open(r'https://www.google.com/search?q='+searchbox.get()+' '+searchbox2.get()+' '+searchbox3.get()+r'&num=100&nfpr=1', new=2, autoraise=True)

def change_file(*event):
	list2.delete(0, END)
	picked = list1.get(list1.curselection()[0])
	path = os.path.join(cwd, picked)
	file = open(picked, mode='r')
	filecontent = file.read()
	file.close()
	filecontent = filecontent.split("\n")
	for item in filecontent:
		list2.insert(END, item)

def edit_file(*event):
	picked = list1.get(list1.curselection()[0])
	path = os.path.join(cwd, picked)
	os.startfile(path)

def change_filter(*event):
	picked = list2.get(list2.curselection()[0])
	searchbox3.delete(0, END)
	searchbox3.insert(0, picked)

sidebar.bind("<Button-1>", toggle_sidebar)
Button(root, text='≡', command=search, bg=colorbg, fg=colorfg).grid(sticky='NSEW', column=0, row=0)

frame1 = Frame(root, bg=colorbg)
frame1.grid(sticky='NSEW', column=0, row=1)
Button(frame1, text='G', command=search, bg=colorbg, fg=colorfg).grid(sticky='N', row=0)
Button(frame1, text='Y', command=search, bg=colorbg, fg=colorfg).grid(sticky='N', row=1)
Button(frame1, text='B', command=search, bg=colorbg, fg=colorfg).grid(sticky='N', row=2)
ttk.Separator(frame1, orient='horizontal').grid(sticky='EW', row=3)
Button(frame1, text='yt', command=search, bg=colorbg, fg=colorfg).grid(sticky='N', row=4)

frame2 = Frame(root, bg=colorbg)
frame2.grid(sticky='NSEW', column=1, row=1, ipady=10, ipadx=10)
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_rowconfigure(3, weight=1)
searchbox2 = Entry(frame2, bg=colorbg, fg=colorfg)
searchbox2.grid(sticky='NSEW', row=0)
searchbox2.bind('<Return>', search)
searchbox3 = Entry(frame2, bg=colorbg, fg=colorfg)
searchbox3.grid(sticky='NSEW', row=1)
searchbox3.bind('<Return>', search)
enginebox = ttk.Combobox(frame2)
enginebox.grid(sticky='NSEW', row=2)
enginebox.configure(values=['Google','Yandex','Bing'])
enginebox.set('Google')
fileframe = Frame(frame2, bg=colorbg)
fileframe.grid(sticky='NSEW', row=3)
fileframe.grid_columnconfigure(1, weight=1)
fileframe.grid_rowconfigure(0, weight=1)
list1 = Listbox(fileframe, bg=colorbg, fg=colorfg)
list1.grid(sticky='NSEW', row=0, column=0)
list2 = Listbox(fileframe, bg=colorbg, fg=colorfg)
list2.grid(sticky='NSEW', row=0, column=1)
list1.bind('<Double-1>', change_file)
list1.bind('<Button-3>', edit_file)
list2.bind('<Double-1>', change_filter)

searchbox = Entry(root, bg=colorbg, fg=colorfg)
searchbox.grid(sticky='NSEW', column=1, row=0)
searchbox.bind('<Return>', search)


#menubar = Menu(root)
#menubar.add_command(label="Exit", command=menu_clear)
#menubar.add_command(label="Exit", command=root.quit)
#root.config(menu=menubar)

filelist = [x for x in os.listdir(cwd) if not os.path.isdir(os.path.join(cwd, x))]
filelist = os_sorted(filelist)
for item in filelist:
	list1.insert(END, item)

sidebar.mainloop()