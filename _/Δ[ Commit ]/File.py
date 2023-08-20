import Zeta

import time
import os
import glob
import subprocess
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted


ZLCORE = os.environ['ZLCORE']
home = r'D:\Data'
#os.chdir(home)

cwd = os.getcwd()
hidden = False

addicon = False
darkmode = True
tooltip = True
colorbg = "#000000" if darkmode else "#ffffff"
colorbg2 = "#253B34" if darkmode else "#6effbe"
colorfg = "#ffffff" if darkmode else "#000000"


class FileBox(Frame):
	def __init__(self, master, controller, title='Title', color=7, color2=''):
		self.fullpath = home
		self.parent = controller
		self.dialog = ''
		self.newFileName = StringVar(master, "", 'new_name')
		Button(master, text='≡', command=self.goHome, bg=colorbg, fg=colorfg).grid(sticky='NSEW', column=0, row=0)

		frame1 = Frame(master, bg=colorbg)
		frame1.grid(sticky='NSEW', column=0, row=1)
		button1 = Button(frame1, text='∆', command=self.goBack, bg=colorbg, fg=colorfg)
		button2 = Button(frame1, text='X', command=self.goBack, bg=colorbg, fg=colorfg)
		button1.grid(sticky='N', row=0)
		button2.grid(sticky='N', row=1)
		#button1.place(relx=0, rely=0, relwidth=0.1, relheight=0.1)
		Frame.__init__(self, master)
		self.grid(sticky='NSEW', column=1, row=1)

		#Entry(master, textvariable=currentPath, bg=colorbg, fg=colorfg)
		frame3 = Frame(master, bg=colorbg)
		frame3.grid(sticky='NSEW', column=1, row=0)
		frame3_1 = Frame(frame3, bg=colorbg)
		frame3_1.grid(sticky='W', row=0, column=0)
		Button(frame3_1, text='C', bg=colorbg, fg=colorfg, command=lambda: self.goPath('C:\\')).grid(sticky='W', row=0, column=0)
		Button(frame3_1, text='D', bg=colorbg, fg=colorfg, command=lambda: self.goPath('D:\\')).grid(sticky='W', row=0, column=1)
		Label(frame3_1, text='|', bg=colorbg, fg=colorfg).grid(sticky='W', row=0, column=2)
		Button(frame3_1, text='╬', bg=colorbg, fg=colorfg, command=lambda: self.goPath(r'D:\MEGA\ZL-Core\Commit\╬')).grid(sticky='W', row=0, column=3)
		Button(frame3_1, text='_', bg=colorbg, fg=colorfg, command=lambda: self.goPath('D:\\_')).grid(sticky='W', row=0, column=4)
		Button(frame3_1, text='Data', bg=colorbg, fg=colorfg, command=lambda: self.goPath('D:\\Data')).grid(sticky='W', row=0, column=5)
		Button(frame3_1, text='Core', bg=colorbg, fg=colorfg, command=lambda: self.goPath('D:\\ZL-Core')).grid(sticky='W', row=0, column=6)
		Button(frame3_1, text='Scraps', bg=colorbg, fg=colorfg, command=lambda: self.goPath('D:\\Scraps')).grid(sticky='W', row=0, column=7)
		frame3_2 = Frame(frame3, bg=colorbg)
		frame3_2.grid(sticky='E', row=0, column=1)
		frame3.grid_columnconfigure(1, weight=1)
		combo1 = ttk.Combobox(frame3_2, state="readonly", values=['--------------'], width=10)
		combo1.grid(sticky='E', row=0, column=0)
		combo1.bind('<Button-3>', lambda e: combo1.configure(state="normal"))
		combo1.bind('<Button-1>', lambda e: self.workspace_select())
		combo1.bind('<<ComboboxSelected>>', lambda e: self.workspace_select())

		vsb = ttk.Scrollbar(self, orient="vertical")
		hsb = ttk.Scrollbar(self, orient="horizontal")
		self.tree = ttk.Treeview(self, columns=("fullpath", "type", "size"), show="tree",
			displaycolumns="size", yscrollcommand=lambda f, l: self.autoscroll(vsb, f, l),
			xscrollcommand=lambda f, l:self.autoscroll(hsb, f, l))
		vsb['command'] = self.tree.yview
		hsb['command'] = self.tree.xview
		self.tree.grid(column=0, row=0, sticky='NSEW')
		vsb.grid(column=1, row=0, sticky='ns')
		hsb.grid(column=0, row=1, sticky='ew')
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)

		self.tree.heading("#0", text="Directory Structure", anchor='w')
		self.tree.heading("size", text="File Size", anchor='w')
		self.tree.column("size", stretch=0, width=0)
		#tree['show'] = ('headings', 'tree')

		self.populate_masters(self.tree)
		self.tree.bind('<<TreeviewOpen>>', self.update_tree)
		self.tree.bind('<Double-Button-1>', self.change_dir)
		self.tree.bind('<ButtonRelease-1>', self.selectItem)


		#menubar = Menu(master, tearoff=0, background='#ffffff', foreground='#000000', activebackground='#000000', activeforeground='#ffffff')
		menubar = Menu(master, tearoff=0)
		menubar.add_command(label="New", command=self.open_popup)
		menubar.add_separator()
		menubar.add_command(label="Open", command=lambda: (self.parent.toggle_sidebar(), Zeta.System.OS.open(self.fullpath)))
		#subedit = Menu(menubar, tearoff=0)
		#menubar.add_cascade(label="Edit", menu=subedit, command=menu_edit)
		menubar.add_command(label="Edit", command=lambda: (self.parent.toggle_sidebar(), Zeta.System.OS.edit(self.fullpath)))
		menubar.add_command(label="Select", command=self.menu_select)
		menubar.add_separator()
		menubar.add_command(label="Copy path", command=lambda: (self.parent.window.clipboard_clear(),self.parent.window.clipboard_append(self.fullpath),self.parent.window.update()))
		menubar.add_command(label="Go to path", command=lambda: self.menu_select(self.parent.window.clipboard_get()))
		menubar.add_command(label="Terminal", command=lambda: (self.parent.toggle_sidebar(), Zeta.System.OS.terminal(self.fullpath)))
		menubar.add_command(label="Detach", command=self.menu_select)
		#menubar.add_command(label="Exit", command=menu_clear)
		#menubar.add_command(label="Exit", command=master.quit)
		#master.config(menu=menubar)
		self.tree.bind("<Button-3>", lambda event: menubar.post(event.x_root, event.y_root))
		# self._color1 = Zeta.Color.Neon(color=color, color2=color2).hex
		# self._bg1 = Zeta.Color.Neon(color=color, color2=color2).hue

		# Frame.__init__(self, master, background=self._bg1)
		# top = Frame(self, background=self._bg1)
		# top.pack(side='top', expand=True, fill="both")
		# top.grid_columnconfigure(0, weight=1)
		# #body = Frame(self)
		
		# msg = Label(top, wraplength='4i', justify=LEFT, foreground=self._color1, background=self._bg1, font=("Courier New", 10, "normal"))
		# msg['text'] = title
		# msg.grid(row=0, column=0, sticky='NW')
		# btnframe = Frame(top, background=self._bg1)
		# btnframe.grid(row=0, column=1, sticky='E')
		# Button(btnframe, text=u'Ζ', relief='flat', foreground='#c9c9c9', background=self._bg1, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		# Button(btnframe, text=u'Α', relief='flat', foreground='#c9c9c9', background=self._bg1, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		# Button(btnframe, text=u'Σ', relief='flat', foreground='#c9c9c9', background=self._bg1, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		# Button(btnframe, text=u'Ω', relief='flat', foreground='#c9c9c9', background=self._bg1, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		# Button(btnframe, text=u'¦', relief='flat', foreground='#c9c9c9', background=self._bg1, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		# Button(btnframe, text='■', relief='flat', foreground=Zeta.Color.Neon(color2='green').hex, background=self._bg1, command=self.winfo_toplevel().destroy).pack(side='left')
		# Button(btnframe, text='■', relief='flat', foreground=Zeta.Color.Neon(color2='yellow').hex, background=self._bg1, command=self.winfo_toplevel().destroy).pack(side='left')
		# Button(btnframe, text='■', relief='flat', foreground=Zeta.Color.Neon(color2='red').hex, background=self._bg1, command=self.winfo_toplevel().destroy).pack(side='left')

	def menu_select(self, path=''):
		node = self.tree.focus()
		if self.tree.parent(node):
			if path!='': self.fullpath = path
			if os.path.isfile(self.fullpath): self.fullpath = os.path.split(self.fullpath)[0]
			self.tree.delete(self.tree.get_children(''))
			self.populate_masters(self.tree)

	def menu_clear():
		#os.execv(sys.argv[0], sys.argv)
		os.execv(sys.executable, ['python'] + sys.argv)

	def selectItem(self, a):
		selectedfocus = self.tree.focus()
		selecteditem = self.tree.item(selectedfocus)
		self.fullpath = selecteditem.get('values')[0]
		self.parent.preview_file()

	def populate_tree(self, tree, node):
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

	def populate_masters(self, tree):
		#dir = os.path.abspath('.').replace('\\', '/')
		dir = self.fullpath
		node = tree.insert('', 'end', text=dir, values=[dir, "directory"], open=True)
		self.populate_tree(tree, node)

	def update_tree(self, event):
		tree = event.widget
		self.populate_tree(tree, tree.focus())

	def change_dir(self, event):
		tree = event.widget
		node = tree.focus()
		if tree.parent(node):
			path = os.path.abspath(tree.set(node, "fullpath"))
			if os.path.isfile(path): os.startfile(path)
			# if os.path.isdir(path):
			# 	os.chdir(path)
			# 	tree.delete(tree.get_children(''))
			# 	populate_masters(tree)

	def autoscroll(self, sbar, first, last):
		first, last = float(first), float(last)
		if first <= 0 and last >= 1:
			sbar.grid_remove()
		else:
			sbar.grid()
		sbar.set(first, last)

	def goBack(self, event=None):
		self.fullpath = self.tree.item(self.tree.get_children('')).get('values')[0]
		#self.goPath(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
		self.goPath(os.path.abspath(os.path.join(self.fullpath, os.pardir)))

	def goHome(self, event=None):
		self.goPath(home)

	def goPath(self, path):
		self.fullpath = path
		self.tree.delete(self.tree.get_children(''))
		self.populate_masters(self.tree)

	def open_popup(self):
		self.newFileName.set('')
		
		self.dialog = Toplevel(self.parent.window)
		self.dialog.geometry("+333+25")
		self.dialog.resizable(False, False)
		self.dialog.title("New")
		self.dialog.transient(self.parent.window)
		self.dialog.columnconfigure(0, weight=1)
		Label(self.dialog, text='Enter File or Folder name').grid()
		Entry(self.dialog, textvariable=self.newFileName).grid(column=0, sticky='NSEW')
		btnframe = Frame(self.dialog)
		btnframe.grid(column=0, sticky='NSEW')
		Button(btnframe, text="Time", command=lambda: self.newFileName.set( str(round(time.time())) )).pack(side=LEFT)
		Button(btnframe, text="TXT", command=lambda: self.newFileName.set(self.newFileName.get()+'.txt')).pack(side=LEFT)
		Button(btnframe, text="[  ]", command=lambda: self.newFileName.set(r'[ '+self.newFileName.get()+r' ]')).pack(side=LEFT)
		Button(btnframe, text=" ¦ ", command=lambda: self.newFileName.set(self.newFileName.get()+r' ¦ ')).pack(side=LEFT)
		Button(btnframe, text=" √ ", command=lambda: self.newFileName.set(r'√ ')).pack(side=LEFT)
		Button(btnframe, text=" ≡ ", command=lambda: self.newFileName.set(r'≡ ')).pack(side=LEFT)
		Button(btnframe, text=" ▷ ", command=lambda: self.newFileName.set(r'▷ ')).pack(side=LEFT)
		Button(btnframe, text=" Δ ", command=lambda: self.newFileName.set(r'Δ[ '+self.newFileName.get()+r' ]')).pack(side=LEFT)
		Button(btnframe, text=" Σ ", command=lambda: self.newFileName.set(r'Σ[ '+self.newFileName.get()+r' ]')).pack(side=LEFT)
		Button(btnframe, text=" Ω ", command=lambda: self.newFileName.set(r'Ω[ '+self.newFileName.get()+r' ]')).pack(side=LEFT)
		Button(btnframe, text="Create", command=self.newFileOrFolder).pack(side=LEFT)

	def newFileOrFolder(self):
		if os.path.isdir(self.fullpath): fullpath2 = self.fullpath
		if os.path.isfile(self.fullpath): fullpath2 = os.path.split(self.fullpath)[0]
		if len(self.newFileName.get().split('.')) != 1:
			open(os.path.join(fullpath2, self.newFileName.get()), 'w').close()
		else:
			os.mkdir(os.path.join(fullpath2, self.newFileName.get()))
		self.dialog.destroy()
		if os.path.isdir(self.fullpath): self.populate_tree(self.tree, self.tree.focus())
		else: self.populate_tree(self.tree, self.tree.parent(self.tree.focus()))

	#currentPath = StringVar(master, name='currentPath', value=pathlib.Path.cwd())
	#currentPath.trace('w', pathChange)

	def workspace_select(self):
		combo1.configure(state="readonly")
		file = open(ZLCORE+r'\Toolbar\F\[ Workspace ]\[ Sidebar ]\Internal.txt', mode='r')
		filecontent = file.read()
		file.close()
		filecontent = filecontent.split("\n")
		combo1['values'] = filecontent

		#combo1.configure(width=len(combo1.get())+1)
		self.fullpath = ZLCORE+'\\Toolbar\\F\\[ Workspace ]\\[ Sidebar ]\\'+combo1.get()
		if os.path.isdir(self.fullpath):
			self.tree.delete(self.tree.get_children(''))
			self.populate_masters(self.tree)