from tkinter import *

class Toplevel2(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-alpha', 0.99)
		
		self.child = []
		self.owner = []
		self.visible = True
		#self.protocol( 'WM_DELETE_WINDOW' , self.close)

	def hide(self):
		self.withdraw()
		self.visible = False
		for w in self.child:
			try: w.hide()
			except: print('hide() failed')

	def show(self):
		self.deiconify()
		self.visible = True
		for w in self.child:
			try: w.show()
			except: print('show() failed')

	def close(self):
		self.destroy()
		for w in self.owner: w.child.remove(self)
		for w in self.child:
			try: w.close()
			except: print('close() failed')

	def transient(self, master):
		self.owner.append(master)
		master.child.append(self)

	def trancend(self):
		for w in self.owner: w.child.remove(self)

	def start_move(self, event):
		self.x = event.x
		self.y = event.y

	def stop_move(self, event):
		self.x = None
		self.y = None
		x = self.winfo_x() - (self.winfo_x() % 10)
		y = self.winfo_y() - (self.winfo_y() % 10)
		self.geometry(f"+{x}+{y}")

	def do_move(self, event):
		deltax = event.x - self.x
		deltay = event.y - self.y
		x = self.winfo_x() + deltax
		y = self.winfo_y() + deltay
		self.geometry(f"+{x}+{y}")

	def bind_rightclick(self):
		self.bind("<ButtonPress-3>", self.start_move)
		self.bind("<ButtonRelease-3>", self.stop_move)
		self.bind("<B3-Motion>", self.do_move)

	def bind_drag(self, control):
		control.bind("<ButtonPress-1>", self.start_move)
		control.bind("<ButtonRelease-1>", self.stop_move)
		control.bind("<B1-Motion>", self.do_move)