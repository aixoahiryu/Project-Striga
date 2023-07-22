# File: clrpick.py
#    http://infohost.nmt.edu/tcc/help/pubs/tkinter//dialogs.html#tkColorChooser

from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import *

from demopanels import MsgPanel, SeeDismissPanel

class ColorPickDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='clrpickdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Color Picker Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, 
                     ["Press the buttons below to choose the foreground ",
                      "and background colors for the widgets in this window."])
            
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = ttk.Frame(self, name='demo')
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
        
        bgBtn = ttk.Button(demoPanel, text='Set background color...',
                           width=25, name='bgBtn',
                           command=lambda: self._set_color('background'))
        fgBtn = ttk.Button(demoPanel, text='Set foreground color...',
                           width=25, name='fgBtn',
                           command=lambda: self._set_color('foreground'))
        bgBtn.pack(side=TOP, anchor=CENTER, pady='2m')
        fgBtn.pack(side=TOP, anchor=CENTER, pady='2m')

    def _set_color(self, opt):
        
        # askcolor() returns a tuple of the form
        # ((r,g,b), hex) or (None, None) if cancelled
        color = askcolor(parent=self,
                         title='Choose a {} color'.format(opt))
        if color[1]:
            opts = {opt: color[1]}
            children = self._get_all_children(self.master.winfo_children(),
                                              self.master.winfo_children())
    
            for child in children:
                try:
                    child.config(opts)
                except TclError:    # no background/foreground attribute
                    # ttk.Button background option only changes the
                    # button highlight area, not the entire background
                    # foreground works as expected
                    ttk.Style().configure(child.winfo_class(), **opts)
        
    def _get_all_children(self, children, allChildren) :
        # recursive routine to get all of a given widgets children
        # children - list of a given widgets children
        # allchildren - list of 'all' the given widgets children
        #               including grandchildren, great-grandchildren,etc
        #               initially, should be the same as children
        for child in children :
            if child.winfo_children():
                allChildren.extend(child.winfo_children())
                self._get_all_children(child.winfo_children(), allChildren)
        
        return allChildren

if __name__ == '__main__':
    ColorPickDemo().mainloop()