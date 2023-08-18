import Zeta
from Zeta.Panel.Window import Panel
from Zeta.Image import Icon

from tkinter import *

x1 = Panel(border='mono', color2='green', mode='basic')
hue = Zeta.Color.Neon(color2='green').hue

imgx = Icon.Load(icon='alchemybw', icontype='bw').image
#imgx = Zeta.Image.Icon.Load(icon='alchemybw', icontype='bw').image
b1 = Button(x1, text="Close", background=hue, relief='flat', command=x1.window.destroy, image=imgx)
b1.pack(side="top")

x1.window.mainloop()