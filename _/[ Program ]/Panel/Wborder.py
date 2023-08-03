from tkinter import *
from Frame.Corner import CornerFrame
from Frame.Mono import MonoFrame
from Frame.Gradient import GradientFrame

class Wborder(Frame):
    def __init__(self, *args, **kwargs):
        window = Toplevel2()

        gradient_frame = CornerFrame(window)
        gradient_frame.pack(side="top", fill="both", expand=True)
        Frame.__init__(self, gradient_frame, *args, **kwargs)
        self.pack(side="top", fill="both", expand=True, padx=5, pady=5)

class Toplevel2(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)

        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<ButtonRelease-1>", self.stop_move)
        self.bind("<B1-Motion>", self.do_move)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

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