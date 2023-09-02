import Zeta
from tkinter import *

class Decoration(Frame):
	def __init__(self, master, title='Title', color=7, color2=''):
		self._color1 = Zeta.Color.Neon(color=color, color2=color2).hex
		self._bg1 = Zeta.Color.Neon(color=color, color2=color2).hue

		Frame.__init__(self, master, background=self._bg1)
		top = Frame(self, background=self._bg1)
		top.pack(side='top', fill=X)
		top.grid_columnconfigure(0, weight=1)
		#body = Frame(self)
		
		msg = Label(top, wraplength='4i', justify=LEFT, foreground=self._color1, background=self._bg1, font=("Courier New", 10, "normal"))
		msg['text'] = title
		msg.grid(row=0, column=0, sticky='NW')
		btnframe = Frame(top, background=self._bg1)
		btnframe.grid(row=0, column=1, sticky='E')
		Button(btnframe, text=u'Ζ', relief='flat', foreground='#c9c9c9', background=self._bg1, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text=u'Α', relief='flat', foreground='#c9c9c9', background=self._bg1, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text=u'Σ', relief='flat', foreground='#c9c9c9', background=self._bg1, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text=u'Ω', relief='flat', foreground='#c9c9c9', background=self._bg1, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text=u'¦', relief='flat', foreground='#c9c9c9', background=self._bg1, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text='■', relief='flat', foreground=Zeta.Color.Neon(color2='green').hex, background=self._bg1, command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text='■', relief='flat', foreground=Zeta.Color.Neon(color2='yellow').hex, background=self._bg1, command=self.winfo_toplevel().destroy).pack(side='left')
		Button(btnframe, text='■', relief='flat', foreground=Zeta.Color.Neon(color2='red').hex, background=self._bg1, command=self.winfo_toplevel().destroy).pack(side='left')

		try:
			self.winfo_toplevel().bind_drag(top)
			self.winfo_toplevel().bind_drag(msg)
			self.winfo_toplevel().bind_drag(btnframe)
			# top.bind("<ButtonPress-1>", self.winfo_toplevel().start_move)
			# top.bind("<ButtonRelease-1>", self.winfo_toplevel().stop_move)
			# top.bind("<B1-Motion>", self.winfo_toplevel().do_move)
		except: print('Window error')