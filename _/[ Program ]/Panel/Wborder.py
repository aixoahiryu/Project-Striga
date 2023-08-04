from tkinter import *
from Toplevel2 import Toplevel2
from Frame.Corner import CornerFrame
from Frame.Mono import MonoFrame
from Frame.Gradient import GradientFrame

class Wborder(Frame):
    def __init__(self, *args, **kwargs):
        self.window = Toplevel2()
        self.window.overrideredirect(True)

        gradient_frame = MonoFrame(self.window)
        gradient_frame.pack(side="top", fill="both", expand=True)
        Frame.__init__(self, gradient_frame, *args, **kwargs)
        self.pack(side="top", fill="both", expand=True, padx=5, pady=5)

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        frame1 = Wborder()

        b1 = Button(frame1, text="Close",command=self.destroy)
        t1 = Text(frame1, width=40, height=10)
        b1.pack(side="top")
        t1.pack(side="top", fill="both", expand=True)

if __name__ == "__main__":
    app=SampleApp()
    app.mainloop()