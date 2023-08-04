from tkinter import *
from Toplevel2 import Toplevel2
from Frame.Corner import CornerFrame
from Frame.Mono import MonoFrame
from Frame.Gradient import GradientFrame

class Wborder(Frame):
    def __init__(self, draggable=True, border='mono', color=7, mode='border', *args, **kwargs):
        if draggable: self.window = Toplevel2()
        else: self.window = Toplevel()
        self.window.overrideredirect(True)

        if border=='mono': from Frame.Mono import MonoFrame as ColorFrame
        elif border=='corner': from Frame.Corner import CornerFrame as ColorFrame
        elif border=='gradient': from Frame.Gradient import GradientFrame as ColorFrame
        gradient_frame = ColorFrame(self.window, color=color)
        gradient_frame.pack(side="top", fill="both", expand=True)

        Frame.__init__(self, gradient_frame, *args, **kwargs)
        self.pack(side="top", fill="both", expand=True, padx=5, pady=5)

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        frame1 = Wborder(border='mono', color=6)

        b1 = Button(frame1, text="Close",command=self.destroy)
        t1 = Text(frame1, width=40, height=10)
        b1.pack(side="top")
        t1.pack(side="top", fill="both", expand=True)

if __name__ == "__main__":
    app=SampleApp()
    app.mainloop()