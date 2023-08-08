from tkinter import *
from Toplevel2 import Toplevel2

class Panel(Frame):
    def __init__(self, draggable=True, border='mono', color=7, color2='', mode='basic', style='even', title='Title', *args, **kwargs):
        if draggable: self.window = Toplevel2()
        else: self.window = Toplevel()
        self.window.overrideredirect(True)

        if border=='mono': from Frame.Mono import MonoFrame as ColorFrame
        elif border=='corner': from Frame.Corner import CornerFrame as ColorFrame
        elif border=='gradient': from Frame.Gradient import GradientFrame as ColorFrame
        gradient_frame = ColorFrame(self.window, color=color, color2=color2)
        gradient_frame.pack(side="top", fill="both", expand=True)

        if mode=='basic': from Wbasic import Decoration as ControlFrame
        if mode!='border':
            control_frame = ControlFrame(gradient_frame, color=color, color2=color2, title=title)
            control_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        if mode=='border': Frame.__init__(self, gradient_frame, *args, **kwargs)
        else: Frame.__init__(self, control_frame, *args, **kwargs)
        self.pack(side="top", fill="both", expand=True, padx=5, pady=5)

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        frame1 = Panel(color2='green', mode='basic', border='corner', title='Sample app')

        b1 = Button(frame1, text="Close",command=self.destroy)
        t1 = Text(frame1, width=40, height=10)
        b1.pack(side="top")
        t1.pack(side="top", fill="both", expand=True)

if __name__ == "__main__":
    app=SampleApp()
    app.mainloop()