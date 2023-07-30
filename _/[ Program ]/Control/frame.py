import time
import os
import glob
import subprocess
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted

class CustomWidget(Frame):
    def __init__(self, parent, label, default=""):
        Frame.__init__(self, parent)

        self.label = Label(self, text=label, anchor="w")
        self.entry = Entry(self)
        self.entry.insert(0, default)

        self.label.pack(side="top", fill="x")
        self.entry.pack(side="bottom", fill="x", padx=4)

    def get(self):
        return self.entry.get()

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.label = Label(self)
        self.e1 = CustomWidget(self, "First Name:", "Inigo")
        self.e2 = CustomWidget(self, "Last Name:", "Montoya")
        self.submitButton = Button(self, text="Submit", command=self.submit)

        self.e1.grid(row=0, column=0, sticky="ew")
        self.e2.grid(row=1, column=0, sticky="ew")
        self.label.grid(row=2, column=0, sticky="ew")
        self.submitButton.grid(row=4, column=0)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def submit(self):
        first = self.e1.get()
        last = self.e2.get()
        self.label.configure(text="Hello, %s %s" % (first, last))

if __name__ == "__main__":
    root = Tk()
    Example(root).place(x=0, y=0, relwidth=1, relheight=1)
    root.mainloop()