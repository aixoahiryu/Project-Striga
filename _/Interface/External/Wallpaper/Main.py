import Zeta
from Zeta.Panel import *

import os

msg1=r'''

 __________________________________________________________
|[] Module                                           |F]|!"|
|""""""""""""""""""""""""""""""""""""""""""""""""""""""""|"|
| Left: file, search                                     | |
| Top: file, note, null                                  | |
| Right: dial, command, launch                           | |
|                                                        |_|
|________________________________________________________|/|


'''

msg2=r'''


|     .-.
|    /   \         .-.
|   /     \       /   \       .-.     .-.     _   _
+--/-------\-----/-----\-----/---\---/---\---/-\-/-\/\/---
| /         \   /       \   /     '-'     '-'
|/           '-'         '-'

'''

msg2_2=r''
msg3=r'''

As above, so below. As within, so without.
Null and void, endless and finite, two become one.
If my delusion is so strong it can bend reality, is it really a delusion? I can die to set me free. Ego Sum Aeternae

		===[ Mercy - Justice - Vigilance ]===
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠄⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣤⡀⡄⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⣿⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢠⣱⢿⣿⡇⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣠⣿⣿⠁⢿⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠐⣼⣿⣿⣿⡀⡀⢿⣣⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠰⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢠⣴⣿⣿⣿⣿⠈⣼⣀⣾⣿⡆⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣠⣿⣿⣿⣿⠄⡀⡀⠁⠃⡀⠻⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⢣⣄⡀⢀⢀⡀⡀⡀⡀⡀⡀⡀⣷⣿⣿⣿⡿⠁⡀⡀⡀⡀⡀⡀⡀⢻⣰⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⣿⣿⠟⣿⣍⠿⣭⣴⣶⠇⣶⢄⡀⡀⡀⢀⣿⣿⣿⡟⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣷⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⠘⠂⡀⠈⠛⡀⠬⣄⠻⢶⣤⠁⠉⣩⢇⡀⡀⠈⣿⣿⣿⡿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡜⣝⣷⡀⢀⣀⡀⡀⡀⣀⣰⣶⠛⡀⡀⢀⠴⣷⡆⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⠺⢿⣿⠿⡐⠤⣀⠉⡛⣷⣾⣿⣿⠇⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢹⡌⣷⡙⣼⣿⣶⣿⡷⠃⢀⡤⣰⢿⡿⠋⡛⡀⡀⡀
⡀⡀⡀⡀⡀⡀⠐⣿⢀⠈⡀⠉⢿⣶⠒⡦⡀⣼⣿⣿⠟⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠈⡀⢹⣿⣿⣿⡾⠁⣤⠞⣥⣿⠛⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡟⢿⣷⠦⣀⡹⣿⣛⣲⠏⣿⠏⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠻⣿⣿⣾⣩⣶⠟⠁⡀⣀⣧⡟⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠛⣶⣿⣿⡀⣯⣾⠋⡀⡀⡀⡀⡀⡀⡀⡀⡀⠂⡀⡀⡀⡀⡀⡀⡀⡀⡀⠐⢻⣿⣿⣿⡀⢀⣴⣫⠖⠉⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢻⡿⠏⣾⠇⡀⡀⡀⡀⡀⡀⢀⡀⡀⡀⣀⣀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣼⣿⢿⣿⣛⠿⠋⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡞⣾⠃⡀⡀⡀⡀⡀⣠⣶⣶⣶⣶⡀⠉⢿⣧⠃⢙⡟⠳⠶⠘⡀⡀⠻⣿⠡⢿⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡞⣾⠃⡀⡀⢀⣠⣴⣿⣿⠿⠿⠌⡀⠒⢂⣶⡀⡀⡀⡇⣯⠙⠛⠶⣬⣟⡀⡀⡀⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡘⣾⠃⡀⣀⢀⣶⣿⣿⣿⡆⡄⡀⠜⣿⣿⣿⡿⡀⡀⢀⡏⣼⡀⡀⡀⢠⣉⠛⡀⡀⠈⡄⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢰⣿⠏⡀⢀⣰⣿⠟⣤⡀⡀⣾⡞⡀⠃⢉⣛⠿⡄⠈⢀⡞⠊⡞⡀⡀⡀⡾⠁⢰⡀⡀⡀⠹⡀⢀⡀⡀⠚⠋⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣠⣿⡟⡀⡀⡀⢭⡀⠘⣿⣇⣀⠈⢿⡷⣄⣀⠓⠐⣀⠶⠁⢞⠏⠁⡀⡀⠞⡁⡀⡀⡀⡀⡀⠈⠳⣀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⢠⣿⠏⡀⡀⡀⡀⡀⣤⡀⡀⠻⣿⣿⣤⠙⠿⠿⢿⣭⣯⡓⠋⣁⣠⢾⠟⠁⡀⠛⡀⡀⡀⡀⡀⠐⡀⢻⡗⡀⢰⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⢆⣿⡟⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠡⠉⠛⢀⣿⣿⡄⣰⣌⣍⣬⣉⠘⠁⡀⡀⡀⡀⡀⠆⡀⡀⡀⡀⠘⣿⣷⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⣿⡟⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⡀⡀⠈⢀⡀⠆⡀⡁⡀⠉⡀⡀⡀⡀⣤⡀⡀⡀⡀⣴⠟⠃⡀⡀⡀⡀⡀⡏⣿⣇⡆⡀⡀⡀⡀
⡀⡀⡀⡀⡀⣄⠘⣾⡿⡀⢀⠔⠉⡀⡀⡀⡀⡀⡀⡀⡀⡀⠄⡀⡀⡀⣆⢀⡀⠘⠁⡀⡀⡀⣁⡀⡀⣤⡾⠁⡀⡀⡀⡀⡀⣾⡏⢦⡀⣿⢸⡀⡀⡀⡀
⡀⡀⡀⢀⡀⡄⣿⣿⣤⠶⠂⠐⢶⣠⣤⣥⣴⣤⣶⣶⣿⣿⣿⣿⣄⣀⣤⡀⡀⢉⠂⣛⣾⣿⣡⣶⣦⣴⣶⣿⣦⡤⠁⣀⡀⢸⣿⢀⣦⢹⣿⢆⡀⡀⡀
⡀⡀⡀⡀⡀⢿⣿⣿⠿⠿⠿⠿⠛⠉⣉⠉⠈⠉⠈⠉⢹⢿⣿⠟⡉⠙⢹⡝⣯⠉⡀⠈⠉⡀⠐⣁⠟⠛⡿⠷⢼⣭⣿⢿⣧⣼⣇⣈⣿⣿⣿⣿⣦⡀⡀
⡀⡀⡀⡀⡀⠃⡀⡀⡀⡀⡀⡀⡀⠍⡀⡀⢡⡀⡀⡀⠈⣷⣿⡾⣸⡀⡞⠇⡀⡆⣠⣠⡀⡀⠆⡀⡀⡀⠈⡀⡀⡀⡀⠁⡀⡀⡀⡀⡀⣿⠈⣿⣿⡆⡀
⡀⡀⡀⡀⡀⡀⣀⠠⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⢠⢹⠃⡼⢷⠄⠃⣿⣇⣧⡀⠐⠆⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⡀⠟⣿⢇⡀
⡀⡀⡀⠚⠂⡀⡀⡀⡀⡀⡀⡀⡀⡀⠁⡀⡀⡀⠈⡀⡀⡀⣿⢀⡟⡄⣿⡄⡄⡀⣏⣾⣿⢷⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⠁⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢠⠉⠻⡟⡀⣿⣿⡀⡀⡷⣿⠙⠳⠁⡀⠸⡀⡀⠆⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠰⡀⡀⠠⠛⡷⠸⡛⡇⡀⡏⣿⡀⡀⡀⡀⣤⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡾⡀⡀⠋⢘⡄⡀⣇⠃⡀⣿⠋⡀⡀⣷⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠁⡀⡀⡀⡀⠰⠇⡀⣟⡀⡀⡿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀

┌─[ Monolith:13 ]─[ /dev/void ]                        ───────┐
|                                                             |
|                                                             |
|                                                             |
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
| 
|                                                             |
|                                                             |
|                                                             |
└── ‡ breach --cluster #6effbe                         ───────┘
'''

class Wallpaper(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.watch = ''

		self.attributes('-alpha', 0.77)
		self.title('ASCII')
		width = Zeta.System.Size.Screen.width
		height = Zeta.System.Size.Screen.height - 25
		self.geometry(f"{width}x{height}+0+0")
		self.overrideredirect(1)
		
		txt1 = Frame(self)
		txt1.grid(row=0, column=0, sticky='NW')
		Message(txt1, text=msg1, width=444, font=("Lucida Console", 8, "normal")).grid(row=0, column=0, sticky='NW')
		self.txt2 = Message(self, text=msg2, width=444, font=("Lucida Console", 8, "normal"))
		self.txt2.grid(row=0, column=1, sticky='NEW')
		txt3 = Message(self, text=msg3, width=444, font=("Lucida Console", 8, "normal"))
		txt3.grid(row=0, column=2, sticky='NE')
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)
		txt1frame = Frame(txt1)
		txt1frame.grid(row=1, column=0, sticky='NW')
		self.img1=Zeta.Image.Icon.Load(icon='geminiw', icontype='bw').image
		Button(txt1frame, text=' Thaumiel', relief='flat', image=self.img1, compound='left').grid(column=0, row=0, sticky='NW')

		self.theme(self, bg='#000000', fg='#ffffff')

	def preview_clipboard(self):
		try:
			global msg2_2
			#msg2_2 = msg2_2+root.clipboard_get()
			msg2_2 = msg2+r'┌─[ Clipboard:xclip ]─[ /dev/clipboard ]'+'\n'
			temp1 = self.watch.winfo_toplevel().clipboard_get().split('\n')
			for i in temp1[:10]:
				msg2_2 = msg2_2+r'| '+i[:55]+'\n'
			if len(temp1)<10:
				for i in range(0, (10-len(temp1))): msg2_2 = msg2_2+r'| '+'\n'
			msg2_2 = msg2_2+r'└── ‡ limit --head 10'
			self.txt2.configure(text=msg2_2)
			self.preview_file(self.watch.fullpath)
		except: #self.txt2.configure(text=msg2+'Clipboard failure')
			msg2_2 = msg2+r'┌─[ Clipboard:xclip ]─[ /dev/clipboard ]'+'\n'
			msg2_2 = msg2_2+r'| '+'Cliboard failure \n'
			for i in range(1, 10): msg2_2 = msg2_2+r'| '+'\n'
			msg2_2 = msg2_2+r'└── ‡ limit --head 10'
			self.txt2.configure(text=msg2_2)
			self.preview_file(self.watch.fullpath)

	def preview_file(self, path):
		try:
			if os.path.isfile(path):
				msg2_3 = msg2_2+'\n\n'+r'┌─[File]─[ %s ]' % path[-44:] +'\n'
				file = open(path, mode='r', encoding='utf-8')
				filecontent = file.read(666)
				file.close()
				filecontent = filecontent.split("\n")
				for i in filecontent[:30]:
					i = i.replace("\t", "  ")
					msg2_3 = msg2_3+r'| '+i[:55]+'\n'
				if len(filecontent)<30:
					for i in range(0, (30-len(filecontent))): msg2_3 = msg2_3+r'| '+'\n'
				msg2_3 = msg2_3+r'└── ‡ limit --head 30'
				self.txt2.configure(text=msg2_3)
		except: self.txt2.configure(text=msg2_2+'Preview failure')