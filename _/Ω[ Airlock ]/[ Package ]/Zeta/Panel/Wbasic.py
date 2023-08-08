from tkinter import *

class Decoration(Frame):
	def __init__(self, master, title='Title', color=7, color2=''):
		self._color = ['black', '#FF0C12', '#FDAE32', '#FDFB00', '#5CFF00', '#00CFFB', '#8F00F2', 'white']
		self._name1 = {'black': '#000000', 'white': '#ffffff'}
		self._name1['red'] = '#ec5555'
		self._name1['orange'] = '#FF5F1F'
		self._name1['yellow'] = '#FFCC00'
		self._name1['green'] = '#6effbe'
		self._name1['blue'] = '#00FFFF'
		self._name1['purple'] = '#bc13fe'
		self._color1 = self._color[color]
		if color2 != '': self._color1 = self._name1[color2]

		Frame.__init__(self, master)
		top = Frame(self)
		top.pack(side='top', expand=True, fill="both")
		top.grid_columnconfigure(0, weight=1)
		#body = Frame(self)
		
		msg = Label(top, wraplength='4i', justify=LEFT, foreground=self._color1)
		msg['text'] = title
		msg.grid(row=0, column=0, sticky='NW')
		btnframe = Frame(top)
		btnframe.grid(row=0, column=1, sticky='E')
		Button(btnframe, text=u'Ζ', relief='flat', foreground='#c9c9c9', font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text=u'Α', relief='flat', foreground='#c9c9c9', font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text=u'Σ', relief='flat', foreground='#c9c9c9', font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text=u'Ω', relief='flat', foreground='#c9c9c9', font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text=u'¦', relief='flat', foreground='#c9c9c9', font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text='■', relief='flat', foreground=self._name1['green'], command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text='■', relief='flat', foreground=self._name1['yellow'], command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text='■', relief='flat', foreground=self._name1['red'], command=self.winfo_toplevel().destroy).pack(side='left')
