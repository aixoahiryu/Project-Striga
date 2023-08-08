# File: canvasruler.py
#     http://infohost.nmt.edu/tcc/help/pubs/tkinter//canvas.html

from tkinter import *
from tkinter import ttk
from demopanels import MsgPanel, SeeDismissPanel

class CanvasRulerDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='canvasrulerdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Canvas Ruler Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, 
                     ["This canvas widget shows a mock-up of a ruler.  You can ",
                      "create tab stops by dragging them out of the well to the ",
                      "right of the ruler.  You can also drag existing tab stops.  ",
                      "If you drag a tab stop far enough up or down so that it ",
                      "turns dim, it will be deleted when you release the mouse button."])
            
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP)
        
        self.canvas = Canvas(width='14.8c', height='2.5c')
        self.canvas.pack(in_=demoPanel, side=TOP, fill=X)

        self._define_ruler()
        self._draw_ruler()
        self._create_bindings()
        
    def _define_ruler(self):
        # ruler dimensions and tab styles
        # winfo_fpixels() translates centimeters (c) to pixels
                
        d = {'grid': '.25c',
             'left': self.canvas.winfo_fpixels('1c'),
             'right': self.canvas.winfo_fpixels('13c'),
             'top': self.canvas.winfo_fpixels('1c'),
             'bottom': self.canvas.winfo_fpixels('1.5c'),
             'size': self.canvas.winfo_fpixels('.2c'),
             'x': 0,
             'y': 0,
             'normal': {'fill': 'black', 'stipple': ''},
             'active': {'fill': 'red', 'stipple': ''},
             'delete': {'fill': 'red', 'stipple': 'gray25'}
             }
         
        self.canvas.rulerInfo = d
        
    def _draw_ruler(self):
        # base line and end ticks
        self.canvas.create_line('1c 0.5c 1c 1c 13c 1c 13c 0.5c', width=1)
        
        # tick lines at 1/4, 1/2, 3/4 and 1cm positions
        for i in range(12):
            x = i + 1
            self.canvas.create_line('{0}c 1c {0}c 0.6c'.format(x), width=1)
            self.canvas.create_line('{0}.25c 1c {0}.25c 0.8c'.format(x), width=1)
            self.canvas.create_line('{0}.5c 1c {0}.5c 0.7c'.format(x), width=1)
            self.canvas.create_line('{0}.75c 1c {0}.75c 0.8c'.format(x), width=1)
            self.canvas.create_text('{}.15c .75c'.format(x), text=i, anchor='sw')
            
        # draw tab well
        self.canvas.create_rectangle('13.2c 1c 13.8c 0.5c', 
                                     outline='black', 
                                     tag=('well',))
        
        # add tab symbol to 'well'
        x = self.canvas.winfo_pixels('13.5c')
        y = self.canvas.winfo_pixels('.65c')
        self.canvas.addtag_withtag('well', 
                                   self._draw_tab(x, y))     
    
    def _draw_tab(self, x, y):
        # create a filled triangle to represent a tab stop
        size = self.canvas.rulerInfo['size']
        tab = self.canvas.create_polygon(x, y, 
                                         x+size, y+size,
                                         x-size, y+size)
        return tab

    # ==============================================================================
    # Create bindings
    # ==============================================================================
    def _create_bindings(self):
        self.canvas.tag_bind('well', '<1>', self._new_tab)
        self.canvas.tag_bind('tab', '<1>', self._sel_tab)
        self.canvas.bind('<B1-Motion>', self._move_tab)
        self.canvas.bind('<Any-ButtonRelease-1>', self._release_tab)


    # ==============================================================================
    # Bound methods - create, re-position and alter the appearance of a tab
    # ==============================================================================
    def _new_tab(self, evt):
        # triggered when the user clicks the tab in the 'well'
        # creates a new tab (triangle) and sets it as the
        # active object on the canvas, moving it to the rulers
        # edge
        x = evt.x
        y = evt.y
        tab = self._draw_tab(x,y)
        self.canvas.itemconfigure(tab, tag=('active', 'tab'))
        self.canvas.itemconfigure('active', self.canvas.rulerInfo['active'])
        self.canvas.rulerInfo['x'] = x
        self.canvas.rulerInfo['y'] = y
        
        self._move_tab(evt)

    def _sel_tab(self, evt):
        # triggered when the user clicks on a tab stop
        # position information is remembered to allow dragging
        grid = self.canvas.rulerInfo['grid']
        self.canvas.rulerInfo['x'] = self.canvas.canvasx(evt.x, grid)
        self.canvas.rulerInfo['y'] = self.canvas.rulerInfo['top'] + 2
        self.canvas.addtag_withtag('active', 'current')
        self.canvas.itemconfigure('active', self.canvas.rulerInfo['active'])

    def _move_tab(self, evt):
        # triggered when the user clicks and drags a tab stop
        # the tab position changes as does it's appearance if
        # it is dragged beyond the ruler's boundaries
        if not self.canvas.find_withtag('active'):
            return
        
        grid = self.canvas.rulerInfo['grid']
        
        cx = self.canvas.canvasx(evt.x, grid)
        cy = self.canvas.canvasy(evt.y)

        if cx < self.canvas.rulerInfo['left']:
            cx = self.canvas.rulerInfo['left']
        if cx > self.canvas.rulerInfo['right']:
            cx = self.canvas.rulerInfo['right']
            
        if( cy >= self.canvas.rulerInfo['top'] 
            and cy <= self.canvas.rulerInfo['bottom'] ):
            cy = self.canvas.rulerInfo['top'] + 2
            self.canvas.itemconfigure('active', 
                                      self.canvas.rulerInfo['active'])
        else:
            cy = cy - self.canvas.rulerInfo['size'] - 2
            self.canvas.itemconfigure('active', 
                                      self.canvas.rulerInfo['delete'])
            
        self.canvas.move('active', 
                         cx - self.canvas.rulerInfo['x'],
                         cy - self.canvas.rulerInfo['y'])
            
        self.canvas.rulerInfo['x'] = cx
        self.canvas.rulerInfo['y'] = cy

    def _release_tab(self, evt):
        # triggered when the user releases the mouse
        # if the tab has been dragged beyond the ruler boundaries
        # it is deleted
        if not self.canvas.find_withtag('active'):
            return

        if self.canvas.rulerInfo['y'] != self.canvas.rulerInfo['top'] + 2:
            self.canvas.delete('active')
        else:
            self.canvas.itemconfigure('active',
                                      self.canvas.rulerInfo['normal'])
            self.canvas.dtag('active')
            

if __name__ == '__main__':
    CanvasRulerDemo().mainloop()