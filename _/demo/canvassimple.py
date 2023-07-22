# File: canvassimple.py
#    http://infohost.nmt.edu/tcc/help/pubs/tkinter//canvas.html#create_rectangle
#    http://www.tcl.tk/man/tcl8.5/TkCmd/canvas.htm
#
# Ref: canvasscroll.py from
#    http://tkinter.unpythonic.net/wiki/A_tour_of_Tkinter_widgets


from tkinter import *
from tkinter import ttk
from demopanels import MsgPanel, SeeDismissPanel

# ===========================================================================
# Constants
# ===========================================================================
SQUARE = 60     # width and height of rect
PAD = 20        # padding around rectangles
SIDE = SQUARE + PAD

ROWS = 10       # num of rows
COLS = 20       # num of rect in a row

BG_FILL = 'gray90'  # background fill colour
CUR_FILL = 'cyan'   # selected rectangle fill colour

# ===========================================================================
# Class
# ===========================================================================
class SimpleCanvasDemo(ttk.Frame):
        
    def __init__(self, isapp=True, name='simplecanvasdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Simple Canvas Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, 
                     ["This window displays a canvas widget that can be ",
                      "scrolled either by using the scrollbars or by right ",
                      "clicking in a rectangle and dragging the mouse ",
                      "horizontally and/or vertically.\n\n",
                      "Click on a rectangle and its indices will be displayed ",
                      "in the label area below the canvas."])
            
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
        
        # create text label
        lbl = ttk.Label(text='Selected Rectangle: ', 
                        background='LightGoldenrod1',
                        font=('Helv', '10', 'bold'))
        lbl.pack(in_=demoPanel, side=BOTTOM, fill=X, 
                 expand=Y, pady=10, padx=5)
        
        # create a canvas with rectangles
        canvas = self._create_grid(demoPanel)
        self._create_rects(canvas)
        self._create_bindings(canvas, lbl)
        
    # ===========================================================================
    # Canvas
    # ===========================================================================                
    def _create_grid(self, parent):
        # frame to hold canvas
        grid = ttk.Frame(parent)
        grid.pack(expand=Y, fill=BOTH, padx=1, pady=1)
        
        # scrollable canvas (must set scrollregion)
        c = Canvas(relief=SUNKEN, borderwidth=2,
                   background=BG_FILL,
                   scrollregion=(0,0, 
                                 COLS*SIDE+PAD, 
                                 ROWS*SIDE+PAD))  # (W,N,E,S)
        
        hscroll = ttk.Scrollbar(orient=HORIZONTAL, command=c.xview)
        vscroll = ttk.Scrollbar(orient=VERTICAL, command=c.yview)

        c['xscrollcommand'] = hscroll.set
        c['yscrollcommand'] = vscroll.set
                
        # set canvas and scrollbar positions and
        # resize behaviours
        grid.rowconfigure(0, weight=1, minsize=0)
        grid.columnconfigure(0, weight=1, minsize=0)

        c.grid(in_=grid, padx=1, pady=1, row=0, column=0,
               rowspan=1, columnspan=1, sticky='news')
        vscroll.grid(in_=grid, padx=1, pady=1, row=0,
                     column=1, rowspan=1, columnspan=1,
                     sticky='news')
        hscroll.grid(in_=grid, padx=1, pady=1, row=1,
                     column=0, rowspan=1, columnspan=1,
                     sticky='news')
        
        return c

    def _create_rects(self, c):
        # create 10 rows of rectangles,
        # with 20 rectangles per row
        # initial colour matches canvas bg
        # each rectangle is 'tagged' with its name
        # (same as text displayed in the rectangle)
        
        for i in range(COLS): # columns
            x = PAD + ( i * SIDE)
            for j in range(ROWS): # rows
                y = PAD + (j * SIDE)
                name = '{},{}'.format(i,j)  
                c.create_rectangle(x, y, x+SQUARE, y+SQUARE,
                                   outline='black',
                                   fill=BG_FILL,
                                   tags=('rect', name))
                
                c.create_text(x+(SQUARE/2), y+(SQUARE/2),
                              text=name,
                              anchor=CENTER,
                              tags=('text', name))

    # ===========================================================================
    # Canvas Bindings
    # ===========================================================================
    def _create_bindings(self, canvas, lbl):        
        # highlight rectangle under mouse
        canvas.tag_bind('all', '<Any-Enter>', self._enter_rect )
        canvas.tag_bind('all', '<Any-Leave>', self._leave_rect )
        
        # display rectangle indices on 'select'
        canvas.tag_bind('all', '<1>', 
                        lambda evt, l=lbl, c=canvas: self._sel_rect(c, l))
        
        # drag canvas (scroll using right mouse button)
        canvas.tag_bind('all', '<3>', 
                        lambda evt, c=canvas: self._begin_drag(evt, c))
        canvas.tag_bind('all', '<B3-Motion>', 
                        lambda evt, c=canvas: self._drag_canvas(evt, c))

    # ===========================================================================
    # Canvas bound methods (callbacks)
    # ===========================================================================
    def _sel_rect(self, canvas, label):
        item = self._get_current_rect(canvas)  # selected object
        tags = canvas.gettags('current')       # associated tags
        for t in tags:  
            if t not in ('rect', 'current', 'text'): 
                # tag must be the object name               
                label['text'] = 'Selected Rectangle: ({})'.format(t)

    def _enter_rect(self, evt):
        w = self.nametowidget(evt.widget)     # get canvas
        item = self._get_current_rect(w)      # get selected rect
        w.itemconfigure(item, fill=CUR_FILL)  # change fill colour

    def _leave_rect(self, evt):
        w = self.nametowidget(evt.widget)   # get canvas
        item = self._get_current_rect(w)    # get selected rect
        w.itemconfigure(item, fill=BG_FILL) # change fill colour

    def _get_current_rect(self, c):
        item = c.find_withtag('current')  # id of current item
        tags = c.gettags('current')       # associated tags
        if 'text' in tags:                # text item?
            item = c.find_below(item)     # id of containing rect
            
        return item

    # drag canvas (scroll)
    def _begin_drag(self, evt, canvas):
        canvas.scan_mark(evt.x, evt.y)  # initial right-mouse click
        
    def _drag_canvas(self, evt, canvas): 
        canvas.scan_dragto(evt.x, evt.y) # capture dragging

# ===========================================================================
# Main
# ===========================================================================
if __name__ == '__main__':
    SimpleCanvasDemo().mainloop()