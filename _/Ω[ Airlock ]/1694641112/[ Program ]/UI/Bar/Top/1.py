import os
import glob
import subprocess
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted


ZLCORE = os.environ['ZLCORE']
home = r'D:\ZL-Core\Toolbar\F'
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
sidebar.geometry("444x1+1+0")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)

#root = Tk()
root = Toplevel(sidebar)
root.title('===[ Sidebar: File ]===')
root.attributes('-topmost', True)
root.geometry("444x740+0+1")
root.overrideredirect(1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)
#root.configure(background="#000000")
#root.configure(highlightbackground="#000000")
#root.configure(highlightcolor="white")

style = ttk.Style()
#style.theme_use('alt')
style.configure("Treeview", background=colorbg, foreground=colorfg, fieldbackground=colorbg)
style.map('Treeview', background=[ ('selected', '#6effbe') ], foreground=[ ('selected', '#000000') ])

def toggle_sidebar(*event):
	global hidden
	global root
	hidden = not hidden
	if (hidden == False): root.withdraw()
	else: root.deiconify()
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
	dialog = Toplevel(root)
	dialog.geometry("250x150+444+0")
	dialog.resizable(False, False)
	dialog.title("Child Window")
	dialog.columnconfigure(0, weight=1)
	Label(dialog, text='Enter File or Folder name').grid()
	Entry(dialog, textvariable=newFileName).grid(column=0, pady=10, sticky='NSEW')
	Button(dialog, text="Create", command=newFileOrFolder).grid(pady=10, sticky='NSEW')

def newFileOrFolder():
	if os.path.isdir(fullpath):
		if len(newFileName.get().split('.')) != 1:
			open(os.path.join(fullpath, newFileName.get()), 'w').close()
		else:
			os.mkdir(os.path.join(fullpath, newFileName.get()))
		dialog.destroy()
		populate_tree(tree, tree.focus())

newFileName = StringVar(root, "", 'new_name')
#currentPath = StringVar(root, name='currentPath', value=pathlib.Path.cwd())
#currentPath.trace('w', pathChange)

sidebar.bind("<Button-1>", toggle_sidebar)
root.bind("<Alt-Up>", goBack)
#root.bind("<FocusOut>", exit)

menubar = Menu(root)
menubar.add_command(label="New", command=open_popup)
menubar.add_command(label="Open", command=menu_open)
menubar.add_command(label="Edit", command=menu_edit)
menubar.add_command(label="Select", command=menu_select)
#menubar.add_command(label="Exit", command=menu_clear)
menubar.add_command(label="Exit", command=root.quit)
root.config(menu=menubar)

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
frame3.grid(sticky='NSEW', column=1, row=0, ipady=0, ipadx=0)
Button(frame3, text='Network', bg=colorbg, fg=colorfg, command=lambda: goPath(r'D:\ZL-Core\Toolbar\F\[ Network ]')).grid(sticky='W', row=0, column=0)
#ttk.Separator(frame3, orient='vertical').grid(sticky='NS', row=0, column=1)
Label(frame3, text='|', bg=colorbg, fg=colorfg).grid(sticky='W', row=0, column=1)
Button(frame3, text='U', bg=colorbg, fg=colorfg, command=lambda: goPath(r'D:\ZL-Core\Toolbar\F\Utility')).grid(sticky='W', row=0, column=2)
Button(frame3, text='C', bg=colorbg, fg=colorfg, command=lambda: goPath(r'D:\ZL-Core\Toolbar\F\Content')).grid(sticky='W', row=0, column=3)
#Button(frame3, text='Data', bg=colorbg, fg=colorfg, command=lambda: goPath('D:\\Data')).grid(sticky='W', row=0, column=3)
#Button(frame3, text='Core', bg=colorbg, fg=colorfg, command=lambda: goPath('D:\\ZL-Core')).grid(sticky='W', row=0, column=4)

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
tree.column("size", stretch=0, width=100)
#tree['show'] = ('headings', 'tree')

populate_roots(tree)
tree.bind('<<TreeviewOpen>>', update_tree)
tree.bind('<Double-Button-1>', change_dir)
tree.bind('<ButtonRelease-1>', selectItem)

sidebar.mainloop()