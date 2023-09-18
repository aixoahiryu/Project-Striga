import Zeta

import webbrowser
import os
import pathlib
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted

hidden = False
# cwd = os.getcwd()
cwd = Zeta.System.Path.Core().ZETA + r'/Interface/External/Network/Search'

colorbg = "#000000"
colorfg = "#ffffff"

from Zeta.Panel import *

class Search(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='white', *args, **kwargs)
		self.hide()
		self.attributes('-topmost', True)
		self.attributes('-alpha', 0.77)
		self.geometry("333x333+1+25")
		self.overrideredirect(1)
		self.frame.grid_columnconfigure(1, weight=1)
		self.frame.grid_rowconfigure(1, weight=1)

		Button(self.frame, text='≡', command=self.search).grid(sticky='NSEW', column=0, row=0)

		frame1 = Frame(self.frame, bg=colorbg)
		frame1.grid(sticky='NSEW', column=0, row=1)
		Button(frame1, text='G', command=self.search).grid(sticky='N', row=0)
		Button(frame1, text='Y', command=self.search).grid(sticky='N', row=1)
		Button(frame1, text='B', command=self.search).grid(sticky='N', row=2)
		ttk.Separator(frame1, orient='horizontal').grid(sticky='EW', row=3)
		Button(frame1, text='yt', command=self.search).grid(sticky='N', row=4)

		frame2 = Frame(self.frame, bg=colorbg)
		frame2.grid(sticky='NSEW', column=1, row=1, ipady=10, ipadx=10)
		frame2.grid_columnconfigure(0, weight=1)
		frame2.grid_rowconfigure(3, weight=1)
		self.searchbox2 = Entry(frame2)
		self.searchbox2.grid(sticky='NSEW', row=0)
		self.searchbox2.bind('<Return>', self.search)
		self.searchbox3 = Entry(frame2)
		self.searchbox3.grid(sticky='NSEW', row=1)
		self.searchbox3.bind('<Return>', self.search)
		self.enginebox = ttk.Combobox(frame2)
		self.enginebox.grid(sticky='NSEW', row=2)
		self.enginebox.configure(values=['Google','Yandex','Bing'])
		self.enginebox.set('Google')
		fileframe = Frame(frame2, bg=colorbg)
		fileframe.grid(sticky='NSEW', row=3)
		fileframe.grid_columnconfigure(1, weight=1)
		fileframe.grid_rowconfigure(0, weight=1)
		self.list1 = Listbox(fileframe)
		self.list1.grid(sticky='NSEW', row=0, column=0)
		self.list2 = Listbox(fileframe)
		self.list2.grid(sticky='NSEW', row=0, column=1)
		self.list1.bind('<Double-1>', self.change_file)
		self.list1.bind('<Button-3>', self.edit_file)
		self.list2.bind('<Double-1>', self.change_filter)

		self.searchbox = Entry(self.frame)
		self.searchbox.grid(sticky='NSEW', column=1, row=0)
		self.searchbox.bind('<Return>', self.search)

		filelist = [x for x in os.listdir(cwd) if not os.path.isdir(os.path.join(cwd, x))]
		filelist = os_sorted(filelist)
		for item in filelist:
			self.list1.insert(END, item)

		self.theme(self.frame, bg='#000000', fg='#ffffff')
		self.bind('<Expose>', lambda e: self.searchbox.focus())


	def engine(self, id):
		print(id)
		search()

	def search(self, *event):
		engine = {'Google': 'https://www.google.com/search?q=%s&num=100&nfpr=1',\
		'Yandex': 'https://yandex.com/search/?text=%s',\
		'Bing': 'https://www.bing.com/search?q=%s',\
		}
		searchstr = self.searchbox2.get()+' '+self.searchbox.get()+' '+self.searchbox3.get()
		webbrowser.open(engine[self.enginebox.get()] % searchstr, new=2, autoraise=True)
		#webbrowser.open(r'https://www.google.com/search?q='+self.searchbox.get()+' '+self.searchbox2.get()+' '+self.searchbox3.get()+r'&num=100&nfpr=1', new=2, autoraise=True)

	def change_file(self, *event):
		self.list2.delete(0, END)
		picked = self.list1.get(self.list1.curselection()[0])
		path = os.path.join(cwd, picked)
		file = open(path, mode='r')
		filecontent = file.read()
		file.close()
		filecontent = filecontent.split("\n")
		for item in filecontent:
			self.list2.insert(END, item)

	def edit_file(self, *event):
		picked = self.list1.get(self.list1.curselection()[0])
		path = os.path.join(cwd, picked)
		os.startfile(path)

	def change_filter(self, *event):
		picked = self.list2.get(self.list2.curselection()[0])
		self.searchbox3.delete(0, END)
		self.searchbox3.insert(0, picked)


if __name__ == "__main__":
    app = Search()
    app.mainloop()