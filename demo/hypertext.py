# File: hypertext.py
#    http://infohost.nmt.edu/tcc/help/pubs/tkinter//text.html
#    http://docs.python.org/py3k/library/subprocess.html

import subprocess 
from tkinter import *
from tkinter import ttk
from demopanels import MsgPanel, SeeDismissPanel

class HypertextDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='hypertextdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Hypertext Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:            
            SeeDismissPanel(self)
        
        self.text = self._create_demo_panel()
        self._insert_text()
        self._add_bindings()
        
    def _create_demo_panel(self):
        # create scrolled text widget
        txtFrame = ttk.Frame(self)
        txtFrame.pack(side=TOP, fill=BOTH, expand=Y)
        
        text = Text(txtFrame, height=30, setgrid=True, wrap=WORD, 
                    undo=True, pady=5, padx=5)
        xscroll = ttk.Scrollbar(txtFrame, command=text.xview, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(txtFrame, command=text.yview, orient=VERTICAL)
        text.configure(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        
        # position in frame and set resize constraints
        text.grid(row=0, column=0, sticky=NSEW)
        yscroll.grid(row=0, column=1, sticky=NSEW)
        txtFrame.rowconfigure(0, weight=1)
        txtFrame.columnconfigure(0, weight=1)
        
        return text

    def _insert_text(self):
        txt = ["The same tag mechanism that controls display styles in text widgets ",
              "can also be used to associate Tcl commands with regions of text, so ",
              "that mouse or keyboard actions on the text cause particular Tcl ",
              "commands to be invoked.\n\nFor example, in the text below the ",
              "descriptions of the canvas demonstrations have been tagged.  ",
              "When you move the mouse over a demo description the description ",
              "lights up, and when you press button 1 over a description then that ",
              "particular demonstration is invoked.\n\n"]

        self.text.insert(END, ''.join(txt))
        
        # insert tagged text
        # Note: tags must be passed in a tuple as the third argument
        #       the keyword 'tags' is not recognized; if the tags are
        #       passed as a list they are ignored; 
        #       if passed as a string, each character in the string
        #       is assigned as an individual tag

        newline = '\n\n'  # if included with text, becomes part of the 'tag' content
        
        self.text.insert(END,
                    "1. Samples of all the different types of items that can be created in canvas widgets.",
                    ('d1',))
        self.text.insert(END, newline)
        self.text.insert(END,
                    "2. A simple two-dimensional plot that allows you to adjust the positions of the data points.",
                    ('d2',))
        self.text.insert(END, newline)
        self.text.insert(END,
                    "3. Anchoring and justification modes for text items.",
                    ('d3',))
        self.text.insert(END, newline)
        self.text.insert(END,
                    "4. An editor for arrow-head shapes for line items.",
                    ('d4',))
        self.text.insert(END, newline)
        self.text.insert(END,
                    "5. A ruler with facilities for editing tab stops.",
                    ('d5',))
        self.text.insert(END, newline)
        self.text.insert(END,
                    "6. A grid that demonstrates how canvases can be scrolled.",
                    ('d6',))

    def _add_bindings(self):
        style = {'highlight': {'background': 'yellow',
                               'relief': RIDGE,
                               'borderwidth': 1},
                 'normal': {'background': '',
                            'relief': FLAT}}
        
        txtTags = ('d1', 'd2', 'd3', 'd4', 'd5', 'd6')
        demos = ('canvasitems.py', 'simpleplot.py', 'textcanvas.py',
                 'canvasarrow.py', 'canvasruler.py', 'canvassimple.py')
        
        i = 0   # index to demo file list
        for t in txtTags:
            self.text.tag_bind(t, '<Any-Enter>', 
                               lambda e, t=t, s=style: self.text.tag_config(t, s['highlight']))

            self.text.tag_bind(t, '<Any-Leave>', 
                               lambda e, t=t, s=style: self.text.tag_config(t, s['normal']))
        
            self.text.tag_bind(t, '<1>',
                               lambda e, d=demos, i=i: self._run_demo(e, d[i]))
            
            i += 1
        
    def _run_demo(self,e, fn):
        # assumes the demo files are in the current directory
        # minimizes and blocks until the new process terminates
        try:
            self.master.iconify()
            subprocess.call(['python', fn])
        except:
            print('Unable to run ' + fn)
        finally:
            self.update()
            self.master.deiconify()
            
        
if __name__ == '__main__':
    HypertextDemo().mainloop()