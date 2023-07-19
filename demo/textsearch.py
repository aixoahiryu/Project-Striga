# File: textsearch.py
# References:
#    http://infohost.nmt.edu/tcc/help/pubs/tkinter//text.html
#    http://www.tcl.tk/man/tcl8.5/TkCmd/text.htm
#    http://stackoverflow.com/questions/3781670/tkinter-text-highlighting-in-python

from tkinter import *
from tkinter import ttk
from demopanels import SeeDismissPanel

class TextSearchDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='textsearchdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Text Search Demo')
        self.isapp = isapp
        self.text = None
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:            
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP)
        
        self._load_file_panel(demoPanel)
        self._search_panel(demoPanel)
        self._txt_panel(demoPanel)

    def _load_file_panel(self, parent):
        f = ttk.Frame(parent)
        f.pack(side=TOP)
        
        ttk.Label(text="File Name: ", 
                  width=13, anchor=W).pack(in_=f, side=LEFT)
        
        fname = StringVar()
        e = ttk.Entry(width=40, textvariable=fname)
        e.pack(in_=f, side=LEFT)
        
        btn = ttk.Button(text='Load File', 
                         command=lambda fn=fname: self._load_file(fn.get()))
        btn.pack(in_=f, side=LEFT, padx=10, pady=5)
        
        # 'Return' triggers button routine
        e.bind('<Return>', lambda evt, btn=btn: btn.invoke())
                
    def _load_file(self, fname):    
        self.text.delete('0.0', END) # clear text
        
        try:
            self.text.insert(END, open(fname).read())
        except IOError:
            self.bell()
            self.text.insert(END, 
                             'File ' + fname + ' not found.')
                    
        # stop 'Return' event from propagating    
        return 'break'
                
    def _search_panel(self, parent):
        f = ttk.Frame(parent)
        f.pack(side=TOP)
        
        ttk.Label(text="Search string: ", 
                  width=13, anchor=W).pack(in_=f, side=LEFT)
        
        srchStr = StringVar()
        e = ttk.Entry(width=40, textvariable=srchStr)
        e.pack(in_=f, side=LEFT)
        
        btn = ttk.Button(text='Highlight',
                         command=lambda ss=srchStr: self._search_text(ss.get()))
        btn.pack(in_=f, side=LEFT, padx=10, pady=5)

        # 'Return' triggers button routine
        e.bind('<Return>', lambda evt, btn=btn: btn.invoke())
       
    def _search_text(self, srchString):
        # remove previous search results
        self.text.tag_remove('search', 0.0, END)
        
        # empty search string?
        if not srchString:
            return 'break'  # don't propagate event
        
        cur = 1.0         # current position
        length = IntVar() # num of matched chars
        while True:
            cur = self.text.search(srchString,
                                   cur, END,
                                   count=length)
            if not cur:
                return 'break'
            
            # 'end' position of matched characters
            matchEnd = '{0}+{1}c'.format(cur, length.get())
            
            self.text.tag_add('search', cur, matchEnd)
            cur = self.text.index(matchEnd)
    
    def _txt_panel(self, parent):
        # create scrolled text widget
        txtFrame = ttk.Frame(self)
        txtFrame.pack(side=TOP, fill=BOTH, expand=Y)
        
        self.text = Text(txtFrame, height=20, setgrid=True, wrap=WORD, 
                    undo=True, pady=2, padx=3)
        xscroll = ttk.Scrollbar(txtFrame, command=self.text.xview, 
                                orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(txtFrame, command=self.text.yview, 
                                orient=VERTICAL)
        self.text.configure(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        
        # configure 'search' style tag
        self.text.tag_configure('search', background='yellow')
        
        # position in frame and set resize constraints
        self.text.grid(row=0, column=0, sticky=NSEW)
        yscroll.grid(row=0, column=1, sticky=NSEW)
        txtFrame.rowconfigure(0, weight=1)
        txtFrame.columnconfigure(0, weight=1)
        
        # add text to scrolled text widget
        txt = ["This window demonstrates how to use the ",
         "tagging facilities in text widgets to ",
         "implement a searching mechanism.\n\n  First, ",
         "type a file name in the top entry, then type ",
         "'Return' or click on 'Load File'.\n\n  Then ",
         "type a string in the lower entry and type ",
         "'Return' or click on 'Highlight'.  This will ",
         "cause all of the instances of the string to ",
         "be tagged with the tag 'search', and it will ",
         "arrange for the tag's display attributes to ",
         "change the searched words background colour."]

        self.text.insert(END, ''.join(txt))
        

if __name__ == '__main__':
    TextSearchDemo().mainloop()