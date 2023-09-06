import Zeta
from Zeta.Panel.Window import Panel

from tkinter import *

x1 = Panel(border='gradient', color2='red', mode='basic')
hue = Zeta.Color.Neon(color2='red').hue

b1 = Button(x1.frame, text="Close",command=x1.destroy)
t1 = Text(x1.frame, width=40, height=10, background=hue)
b1.pack(side="top")
t1.pack(side="top", fill="both", expand=True)

x1.mainloop()