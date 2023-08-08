# File: labels.py
# References:
#    The widget.tcl and label.tcl files in the Python 3.2 install 
#    directory under \tcl\tk8.5\demos
#    http://effbot.org/tkinterbook/label.htm

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from demopanels import MsgPanel, SeeDismissPanel

class LabelDemo(ttk.Frame):
    """Demonstrates 5 labels. """
    
    def __init__(self, isapp=True, name='labeldemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Label Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, ['Five labels are displayed below: three textual ones on the left, ',
                      'and a bitmap label and a text label on the right.',
                      "Labels are pretty boring because you can't do anything with them."])
            
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
             
    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
        
        left = Frame(demoPanel)
        right = Frame(demoPanel)
        left.pack(side=LEFT, expand=True, padx=10, pady=10, fill=BOTH)
        right.pack(side=LEFT, expand=True, padx=10, pady=10, fill=BOTH)
        
        # labels
        l1 = ttk.Label(left, text='First Label')
        l2 = ttk.Label(left, text='Second label, raised', relief=RAISED)
        l3 = ttk.Label(left, text='Third label, sunken', relief=SUNKEN)
        
        # pady adds vertical space 'around' the label, 
        # ipadx adds horizontal space 'inside' the label
        l1.pack(side=TOP, expand=True, pady=2, ipadx=2, anchor=W)
        l2.pack(side=TOP, expand=True, pady=2, ipadx=2, anchor=W)
        l3.pack(side=TOP, expand=True, pady=2, ipadx=2, anchor=W)
        
        # image label
        prop = BitmapImage(file='images//face.xbm')
        l4 = ttk.Label(right, borderwidth=2, relief=SUNKEN, image=prop)
        l4.image = prop  # keep reference to prevent garbage collection
        
        caption = ttk.Label(right, text="Tcl/Tk Proprietor")
        l4.pack(side=TOP)
        caption.pack(side=TOP)


if __name__ == '__main__':
    LabelDemo().mainloop()