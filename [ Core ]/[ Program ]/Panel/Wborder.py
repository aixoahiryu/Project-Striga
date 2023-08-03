from tkinter import *
from Frame.Corner import CornerFrame
from Frame.Mono import MonoFrame
from Frame.Gradient import GradientFrame

# class Wborder(Frame):
#     def __init__(self, root, *args, **kwargs):
#         Frame.__init__(self, root, *args, **kwargs)
#         self.pack(side="top", fill="both", expand=True, padx=5, pady=5)

# class Wborder(Frame):
#     def __init__(self, master, msgtxt):
#         Frame.__init__(self, master)
#         self.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        
#         msg = Label(self, wraplength='4i', justify=LEFT)
#         msg['text'] = ''.join(msgtxt)
#         msg.pack(fill=X, padx=5, pady=5)

class Wborder(Frame):
    def __init__(self, *args, **kwargs):
        window = Toplevel2()

        gradient_frame = GradientFrame(window)
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

if __name__ == "__main__":
    app=App()
    app.mainloop()