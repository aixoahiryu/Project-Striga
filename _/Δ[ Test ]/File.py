import Zeta
#from Zeta.Panel.Window import Panel
from Zeta.Panel.Window import Fallback as Panel
from Zeta.Panel.Control.File import FileBox
from Zeta.Image import Icon

from tkinter import *

class Controller():
	def toggle_sidebar(child): print('toggled')
	def preview_file(child): print('preview')


#x1 = Panel(border='mono', color2='green', mode='basic')
x1 = Panel(color2='green', mode='basic')
hue = Zeta.Color.Neon(color2='green').hue
controller1 = Controller()

imgx = Icon.Load(icon='alchemybw', icontype='bw').image
frame1 = Frame(x1)
#imgx = Zeta.Image.Icon.Load(icon='alchemybw', icontype='bw').image
b1 = Button(x1, text="Close", background=hue, relief='flat', command=x1.window.destroy, image=imgx)
b1.pack(side="top")
frame1.pack(side="top")

FileBox(frame1, home=r'D:\Data', color2='green', darkmode=True, neonmode=True)

x1.window.mainloop()


