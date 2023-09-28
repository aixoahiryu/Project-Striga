import Zeta
from Zeta.Panel import *
from .Overflow import Overflow
from .Menubar import *

import os

ZLCORE = Zeta.System.Path.Core.ZLCORE

class Taskbar(Toplevel):
	def __init__(self, Workspace, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', 0.77)
		self.title('Task bar')
		width = Zeta.System.Size.Screen.width
		height = 25
		self.geometry(f"{width}x{height}+1+0")
		self.overrideredirect(1)
		#self.configure(bg=colorbg, bd=1, relief='groove')
		Label(self, text=r'[ Workspace ]').place(relx=0.48, rely=0)

		appframe = Frame(self)
		appframe.grid(sticky='NSW', column=0, row=0)
		#Button(appframe, text='1', relief='flat', background='#3c3c3c').grid(column=0, row=0, sticky='NW')
		Button(appframe, text='1', relief='flat', foreground='#6effbe').grid(column=0, row=0, sticky='NW')
		Button(appframe, text='2', relief='flat').grid(column=1, row=0, sticky='NW')
		Button(appframe, text='3', relief='flat').grid(column=2, row=0, sticky='NW')
		Button(appframe, text='4', relief='flat').grid(column=3, row=0, sticky='NW')
		Button(appframe, text='#', relief='flat').grid(column=4, row=0, sticky='NW')

		# =======================[ Menu ]=======================
		progmenu = ProgramMenu()
		self.imgcode=Zeta.Image.Icon.Load(icon='code', icontype='neon').image
		progbtn = Button(appframe, text=' Program', relief='flat', image=self.imgcode, compound='left')
		progbtn.grid(column=5, row=0, sticky='NW')
		Zeta.System.WM.toggle_bind(progbtn, progmenu, stay=True, geometry='bottom')
		Zeta.System.WM.hover_bind(progbtn, progmenu, geometry='bottom')

		hackmenu = HackingMenu()
		self.imgterm=Zeta.Image.Icon.Load(icon='term3', icontype='neon').image
		hackbtn = Button(appframe, text=' Hacking', relief='flat', image=self.imgterm, compound='left')
		hackbtn.grid(column=6, row=0, sticky='NW')
		Zeta.System.WM.toggle_bind(hackbtn, hackmenu, stay=True, geometry='bottom')
		Zeta.System.WM.hover_bind(hackbtn, hackmenu, geometry='bottom')

		filemenu = FileMenu()
		self.imgfile=Zeta.Image.Icon.Load(icon='file', icontype='neon').image
		filebtn = Button(appframe, text=' File', relief='flat', image=self.imgfile, compound='left')
		filebtn.grid(column=7, row=0, sticky='NW')
		# filebtn.bind("<Button-1>", lambda e: filemenu.post(e.widget.winfo_x(), e.widget.winfo_y() + e.widget.winfo_height()))
		# filebtn.bind('<Button-1>', lambda e: filemenu.show(geometry=f'+{e.widget.winfo_x()}+{e.widget.winfo_y() + e.widget.winfo_height() +1}'), add="+")
		Zeta.System.WM.toggle_bind(filebtn, filemenu, stay=True, geometry='bottom')
		Zeta.System.WM.hover_bind(filebtn, filemenu, geometry='bottom')

		networkmenu = NetworkMenu()
		self.imglink=Zeta.Image.Icon.Load(icon='qr', icontype='neon').image
		netbtn = Button(appframe, text=' Network', relief='flat', image=self.imglink, compound='left')
		netbtn.grid(column=8, row=0, sticky='NW')
		Zeta.System.WM.toggle_bind(netbtn, networkmenu, stay=True, geometry='bottom')
		Zeta.System.WM.hover_bind(netbtn, networkmenu, geometry='bottom')
		#=======================================================

		trayframe = Frame(self)
		trayframe.grid(sticky='NSE', column=1, row=0)
		self.grid_columnconfigure(1, weight=1)
		self.imgcpu=Zeta.Image.Icon.Load(icon='cpuw', icontype='bw').image
		Button(trayframe, text=' 13%', relief='flat', image=self.imgcpu, compound='left').grid(column=0, row=0, sticky='NW')
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		Button(trayframe, text=' 322G', relief='flat', image=self.imghdd, compound='left').grid(column=1, row=0, sticky='NW')
		self.imgnetwork=Zeta.Image.Icon.Load(icon='networkw', icontype='bw').image
		Button(trayframe, text=' 0.7 MB/s', relief='flat', image=self.imgnetwork, compound='left').grid(column=2, row=0, sticky='NW')
		self.imgram=Zeta.Image.Icon.Load(icon='ramw', icontype='bw').image
		Button(trayframe, text=' 2.2 GB', relief='flat', image=self.imgram, compound='left').grid(column=3, row=0, sticky='NW')
		self.imgtemp=Zeta.Image.Icon.Load(icon='tempw', icontype='bw').image
		Button(trayframe, text=' 33°C', relief='flat', image=self.imgtemp, compound='left').grid(column=4, row=0, sticky='NW')
		self.imgvolume=Zeta.Image.Icon.Load(icon='volumew', icontype='bw').image
		Button(trayframe, text=' Ballad', relief='flat', image=self.imgvolume, compound='left').grid(column=5, row=0, sticky='NW')
		self.imgmenu=Zeta.Image.Icon.Load(icon='menuw', icontype='bw').image
		
		overflow = Overflow()
		btnoverflow = Button(trayframe, text='', relief='flat', image=self.imgmenu, compound='none')
		btnoverflow.grid(column=6, row=0, sticky='NW')
		Workspace.toggle_bind(btnoverflow, overflow)

		self.theme(self, bg='#000000', fg='#ffffff')