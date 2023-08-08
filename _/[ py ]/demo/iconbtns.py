# File: iconbtns.py
# References:
 

from tkinter import *
from tkinter import ttk
from demopanels import MsgPanel, SeeDismissPanel

class IconBtnsDemo(Frame):
    
    def __init__(self, isapp=True, name='iconbtnsdemo'):
        Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Icon Buttons Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, ["This window shows two ways of using bitmaps or images ",
                            "in ttk.Radiobuttons and ttk.Checkbuttons.\n\n ",
                            "On the left are two radiobuttons, each of which displays ",
                            "a bitmap and an indicator.\n\n",
                            "The checkbuttons display as themed buttons that 'sink' when selected.",
                            "They also display different images for each state."])
            
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, pady=1, padx=1, expand=False, fill=None)
        
        # create images
        self.letters = PhotoImage(file="folder.gif")
        self.noletters = PhotoImage(file="folder.gif")
        self.flagup = PhotoImage(file="folder.gif")
        self.flagdn = PhotoImage(file="folder.gif")

        # create buttons
        rbs = self._rb_panel(demoPanel)
        cbs = self._cb_panel(demoPanel)
        rbs.pack(side=LEFT, expand=True, padx=10, pady=10, fill=BOTH)
        cbs.pack(side=LEFT, expand=True, padx=10, pady=10, fill=BOTH)
        
    def _rb_panel(self, parent):

        mail = StringVar()

        f = ttk.Frame(parent)
        b1 = ttk.Radiobutton(f, image=self.letters, variable=mail, value='full')
        b2 = ttk.Radiobutton(f, image=self.noletters, variable=mail, value='empty')
        
        b1.pack(side=TOP, expand=Y)
        b2.pack(side=TOP, expand=Y)
        
        return f

    def _cb_panel(self, parent):
        # the simple expedient of setting the Checkbutton style
        # to 'TButton' vs 'TCheckbutton' causes the small checkbox
        # to disappear and the Checkbutton images to appear in a
        # properly themed 'button'
        f = ttk.Frame(parent)     
        
        cb = ttk.Checkbutton(f, style='Demo.TButton', 
                         image=(self.flagdn, 'selected', self.flagup),
                         command=lambda: self._cb_value_changed(cb))
        
        cb.pack(side=LEFT, expand=False, padx=5, fill=None)
        
        cb1 = ttk.Checkbutton(f, style='Demo.TButton',
                              image=(self.noletters, 'selected', self.letters),
                              command=lambda: self._cb_value_changed(cb1))
        cb1.pack(side=LEFT, expand=False, padx=5, fill=None)
        
        # modify the Toolbutton style to center the text and match the padding
        # of a TButton
        ttk.Style().configure('Demo.Toolbutton', anchor='center', padding=(5,5))
        cb2 = ttk.Checkbutton(f, style='Demo.TButton', text='Off', width=-12,
                              onvalue='On', offvalue='Off',
                              command=lambda: self._cb_value_changed(cb2))
        cb2.pack(side=LEFT, expand=False, padx=5, fill=None)
        
        return f
        
    def _cb_value_changed(self, cb):
        # if a checkbutton is selected, use the 'Toolbutton' 
        # style to make it appear 'sunken'
        if cb.instate(('selected',)):
            cb['style'] = 'Demo.Toolbutton'
            if cb.cget('text'):
                cb['text'] = cb['offvalue']
        else:
            cb['style'] = 'Demo.TButton'
            if cb.cget('text'):
                cb['text'] = cb['onvalue']
        
        
if __name__ == '__main__':
    IconBtnsDemo().mainloop()