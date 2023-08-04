from tkinter import *

class Decoration(Frame):
    def __init__(self, master, title='Title'):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=X)
        
        msg = Label(self, wraplength='4i', justify=LEFT)
        msg['text'] = ''.join(msgtxt)
        msg.pack(fill=X, padx=5, pady=5)
        btnclose = Button(text='Ω', command=self.winfo_toplevel().destroy)