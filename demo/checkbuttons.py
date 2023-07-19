# File: checkbuttons.py
# References:
#    http://www.tcl.tk/man/tcl8.5/TkCmd/ttk_checkbutton.htm

from tkinter import *
from tkinter import ttk
from demopanels import MsgPanel, SeeDismissPanel

class CheckbuttonDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='checkbuttondemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Checkbutton Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, 
                     ["Four checkbuttons are displayed below.  If you click on a button, ",
                      "it will toggle the button's selection state and set a control variable ",
                      "to a value indicating the state of the checkbutton.\n\n",
                      "The first button follows the state of the other three. ",
                      "If only some of the three are checked, the first button will ",
                      "display the 'alternate' (tri-state) mode."]
                      )
            
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = ttk.Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
        
        left = self._create_btn_panel(demoPanel)    # checkbuttons
        right = self._create_var_panel(demoPanel)   # checkbutton variables
        
        left.pack(side=LEFT, expand=True, padx=10, fill=BOTH)
        right.pack(side=LEFT, expand=True, padx=10, fill=BOTH)

    def _create_var_panel(self, parent):
        # panel to display check button variable values
        right = ttk.LabelFrame(parent, text='Checkbutton Control Variables')
        
        self.vb0 = ttk.Label(right, font=('Courier', 10))
        self.vb1 = ttk.Label(right, font=('Courier', 10))
        self.vb2 = ttk.Label(right, font=('Courier', 10))    
        self.vb3 = ttk.Label(right, font=('Courier', 10))  
        
        self.vb0.pack(anchor=NW, pady=3)
        self.vb1.pack(anchor=NW, pady=3)
        self.vb2.pack(anchor=NW, pady=3)
        self.vb3.pack(anchor=NW, pady=3)  
        
        self._show_vars()   
        
        return right

    def _show_vars(self):
        # set text for labels in var_panel to include the control 
        # variable name and current variable value
        self.vb0['text'] = '{:<8} {:<8}'.format('safety:', self.safety.get())
        self.vb1['text'] = '{:<8} {:<8}'.format('wipers:', self.vars[0].get())
        self.vb2['text'] = '{:<8} {:<8}'.format('brakes:', self.vars[1].get())
        self.vb3['text'] = '{:<8} {:<8}'.format('sober:', self.vars[2].get())
            
    def _create_btn_panel(self, parent):
        # frame to hold the check buttons
        left = ttk.LabelFrame(parent, text='Checkbuttons')
        
        # control variables linked to check buttons
        self.safety = StringVar(value='none')   # group monitor
        
        wipers = IntVar()
        brakes = IntVar()
        sober = IntVar()
        
        self.vars = [wipers, brakes, sober]
        
        # check buttons
        self.b0 = ttk.Checkbutton(left, text='Safety Check', variable=self.safety,
                             onvalue= 'all', offvalue='none', command=self._safety_changed)
        b1 = ttk.Checkbutton(left, text='Wipers OK', variable=wipers, command=self._value_changed)
        b2 = ttk.Checkbutton(left, text='Brakes OK', variable=brakes, command=self._value_changed)
        b3 = ttk.Checkbutton(left, text='Driver Sober', variable=sober, command=self._value_changed)

        # pack the buttons
        self.b0.pack(side=TOP, pady=2, anchor=W)
        
        for b in [b1, b2, b3]:
            b.pack(side=TOP, pady=2, padx=15, anchor=W)
        
        return left
            
    def _safety_changed(self):
        # all or none other check buttons selected
        if self.safety.get() != 'partial':
            value = 0   # deselect all
            
            if self.safety.get() == 'all':
                value = 1   # select all
            
            # select or deselect other buttons
            for i in range(len(self.vars)):
                self.vars[i].set(value)
                
        self._show_vars()
    
    def _value_changed(self):        
        # get check button values
        values = []
        for i in range(len(self.vars)):
            values.append(self.vars[i].get())
            
        if 0 not in values:         # all check buttons selected
            self.safety.set('all')  # set safety check button to 'all'
        else:
            # all not selected, set safety to 'partial'
            self.safety.set(value='partial')
            
            # change safety check button visual state 
            # to 'indefinite', neither checked nor empty
            self.b0.state(['alternate'])  
            
        self._show_vars()
        
    
if __name__ == '__main__':
    CheckbuttonDemo().mainloop()