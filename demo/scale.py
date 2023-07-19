# File: scale.py
#    http://www.tcl.tk/man/tcl8.5/TkCmd/ttk_scale.htm

from tkinter import *
from tkinter import ttk
from demopanels import MsgPanel, SeeDismissPanel

class ScaleDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='scaledemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Scale Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, 
                     ["A label tied to a horizontal scale is displayed below. ",
                      "If you click or drag mouse button 1 in the scale, you ",
                      "can change the contents of the label; a callback command ",
                      "is used to couple the slider to both the text and the ",
                      "coloring of the label."])
            
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = ttk.Frame(self, borderwidth=10)
        demoPanel.pack(side=TOP, fill=X, expand=Y)
        
        self.colorList = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet']
        self.lbl = ttk.Label()
        self.scale = ttk.Scale(from_=0, to=5, command=self._scale_update)
        
        self.lbl.pack(in_=demoPanel)
        self.scale.pack(in_=demoPanel)
        self.scale.set(0)
        
    def _scale_update(self, evt):
        idx = int(float(evt))
        color = self.colorList[idx]
        self.lbl.configure(foreground=color,
                           text='Color: {}'.format(color))
        
        
if __name__ == '__main__':
    ScaleDemo().mainloop()