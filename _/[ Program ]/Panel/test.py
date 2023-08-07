from tkinter import *
from Wborder import Wborder
from Control.File import Example

test = Tk()
frame1 = Wborder(color2='green')
t1 = Text(frame1, width=40, height=10)
t1.pack(side="top", fill="both", expand=True)
Example(frame1).pack(side="top")

#frame1.window.transient(test)

test.mainloop()