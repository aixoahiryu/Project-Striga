from Zeta.Panel import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename

class TextBox(Frame):
	def __init__(self, master, file='', darkmode=True, richtext=False, color2='', neonmode=False):
		Frame.__init__(self, master)
		self.pack(fill='both', expand=True)
		self.text = ScrolledText(self, height=30, wrap='word', undo=True, setgrid=True, pady=2, padx=3)
		self.text.pack(fill='both', expand=True) # in_=

		if file!='': self.read(file)

	def open(self):
		path = askopenfilename() #filetypes=validFileTypes, initialdir=initialdir
		self.read(path)

	def read(self, path):
		with open(path, 'r+', encoding='utf-8') as target:
			content = target.read()
			self.text.delete('1.0', 'end')
			self.text.insert('end', content)


class TextPanel(Window):
	def __init__(self, mode='basic', color2='green', file='', *args, **kargs):
		Window.__init__(self, mode=mode, color2=color2, *args, **kargs)
		maintext = TextBox(self.frame, file=file)

		self.theme(self.frame, fg=self.neon, bg=self.hue)
		self.bind_all('<Control-o>', lambda e: maintext.open())

if __name__ == '__main__':
	TextPanel(title='Text panel', file=r'D:\_\Interface\Void.py').mainloop()