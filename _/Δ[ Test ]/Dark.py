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
x1 = Panel(color2='white', mode='basic')
x2 = Panel(color2='white', mode='basic')
hue = Zeta.Color.Neon(color2='white').hue
controller1 = Controller()

imgx = Icon.Load(icon='alchemybw', icontype='bw').image
frame1 = Frame(x1.frame)
#imgx = Zeta.Image.Icon.Load(icon='alchemybw', icontype='bw').image
b1 = Button(x1.frame, text="Close", background=hue, relief='flat', command=x1.destroy, image=imgx)
b1.pack(side="top")
frame1.pack(side="top")

FileBox(frame1, home=r'D:\Data', darkmode=True)

x1.child.append(x2)
x1.bind('<Button-1>', lambda e: print(x1.winfo_width()))
x1.mainloop()


